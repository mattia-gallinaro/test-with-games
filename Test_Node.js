const http = require('http');
const url = require('url')

http.createServer(function (req, res){
    res.writeHead(200, {'Context-Type':'text/html'});
    res.write('Hello World');
    var u = url.parse(req.url, true).query;
    var text = u.year + " " + u.month;
    console.log(typeof(u.year))
    res.end(text);
}).listen(8080)