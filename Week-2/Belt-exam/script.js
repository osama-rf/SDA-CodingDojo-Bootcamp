const cartButton = document.getElementById("cart-button")
const accpetCookiesButton = document.getElementById("accept-cookies-button");
const sliderImage = document.getElementById("slider-pic")
const cookiesNotification = document.getElementById("cookies-notification");

cartButton.addEventListener('click', () => {
    alert("Your Cart is empty!!")
})

sliderImage.addEventListener('mouseover', () => {
    // replace image src
    sliderImage.src = "./assets/succulents-2.jpg"
})

sliderImage.addEventListener('mouseout', () => {
    // replace image src
    sliderImage.src = "./assets/succulents-1.jpg"
})

accpetCookiesButton.addEventListener('click', () => {
    cookiesNotification.style.display = "none"
})

