$('.containerlittle').hide(0).delay(0);
function probando(){
    location.reload();
}

$(window).scroll(function (event) {
    var position_inicio = $('#inicio').position();
    var position_nuestrahistoria = $('#nuestrahistoria').position();
    var position_nuestrostrabajos = $('#nuestrostrabajos').position();
    var position_contacto = $('#contacto').position();

    var scroll = $(window).scrollTop();
    if (scroll > 450) {
        $('.containerlittle').show();
    } else {
        $('.containerlittle').hide();
    }
    if(scroll < position_inicio.top -50){
        $('.menu .selected').removeClass('selected');
    }

    if(scroll >= position_inicio.top -50){
        $('.menu .selected').removeClass('selected');
        $('a[href="#inicio"]').addClass('selected');
    }
    if(scroll >= position_nuestrahistoria.top -50){
        $('.menu .selected').removeClass('selected');
        $('a[href="#nuestrahistoria"]').addClass('selected');
    }
    if(scroll >= position_nuestrostrabajos.top -50){
        $('.menu .selected').removeClass('selected');
        $('a[href="#nuestrostrabajos"]').addClass('selected');
    }
    if(scroll >= position_contacto.top -50){
        $('.menu .selected').removeClass('selected');
        $('a[href="#contacto"]').addClass('selected');
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
        $('#fotorama1').show();
        $(".imgFadeIn").hide(0).fadeIn(3000);
        $(".portada").hide(0).fadeIn(3000);

    });

    $(".fotorama-nav li").click(function(){
        var show = $(this).attr("data-show");
        $(".fotorama").hide();
        $(show).fadeIn();
    })
});

        

