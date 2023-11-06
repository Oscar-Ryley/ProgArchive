adjective_list = ["blue", "red", "yellow", "hungry", "pink", "scary", "desperate"]
noun_list = ["Dog", "Ant", "Cat", "Lemur", "Leopard", "Elephant"]
verb_list = ["eats", "juggles", "eats", "jumps", "hops", "runs"]
adverb_list = ["lazily", "quickly", "ferociously"]

function create_poetry () {
    return String("The " 
    + adjective_list[Math.floor(Math.random()*adjective_list.length)] + " " 
    + noun_list[Math.floor(Math.random()*noun_list.length)] + " " 
    + verb_list[Math.floor(Math.random()*verb_list.length)] + " " 
    + adverb_list[Math.floor(Math.random()*adverb_list.length)]
    )
}

let button = document.getElementById("generate");
function output_poetry(){
    document.getElementById("poetry").innerHTML = ("<h1>" + create_poetry() +"</h1>");
}
button.addEventListener("click", output_poetry);