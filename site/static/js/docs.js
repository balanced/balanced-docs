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
    window.history.replaceState({}, null, currentTopic.attr('href'));
    $('.nav.nav-list').scrollTo('.active', 100, {offset : -100});
    //console.log(currentTopic.attr('href'));
}
$(document).ready(function () {
    //SIDEBAR TO STICK TO BOTTOM
    function fix_sidebar(){
        var window_height = $(window).height();
        var top_of_sidebar = 300;
        var height_of_sidebar = window_height - top_of_sidebar;
        $('.nav.nav-list').css('height', height_of_sidebar);
    }

    $(window).resize(function (){
        fix_sidebar();
    });

    //FIX ON LOAD
    fix_sidebar();

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

    $('a').each(function() {
        if ($(this).attr('href') != null) {
            if ($(this).attr('href').indexOf("api.html") != -1 ||
                $(this).attr('href').indexOf("overview.html") != -1) {
                    var href = $(this).attr('href');
                    var insertPos = href.indexOf('.html') + 5;
                    if (href.indexOf('?') != -1) {
                        insertPos += 1;
                    }
                    $(this).attr('href', [href.slice(0, insertPos), "?language=" + default_lang, href.slice(insertPos)].join(''));
                }
        }
    });
    
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

    //SWITCH SELECTORS
    $('#context-selector > li').click(function (){
        window.location = $(this).find('a').attr('href');
    });

    // VERSION SELECTOR
    var default_version = "rev0";
    try {
	    default_version = location.pathname.split('/')[1];
    }
    catch(e) {}
    var version_element = $("[data-version='" + default_version + "']");
    if(!version_element.length) {
	    default_version='rev0';
    	version_element = $("[data-version=rev0]");
    }
    version_element.parent().hide();
    $("#version-dropdown-head").html(version_element.html() + ' <b class="caret"></b>');
    $("#version-dropdown-head > .version-change").removeClass("version-change").attr('href', '#');
    $("[class^=rev-]").hide();
    $(".rev-"+default_version).show();
    $("a.version-change").click(function() {
    	var $this = $(this);
    	var href = $this.attr('data-version');
    	location.href = location.href.replace(/rev\d+/, href);
    	return false;
    });
});
