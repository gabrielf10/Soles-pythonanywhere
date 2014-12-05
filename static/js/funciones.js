$('.containerlittle').hide();

$(window).scroll(function (event) {
    var scroll = $(window).scrollTop();
    if (scroll > 450) {
        $('.containerlittle').show();
    } else {
        $('.containerlittle').hide();
    }
});
$('.menu a').click(function() {
    $('.menu .selected').removeClass('selected');
    $(this).addClass('selected');
});

$('.menufotorama li').click(function() {
    $('.menufotorama .selected').removeClass('selected');
    $(this).addClass('selected');
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

        

