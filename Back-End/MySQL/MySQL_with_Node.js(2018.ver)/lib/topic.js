var db = require("./db");
var template = require("./template.js");
var url = require("url");
var qs = require("querystring");

exports.home = function (request, response) {
  db.query(`SELECT * FROM topic`, function (err, topics) {
    var title = "Welcome";
    var description = "Hello, Node.js";
    var list = template.list(topics);
    var html = template.HTML(
      title,
      list,
      `<h2>${title}</h2>${description}`,
      `<a href="/create">create</a>`
    );
    response.writeHead(200);
    response.end(html);
  });
};

exports.page = function (request, response) {
  var _url = request.url;
  var queryData = url.parse(_url, true).query;
  db.query(`SELECT * FROM topic`, function (err, topics) {
    if (err) {
      throw err;
    }
    db.query(
      `SELECT * FROM topic LEFT JOIN author ON topic.author_id=author.id WHERE topic.id=?`,
      [queryData.id],
      function (err2, topic) {
        if (err2) {
          throw err2;
        }
        var title = topic[0].title;
        var description = topic[0].description;
        var list = template.list(topics);
        var html = template.HTML(
          title,
          list,
          `
              <h2>${title}</h2>
              ${description}
              <p>by ${topic[0].name}</p>
              `,
          ` <a href="/create">create</a>
              <a href="/update?id=${queryData.id}">update</a>
              <form action="delete_process" method="post">
                <input type="hidden" name="id" value="${queryData.id}">
                <input type="submit" value="delete">
              </form>`
        );
        response.writeHead(200);
        response.end(html);
      }
    );
  });
};

exports.create = function (request, response) {
  db.query(`SELECT * FROM topic`, function (err, topics) {
    db.query(`SELECT * FROM author`, function (err2, authors) {
      var title = "Create";
      var list = template.list(topics);
      var html = template.HTML(
        title,
        list,
        `
            <form action="/create_process" method="post">
              <p><input type="text" name="title" placeholder="title"></p>
              <p>
                <textarea name="description" placeholder="description"></textarea>
              </p>
              <p>
                ${template.authorSelect(authors)}
              </p>
              <p>
                <input type="submit">
              </p>
            </form>
          `,
        `<a href="/create">create</a>`
      );
      response.writeHead(200);
      response.end(html);
    });
  });
};

exports.create_process = function (request, response) {
  var body = "";
  request.on("data", function (data) {
    body = body + data;
  });
  request.on("end", function () {
    var post = qs.parse(body);

    db.query(
      `INSERT INTO topic (title, description, created, author_id) VALUES(?, ?, NOW(), ?);`,
      [post.title, post.description, post.author],
      function (err, result) {
        if (err) {
          throw err;
        }
        response.writeHead(302, { Location: `/?id=${result.insertId}` });
        response.end();
      }
    );
  });
};
