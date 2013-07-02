index = lunr(function () {
    this.field('title', {boost: 10});
    this.field('body');
    this.ref('ref');
});
$(document).ready(function () {
    $("section").each(function () {
        var header = $(this).find(':header').first();
        var title = header.text();
        var link = header.find('a.headerlink').first().attr('href');
        var id = $(this).attr('id');
        var ref = id + "__" + link;
        var body = $(this).find('p').first().text();
        index.add({
            ref: ref,
            title: title,
            body: body
        });
    });
    $('#search').focus(function(){
        if ($('#search-dropdown li').length > 0){
            $('#search-dropdown').show();
        }
    });
    $('#search-dropdown').on('click', 'li', function () {
        $('.search-active').removeClass('search-active');
        var to = $(this).attr('data-scroll-to');
        var search_text = $('#search').val();
        var header = $(to).find(':header').first();
        var body = $(to).find('p').first();
        header.html(highlight_match(header.text(), search_text));
        body.html(highlight_match(body.text(), search_text));
        $.scrollTo(to, 800);
        $('#search-dropdown').hide()
    });
    $('html').click(function () {
        $('#search-dropdown').hide()
    });
    $('#search-section').click(function (event) {
        event.stopPropagation();
    });

    $('#search').keyup(function () {
        var search_text = $(this).val();
        var results = index.search(search_text);
        s_dropdown = $('#search-dropdown');
        s_dropdown.html('');
        $.each(results, function (key, value) {
            var resp_array = value['ref'].split('__');
            var ref = resp_array[0];
            var section = $('#' + ref);
            var link = resp_array[1];
            var header = highlight_match(section.find(':header').first().text(), search_text);
            var body = highlight_match(section.find('p').first().text(), search_text);

            var result_body = "<li class='result_item' data-scroll-to='" +
                link + "'><h4>" +
                header  + "</h4><p>" +
                body + "</p></li>";
            s_dropdown.append(result_body);

        });
        if (results.length > 0) {
            s_dropdown.show();
        }
        else {
            s_dropdown.hide();
        }
    });

    function highlight_match(string_to_check, search_text){
        function highlight(string){
            return "<span class='text-highlight search-active'>" + string + "</span>";
        }
        var min_len = 3
        var already_replaced = {};
        var to_match_split = search_text.split(' ');
        for(var i=0; i<to_match_split.length; i++){
            var word_to_replace = to_match_split[i];
            if (word_to_replace.length > min_len && !(word_to_replace in already_replaced)){
                var regex = new RegExp( '(' + word_to_replace + ')', 'gi' );
                string_to_check = string_to_check.replace(regex, function(match){
                    return highlight(match)
                });
                already_replaced[word_to_replace] = true;
            }
        }
        return string_to_check
    }


});

