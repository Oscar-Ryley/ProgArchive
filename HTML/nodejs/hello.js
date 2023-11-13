const http = require('http');
var fs = require('fs')
const hostname = '127.0.0.1';
const port = 8080;

fs.readFile('index.html', function(error,html){
    if (error) throw error;
    const server = http.createServer(function(req, res){
        res.writeHeader(200, {"Content-Type": "text/html"});
        res.write(html);
        res.end();
    });
    server.listen(port, hostname, () => {
        console.log(`Server running at http://${hostname}:${port}/`);
      });
});