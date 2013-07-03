function update_link(language) {
    var uri = updateQueryStringParameter(window.location.pathname + window.location.search, 'language', language);
    uri = uri + '' + window.location.hash;
    window.history.pushState({}, document.title, uri);
}
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
}

$(document).ready(function () {
    function update_lang_head(text){
        var lang_head = $('#lang-dropdown-head');
        lang_head.html(text + " <b class='caret'></b>")
    }
    var lang = getParameterByName('language', window.location.href);
    lang = (lang.length > 0) ? lang[0] : 'bash';
    update_lang_head($("[data-lang='" + lang +"']").text());
    $("[class^='highlight-']").hide();
    $(".highlight-" + lang).show();
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
        update_link(lang);
        $('[data-spy="scroll"]').each(function () {
            var $spy = $(this).scrollspy('refresh')
        });
    });
    $("li [class^='toctree-']").bind('activate', updateNavigation);
});