const express = require('express');
const app = express();
app.use(express.urlencoded({ extended: false })); //Parse URL-encoded bodies

var recipes = require('./potato_recipes.json');

app.get('/', function(req, resp){
    let item = 0
    let qreq = req.query.query
    for (let i = 0; i < recipes.length; i++){
        if (recipes[i].title = qreq) {
            item = i
        }
    }
    resp.send("Title: " + recipes[item].title + 
    "\n Ingredients: " + recipes[item].ingredients +
    "\n Servings: " + recipes[item].servings + 
    "\n Instructions: " + recipes[item].instructions)
})

app.post('/p', function(req, resp){ 
    resp.send('POST!')
});

app.listen(8090);