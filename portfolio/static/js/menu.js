
$(document).ready(function() {
        if ($(window).width() < 801) {
            $('#des-menu').css("display", "none");
            $('#navigation').css("display", "block");
        }
        else {
            $('#des-menu').css("display", "block");
            $('#navigation').css("display", "none");
        }
    $(window).resize(function() {
        if ($(window).width() < 801) {
            $('#des-menu').css("display", "none");
            $('#navigation').css("display", "block");
        }
        else {
            $('#des-menu').css("display", "block");
            $('#navigation').css("display", "none");
        }
    })
})



