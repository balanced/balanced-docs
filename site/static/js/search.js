///////////////
// search.js //
///////////////

$('.search link').attr('href','/static/css/styles.css');


$( document ).ready(function() {
    setTimeout(function(){
        $('.gsc-input').attr('background-color', '#59606B')
        $('#gsc-i-id1').attr('style', "width: 100%; padding: 0px; border: none; margin: -0.0625em 0px 0px; height: 1.25em; outline: none; background-color: #59606B; background-position: 0% 50%; background-repeat: no-repeat no-repeat;")
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




