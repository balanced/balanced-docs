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

    var current_version;

    function change_version(vers) {
	if(vers == current_version) return;
	current_version = vers;

	var version_element = $("[data-version='" + vers + "']");
	if(!version_element.length) {
	    throw new Error('Version '+vers+' not found');
	}
	$('ul.version > li').show();
	version_element.parent().hide();
	$("#version-dropdown-head").html(version_element.html() + ' <b class="caret"></b>');
	$("#version-dropdown-head > .version-change").removeClass("version-change").attr('href', '#');

	$('div[class^=api-version]').hide();
	$('div.api-version-'+vers).show();

	$("[class^=rev-]").hide();
	$(".rev-"+vers).show();

	var new_hash = location.hash.replace(/rev(\w+)/, vers);

	fix_sidebar();
	$('[data-spy="scroll"]').each(function () {
           $(this).scrollspy('refresh');
        });

	location.hash = new_hash;
	//$.scrollTo(new_hash);

	//history.pushState(null, '', new_hash);

    }

    $("div[class^=api-version]").each(function () {
	var $container = $(this);
	var vers = /rev\w+/.exec($container.attr('class'))[0];
	$container.find('a').each(function () {
	    var $a = $(this);
	    var href = $a.attr('href');
	    if(href[0] == '#') {
		$a.attr('href', '#'+vers+'-'+href.substring(1));
	    }
	});
	$container.find('section').each(function () {
	    var $section = $(this);
	    var id = $section.attr('id');
	    id && $section.attr('id', vers+'-'+id);
	});
    });

    $(window).on('hashchange', function (){
	var vers = /(rev\w+)-/.exec(location.hash)[1];
	change_version(vers);
    });

    $('a.version-change').click(function () {
	var $this = $(this);
	var ver = $this.attr('data-version');
	change_version(ver);
	$('ul.nav-api-version').find('.dropdown-toggle').dropdown('toggle')
	return false;
    });

    change_version(/rev\w+/.exec(location.hash)[0] || 'rev0');

});
