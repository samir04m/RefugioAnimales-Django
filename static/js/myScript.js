$(document).ready(function() {
    $('select').material_select();

    $('.dropdown-button').dropdown({
         belowOrigin: true,
         constrainWidth: false
    });

    $('#btnLogin').click(function(){
        if ($('#id_username').val() != "" && $('#id_password').val() != ""){
            $(this).addClass("hide");
            $("#preloader").removeClass('hide');
        }
    });
});
