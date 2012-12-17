var dockers = {};
dockers.main = {};

dockers.main.init = function() {
  dockers.main.initializeEvents();
  dockers.main.loadOnClickHandlersForMenu();
  dockers.main.transformDomForHeaders();
};

dockers.main.transformDomForHeaders = function () {

};

dockers.main.closeMenus = function() {
  $('.navigation.active').removeClass('active');
};

dockers.main.initializeEvents = function () {
  $('.navigation > *').change(function() {
    var $nav = $(this).parent();
     if($nav.hasClass('active')) {
       dockers.main.closeMenus();
    } else {
       dockers.main.closeMenus();
       $nav.addClass('active');
    }
  });
};

dockers.main.loadOnClickHandlersForMenu = function () {
  $('.navigation > *').click(function() {
    $(this).change();
  });
};

$(dockers.main.init);
