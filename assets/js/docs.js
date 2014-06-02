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
    $('.nav.nav-list').scrollTo('.active', 100, {offset : -150});
}
function scrollToAnchor(href) {
    var href = typeof(href) == "string" ? href : $(this).attr("href");
    var fromTop = 50;
    if (href != null && href.indexOf("#") == 0) {
        var $target = $(href);
        if ($target.length) {
            $('html, body').animate({ scrollTop: $target.offset().top - fromTop });
            if (history && "pushState" in history) {
                history.pushState({}, document.title, window.location.pathname + href);
                return false;
            }
        }
    }
}
function updateLangTitle(text){
    $('#lang-dropdown-head').html("lang: " + text + " <b class='caret'></b>");
}
$(document).ready(function () {
    var langParam = getParameterByName('language', window.location.href)[0];
    if (langParam != null) {
        $.cookie('language', langParam, { expires: 7, path: '/' });
    }

    function fix_sidebar() {
        var window_height = $(window).height();
        var top_of_sidebar = 65;
        var height_of_sidebar = window_height - top_of_sidebar;
        $('.nav.nav-list').css('height', height_of_sidebar);
    }

    $(window).resize(function (){
        fix_sidebar();
    });

    $(".nav.nav-list").mouseover(function() {
      $('body').addClass('freeze-scroll');
    });
    $(".nav.nav-list").mouseout(function() {
      $('body').removeClass('freeze-scroll');
    });

    $("li").bind('activate', updateNavigation);

    var defaultLang = defaultLang = $.cookie('language');
    defaultLang = (defaultLang != null) ? defaultLang : 'bash';
    defaultLang_dd = $("[data-lang='" + defaultLang +"']");
    updateLangTitle(defaultLang_dd.text());
    defaultLang_dd.parent().hide();
    $("[class^='highlight-']").hide();
    $("[class^='section-']").hide();
    $("[class$='nohide']").show();
    $(".highlight-" + defaultLang).show();
    $(".section-" + defaultLang).show();
    $('.highlight-javascript').show();
    $('.highlight-html').show();
    $('.highlight-objc').show();
    $('.highlight-android').show();
    $("[class^='highlight-text']").show();

    $('.lang-change').click(function (e) {
        e.preventDefault();
        var lang = $(this).attr('data-lang');
        $.cookie('language', lang, { expires: 7, path: '/' });
        var langtext = $(this).text();
        updateLangTitle(langtext);
        var parent = $(this).parent();
        parent.siblings().show();
        parent.hide();
        $("[class^='highlight-']").hide();
        $("[class^='section-']").hide();
        $("[class$='nohide']").show();
        $(".highlight-" + lang).show();
        $(".section-" + lang).show();
        $('.highlight-javascript').show();
        $('.highlight-html').show();
        $('.highlight-objc').show();
        $('.highlight-android').show();
        $("[class^='highlight-text']").show();
    });

    scrollToAnchor(window.location.hash);
    $("body").on("click", "a", scrollToAnchor);
    fix_sidebar();
});