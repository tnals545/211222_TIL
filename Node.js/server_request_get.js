var http = require('http');

var url = require('url');

var querystring = require('querystring');

var server = http.createServer(function(request,response){
    console.log('--- log start ---');

    var parsedUrl = url.parse(request.url);
    console.log(parsedUrl);

    var parsedQuery = querystring.parse(parsedUrl.query,'&','=');
    console.log(parsedQuery);

    console.log('--- log end ---');

    response.writeHead(200, {'Content-Type':'text/plain; charset=utf-8'});
    // response.end('Hello node.js!!');
    // response.end('var1의 값은 '+parsedQuery.var1);
    response.end('var1의값=' + parsedQuery.var1 + ', var2의값=' + parsedQuery.var2 + ', var3의값=' +parsedQuery.var3);
});

server.listen(8080, function(){
    console.log('Server is running...');
});