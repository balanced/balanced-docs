index = lunr(function () {
    this.field('title', {boost: 10});
    this.field('body');
    this.ref('ref');
});
var $search_dropdown = $('#search-dropdown');
var $light_box = $('#light-box');
var $search_input = $("#search");
function show_search_results() {
    $search_dropdown.show();
    $search_input.addClass('in-search');
    $light_box.show();
}

function hide_search_results() {
    $search_dropdown.hide();
    $search_input.removeClass('in-search');
    $light_box.hide();
}

function endsWith(str, suffix) {
    return str.indexOf(suffix, str.length - suffix.length) !== -1;
}

$(document).ready(function () {
    //ADD OTHER PAGES
    $('body').append("<div id='search_extra' style='display: none'></div>");
    function add_to_search(url) {
        // GRAB THE STUFF
        $.get(url, function (data) {
            var results = $(data).find('section');
            $.each(results, function (key, value) {
                var $value = $(value).find(':header').first().find('a.headerlink');
                if ($value.attr('href').substring(0, 1) == '#') {
                    var current_href = $value.attr('href');
                    $value.attr('href', url + current_href);
                }
            });
            $('#search_extra').append(results);
            create_index();

        });
    }

    //INDEX THE PAGE
    function create_index() {
        $("section").each(function (key, value) {

            var header = $(value).find(':header').first();
            var title = header.text();
            var link = header.find('a.headerlink').first().attr('href');
            var id = $(value).attr('id');
            var ref = id + "{SPLIT_HERE}" + link;
            var body = $(this).find('p').first().text();
            index.add({
                ref: ref,
                title: title,
                body: body
            });
        });
    }

    if (endsWith(window.location.pathname, 'overview.html')) {
        add_to_search('api.html');
    }
    else if (endsWith(window.location.pathname, 'api.html')) {
        add_to_search('overview.html');
    }


    //KEY BINDINGS
    $(document).keydown(function (e) {
        if (e.keyCode == 40) {
            var $result = $('#search-dropdown li.search-selected').first();
            if ($result.next().length != 0) {
                $result.removeClass('search-selected');
                $result.next().addClass('search-selected');
            }
        }
        if (e.keyCode == 38) {
            var $result = $('#search-dropdown li.search-selected').first();
            if ($result.prev().length != 0) {
                $result.removeClass('search-selected');
                $result.prev().addClass('search-selected');
            }
        }
        if (e.keyCode == 13) {
            var $result = $('#search-dropdown li.search-selected').first();
            if ($result.length != 0) {
                visit_result($result);
            }
            $("#search").blur();
            e.preventDefault();
        }
        if (e.keyCode == 191) {
            $('#search').focus();
            e.preventDefault();
        }
    });


    //SHOW LIST OF RESULTS IF SEARCHING AND LIST NOT EMPTY
    $search_input.focus(function () {
        if ($('#search-dropdown li').length > 0) {
            show_search_results();
        }
    });

    function visit_result(item) {
        $('.search-active').removeClass('search-active');
        var to = $(item).attr('data-scroll-to');
        var search_text = $search_input.val();
        var header = $(to).find(':header').first();
        var body = $(to).find('p').first();
        header.html(highlight_match(header.text(), search_text));
        body.html(highlight_match(body.text(), search_text));
        if (to.substring(0, 1) == '#') {
            $.scrollTo(to, 800);
        }
        else {
            window.location = to;
        }
        hide_search_results()
    }

    //CLICK SEARCH RESULT
    $search_dropdown.on('click', 'li', function () {
        visit_result(this)
    });

    //CLOSE SEARCH BOX BY CLICKING ANYWHERE ELSE
    $('html').click(function () {
        hide_search_results();
    });
    $('#search-section').click(function (event) {
        event.stopPropagation();
    });

    //PREFORM THE SEARCH
    $search_input.keyup(function (e) {
        if ([37, 38, 39, 40, 13].indexOf(e.keyCode) != -1) {
            return;
        }
        var search_text = $(this).val();
        var results = index.search(search_text);
        $search_dropdown.html('');
        $.each(results, function (key, value) {
            var resp_array = value['ref'].split('{SPLIT_HERE}');
            var ref = resp_array[0];
            var section = $('#' + ref);
            var link = resp_array[1];
            var header = highlight_match(section.find(':header').first().text(), search_text);
            var body = highlight_match(section.find('p').first().text(), search_text);
            var class_addon = ""
            if (key == 0) {
                class_addon = "search-selected"
            }
            var result_body = "<li class='result_item " + class_addon +
                "' data-scroll-to='" +
                link + "'><h4>" +
                header + "</h4><p>" +
                body + "</p></li>";
            $search_dropdown.append(result_body);

        });
        if (results.length > 0) {
            show_search_results();
        }
        else {
            hide_search_results();
        }
    });
    $('ul').on('mouseover', 'li.result_item',
        function (e) {
            $(this).addClass('search-selected');
            $(this).siblings().removeClass('search-selected');
        }
    );

    //HIGHLIGHT MATCHES
    function highlight_match(string_to_check, search_text) {
        function highlight(string) {
            return "<span class='text-highlight search-active'>" + string + "</span>";
        }
        var min_len = 3;
        var already_replaced = {};
        var to_match_split = search_text.split(' ');
        for (var i = 0; i < to_match_split.length; i++) {
            var word_to_replace = to_match_split[i];
            if (word_to_replace.length >= min_len && !(word_to_replace in already_replaced)) {
                var regex = new RegExp('(' + word_to_replace + ')', 'gi');
                string_to_check = string_to_check.replace(regex, function (match) {
                    return highlight(match)
                });
                already_replaced[word_to_replace] = true;
            }
        }
        return string_to_check
    }


});

