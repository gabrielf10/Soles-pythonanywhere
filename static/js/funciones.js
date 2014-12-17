//oculta menu pequeño
$(function() {
     $('.containerlittle').hide(0).delay(0);
});

//valida formulario
$("#bEnviar").click(function(){
    //expresion regular para email
    var expr = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$/;
    //expresion regular solo letras
    var expr1 = /^[a-zA-Z_áéíóúñ\s]*$/;
    //expresion regular para telefono
    var expr2 = /^\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d$/;
    var nombre = $("#name").val();
    var email = $("#email").val();
    var tel = $("#tel").val();
    //valida nombre
                if(nombre == "" || !expr1.test(nombre)){
                    $("#mensaje1").fadeIn("slow");
                    $( "#name" ).focus();
                    return false;
                }
                else{
                    $("#mensaje1").fadeOut();

                if(email == "" || !expr.test(email)){
                        $("#mensaje2").fadeIn("slow");
                        $( "#email" ).focus();
                        return false;
                    }
                    else{
                        $("#mensaje2").fadeOut();

                if(tel == "" || !expr2.test(tel)){
                        $("#mensaje3").fadeIn("slow");
                        $( "#tel" ).focus();
                        return false;
                    }
                    else{
                        $("#mensaje3").fadeOut();
                    }
                    }
                }
    //valida email
 
            });


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

        

