//////////////
// docs.js //
/////////////

function updateQueryStringParameter(uri, key, value) {
    var re = new RegExp("([?&])" + key + "=.*?(&|$)", "i");
    var separator = uri.indexOf("?") > -1 ? "&" : "?";
    if (uri.match(re)) {
        return uri.replace(re, "$1" + key + "=" + value + "$2");
    }
    else {
        return uri + separator + key + "=" + value;
    }
}
function getParameterByName(name, queryString) {
    name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
    var regexS = '(?:\\?|&(?:amp;)?)(' + name + ')(?:=?([^&#]*))';
    var regex = new RegExp(regexS, 'g');
    var results;
    var resultsAsAList = [];
    queryString = queryString || window.location.search;
    while (results = regex.exec(queryString)) {
        resultsAsAList.push(decodeURIComponent(results[2].replace(/\+/g, " ")));
    }
    return resultsAsAList;
}
function updateNavigation(e) {
    var $this = $(this);
    var $active = $this.find('.active');
    if ($active.length != 1) {
        return;
    }
    var currentTopic = $active.first().find('a').first();
    window.location = currentTopic.attr('href');
    $('.nav.nav-list').scrollTo('.active', 100, {offset : -100});
    //window.history.replaceState({}, null, currentTopic.attr('href'));
    //console.log(currentTopic.attr('href'));
}
$(document).ready(function () {
    //HIDE OVERVIEW REQUEST BOXES:
    var $overview_content = $('#overview-content');
    $overview_content.find('.request > p:first-child').hide();
    $overview_content.find('.response > p:first-child').hide();

   //BIND URL UPDATE
   $("li").bind('activate', updateNavigation);
    function update_lang_head(text){
        var lang_head = $('#lang-dropdown-head');
        lang_head.html(text + " <b class='caret'></b>")
    }

    //LOAD DEFAULT LANGUAGE
    var default_lang = getParameterByName('language', window.location.href);
    default_lang = (default_lang.length > 0) ? default_lang[0] : 'bash';
    default_lang_dd = $("[data-lang='" + default_lang +"']");
    update_lang_head(default_lang_dd.text());
    default_lang_dd.parent().hide();
    $("[class^='highlight-']").hide();
    $(".highlight-" + default_lang).show();
    $('.highlight-javascript').show();
    $('.highlight-html').show();


    //SWAP LANGUAGE METHODS
    $('.lang-change').click(function () {
        var lang = $(this).attr('data-lang');
        var langtext = $(this).text();
        update_lang_head(langtext);
        var parent = $(this).parent();
        parent.siblings().show();
        parent.hide();
        $("[class^='highlight-']").hide();
        $(".highlight-javascript").show();
        $(".highlight-" + lang).show();
        var uri = updateQueryStringParameter(window.location.pathname + window.location.search, 'language', lang);
        uri = uri + '' + window.location.hash;
        console.log(window.location.hash);
        console.log(uri);
        window.location = uri;
        //window.history.replaceState(null, null, uri);
        $('[data-spy="scroll"]').each(function () {
            var $spy = $(this).scrollspy('refresh');
        });
    });


    //SIDEBAR TO STICK TO BOTTOM
    function fix_sidebar(){
        var window_height = $(window).height();
        var top_of_sidebar = 314;
        var height_of_sidebar = window_height - top_of_sidebar;
        $('.nav.nav-list').css('height', height_of_sidebar);
    }
    $(window).resize(function (){
        fix_sidebar();
    });
    //FIX ON LOAD
    fix_sidebar();

    //SWITCH SELECTORS
    $('#context-selector > li').click(function (){
        window.location = $(this).find('a').attr('href');
    });

    // VERSION SELECTOR
    var default_version = "rev0";
    try {
	default_version = locaiton.pathname.split('/')[1];
    } catch(e) {}
    var version_element = $("[data-version='" + default_version + "']")
    version_element.parent().hide();
    $("#version-dropdown-head").html(version_element.html() + ' <b class="caret"></b>');
    $("#version-dropdown-head > .version-change").removeClass("version-change").attr('href', '#');
    $("[class^=rev-]").hide();
    $(".rev-"+default_version).show();
    $("a.version-change").click(function() {
	var $this = $(this);
	var href = $this.attr('href');
	var path = location.pathname.split('/');
	path.shift(); path.shift();
	location.href = href + '/' + path.join('/') + location.hash;
	return false;
    });

});
