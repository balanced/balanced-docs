///////////////
// search.js //
///////////////

$('.search link').attr('href','/static/css/styles.css');


$( document ).ready(function() {
    setTimeout(function(){
        $('.gsc-input').attr('background-color', '#59606B');
        $('#gsc-i-id1').addClass('google-remove-watermark');
        $('input#gsc-i-id1').blur(function () {
            var searchTerm = $('input#gsc-i-id1').val();
            sessionStorage.setItem('query',searchTerm)
            if (searchTerm.length != 0) {
                setTimeout(function () {
                    $('input#gsc-i-id1').val(searchTerm)
                }, 140)
            }
        });
        $('input#gsc-i-id1').val(sessionStorage.getItem('query'))
    }, 100);
});




