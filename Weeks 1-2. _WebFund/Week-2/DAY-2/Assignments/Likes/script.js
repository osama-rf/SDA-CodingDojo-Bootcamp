

function AddLike(element) {
    const likes = element.parentElement.querySelector("p #liked");
    let numlike = parseInt(likes.innerText);
    
    
    likes.innerText = numlike +1;
}


