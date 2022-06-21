// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function() {scrollFunction()};
/*
function scrollFunction() {

    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        document.getElementById("navbar").style.padding = "30px 10px";
        document.getElementById("logo").style.fontSize = "25px";
    } else {
        document.getElementById("navbar").style.padding = "80px 10px";
        document.getElementById("logo").style.fontSize = "35px";
    }
}
*/
function scrollFunction() {
    window.addEventListener("scroll", function() {
        var elementTarget = document.getElementById("header");
        if (window.scrollY > (elementTarget.offsetTop + elementTarget.offsetHeight) && document.getElementById("navbar").classList.contains("m-fadeOut")) { //scroll past
            document.getElementById("navbar").classList.add("m-fadeIn");
            document.getElementById("navbar").classList.remove("m-fadeOut");
            //document.getElementById("navbar").style.visibility = "visible";
        }
        else if (window.scrollY < (elementTarget.offsetTop + elementTarget.offsetHeight) && document.getElementById("navbar").classList.contains("m-fadeIn")){
            document.getElementById("navbar").classList.add("m-fadeOut");
            document.getElementById("navbar").classList.remove("m-fadeIn");
            //document.getElementById("navbar").style.visibility = "hidden";
            //document.getElementById("navbar").style.padding = "30px 10px";
            //document.getElementById("logo").style.fontSize = "25px";
        }
    });
}