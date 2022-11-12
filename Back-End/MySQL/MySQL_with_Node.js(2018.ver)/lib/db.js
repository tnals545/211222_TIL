var mysql = require("mysql");
var db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "slaustkd545",
  database: "opentutorials",
});
db.connect();

module.exports = db;
