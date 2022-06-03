function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var createPizaa = {};
    createPizaa.crustType = crustType;
    createPizaa.sauceType = sauceType; 
    createPizaa.cheeses = cheeses;
    createPizaa.toppings = toppings;
    return createPizaa;
}

var p1 = pizzaOven("deep dish", "traditional", ["mozzarella", "feta"], ["pepperoni", "sausage"]);
console.log(p1);

var p2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"],["mushrooms", "olives", "onions"]);
console.log(p2);

var p3 = pizzaOven("crust tossed", "marinara", ["mozzarella", "feta"],["mushrooms", "olives", "onions"]);
console.log(p3);

var p4 = pizzaOven("ban tossed", "marinara", ["mozzarella", "feta"],["mushrooms", "olives", "onions"]);
console.log(p4);


var crustTypes = [
    "deep dish",
    "hand tossed",
    "thin and crispy",
    "cauliflower",
    "gluten free",
    "hawaiian bread"
];

var sauceTypes = [
    "traditional",
    "marinara",
    "bbq",
    "white sauce",
    "nacho cheese",
    "tikka masala"
];

var cheeses = [
    "mozzarella",
    "cheddar",
    "feta",
    "swiss cheese",
    "blue cheese",
    "goat cheese",
    "provolone",
    "parmesan",
    "vegan cheese"
];

var toppings = [
    "pepperoni",
    "sausage",
    "chicken",
    "corn",
    "olives",
    "bell peppers",
    "onions",
    "mushrooms",
    "anchovies"
];

function randomRange(max, min) {
    return Math.floor(Math.random() * max - min) + min;
}

function randomPick(arr) {
    var i = Math.floor(arr.length * Math.random());
    return arr[i];
}

function randomPizza() {
    var pizza = {};
    pizza.crustType = randomPick(crustTypes);
    pizza.sauceType = randomPick(sauceTypes);
    pizza.cheeses = [];
    pizza.toppings = [];
    for(var i=0; i<randomRange(5, 1); i++) {
        pizza.cheeses.push(randomPick(cheeses));
    }
    for(var i=0; i<randomRange(4, 0); i++) {
        pizza.toppings.push(randomPick(toppings));
    }
    return pizza;
}

console.log(randomPizza())