$('.menu-little').hide();

$(window).scroll(function (event) {
    var scroll = $(window).scrollTop();
    if (scroll > 500) {
        $('.menu-little').show();
    } else {
        $('.menu-little').hide();
    }
});


$(function () {
    $('.fotorama').fotorama();
            
    $(document).ready(function(){
        $(".fotorama").hide();
    });

    $(".fotorama-nav li").click(function(){
        var show = $(this).attr("data-show");
        $(".fotorama").hide();
        $(show).fadeIn();
    })
});

        

