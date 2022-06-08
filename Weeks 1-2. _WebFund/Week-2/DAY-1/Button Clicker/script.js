function like(element) {
    var text = element.innerHTML;
    var number = "";
    for(i = 0 ; i < text.length ; i++) {
        if(!isNaN(text[i])){
            number +=text[i];
        } else if (text[i] = ""){
            break;
        } else {
            continue;
        }
    }
    element.innerHTML = ++number + " " + 'like';
    alert("Ninja was liked");
}

function remove(element){
    element.remove();
}

function isLoggedIn(element) {
    if(element.innerHTML == "Login"){
        element.innerHTML = "Logout";
    } else {
        element.innerHTML = "Login"
    }
}


