console.log("page loaded...");

const requestSpan = document.querySelector("#requests");
const connectionSpan = document.querySelector("#connections");
const username = document.querySelector("#username");

// functon for accept and ignore
function accept(id) {
    var element = document.querySelector(id);
    element.remove();
    requestSpan.innerText--;
    connectionSpan.innerText++;
}

function ignore(id) {
    var element = document.querySelector(id);
    element.remove();
    requestSpan.innerText -1;
}


// edit
function edit() {
    username.innerText = prompt("Your new name:");
}
