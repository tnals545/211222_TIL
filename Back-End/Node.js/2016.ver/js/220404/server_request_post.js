var http = require('http');
var querystring = require('querystring');

var server = http.createServer(function(request,response){
    var postdata = '';

    request.on('data', function(data){
        postdata = postdata + data;
    });


    request.on('end', function(){
        var parsedQuery = querystring.parse(postdata);

        console.log(parsedQuery);

        response.writeHead(200, {'Content-Type':'text/plain; charset=utf-8'});
        // response.end('var1의 값 = ' + result);
        response.end('var1의값=' + parsedQuery.var1 + ', var2의값=' + parsedQuery.var2 + ', var3의값=' +parsedQuery.var3);
    });
});

server.listen(8080, function(){
    console.log('Server is running...');
});