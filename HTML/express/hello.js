const express = require('express')
const app = express()

app.get('/', function(req, resp){
   resp.send('Hello world')
})

app.get('/wave/:at', function(req, resp){
   resp.send('waving at ' + String(req.params.at))
})

app.get('/p', function(req, resp){
   resp.send(req.query.person)
})

app.listen(8090)