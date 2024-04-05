window.addEventListener("scroll",function(){
    var nav =document.querySelector("nav");
    nav.classList.toggle("blur",window.scrollY > 0);
});