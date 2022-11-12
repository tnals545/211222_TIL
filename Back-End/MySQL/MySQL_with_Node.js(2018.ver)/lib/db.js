var mysql = require("./lib/db");
var db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "slaustkd545",
  database: "opentutorials",
});
db.connect();

module.exports = db;
