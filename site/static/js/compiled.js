/*!
* Bootstrap.js by @fat & @mdo
* Copyright 2012 Twitter, Inc.
* http://www.apache.org/licenses/LICENSE-2.0.txt
*/
!function(e){"use strict";e(function(){e.support.transition=function(){var e=function(){var e=document.createElement("bootstrap"),t={WebkitTransition:"webkitTransitionEnd",MozTransition:"transitionend",OTransition:"oTransitionEnd otransitionend",transition:"transitionend"},n;for(n in t)if(e.style[n]!==undefined)return t[n]}();return e&&{end:e}}()})}(window.jQuery),!function(e){"use strict";var t='[data-dismiss="alert"]',n=function(n){e(n).on("click",t,this.close)};n.prototype.close=function(t){function s(){i.trigger("closed").remove()}var n=e(this),r=n.attr("data-target"),i;r||(r=n.attr("href"),r=r&&r.replace(/.*(?=#[^\s]*$)/,"")),i=e(r),t&&t.preventDefault(),i.length||(i=n.hasClass("alert")?n:n.parent()),i.trigger(t=e.Event("close"));if(t.isDefaultPrevented())return;i.removeClass("in"),e.support.transition&&i.hasClass("fade")?i.on(e.support.transition.end,s):s()};var r=e.fn.alert;e.fn.alert=function(t){return this.each(function(){var r=e(this),i=r.data("alert");i||r.data("alert",i=new n(this)),typeof t=="string"&&i[t].call(r)})},e.fn.alert.Constructor=n,e.fn.alert.noConflict=function(){return e.fn.alert=r,this},e(document).on("click.alert.data-api",t,n.prototype.close)}(window.jQuery),!function(e){"use strict";var t=function(t,n){this.$element=e(t),this.options=e.extend({},e.fn.button.defaults,n)};t.prototype.setState=function(e){var t="disabled",n=this.$element,r=n.data(),i=n.is("input")?"val":"html";e+="Text",r.resetText||n.data("resetText",n[i]()),n[i](r[e]||this.options[e]),setTimeout(function(){e=="loadingText"?n.addClass(t).attr(t,t):n.removeClass(t).removeAttr(t)},0)},t.prototype.toggle=function(){var e=this.$element.closest('[data-toggle="buttons-radio"]');e&&e.find(".active").removeClass("active"),this.$element.toggleClass("active")};var n=e.fn.button;e.fn.button=function(n){return this.each(function(){var r=e(this),i=r.data("button"),s=typeof n=="object"&&n;i||r.data("button",i=new t(this,s)),n=="toggle"?i.toggle():n&&i.setState(n)})},e.fn.button.defaults={loadingText:"loading..."},e.fn.button.Constructor=t,e.fn.button.noConflict=function(){return e.fn.button=n,this},e(document).on("click.button.data-api","[data-toggle^=button]",function(t){var n=e(t.target);n.hasClass("btn")||(n=n.closest(".btn")),n.button("toggle")})}(window.jQuery),!function(e){"use strict";var t=function(t,n){this.$element=e(t),this.$indicators=this.$element.find(".carousel-indicators"),this.options=n,this.options.pause=="hover"&&this.$element.on("mouseenter",e.proxy(this.pause,this)).on("mouseleave",e.proxy(this.cycle,this))};t.prototype={cycle:function(t){return t||(this.paused=!1),this.interval&&clearInterval(this.interval),this.options.interval&&!this.paused&&(this.interval=setInterval(e.proxy(this.next,this),this.options.interval)),this},getActiveIndex:function(){return this.$active=this.$element.find(".item.active"),this.$items=this.$active.parent().children(),this.$items.index(this.$active)},to:function(t){var n=this.getActiveIndex(),r=this;if(t>this.$items.length-1||t<0)return;return this.sliding?this.$element.one("slid",function(){r.to(t)}):n==t?this.pause().cycle():this.slide(t>n?"next":"prev",e(this.$items[t]))},pause:function(t){return t||(this.paused=!0),this.$element.find(".next, .prev").length&&e.support.transition.end&&(this.$element.trigger(e.support.transition.end),this.cycle(!0)),clearInterval(this.interval),this.interval=null,this},next:function(){if(this.sliding)return;return this.slide("next")},prev:function(){if(this.sliding)return;return this.slide("prev")},slide:function(t,n){var r=this.$element.find(".item.active"),i=n||r[t](),s=this.interval,o=t=="next"?"left":"right",u=t=="next"?"first":"last",a=this,f;this.sliding=!0,s&&this.pause(),i=i.length?i:this.$element.find(".item")[u](),f=e.Event("slide",{relatedTarget:i[0],direction:o});if(i.hasClass("active"))return;this.$indicators.length&&(this.$indicators.find(".active").removeClass("active"),this.$element.one("slid",function(){var t=e(a.$indicators.children()[a.getActiveIndex()]);t&&t.addClass("active")}));if(e.support.transition&&this.$element.hasClass("slide")){this.$element.trigger(f);if(f.isDefaultPrevented())return;i.addClass(t),i[0].offsetWidth,r.addClass(o),i.addClass(o),this.$element.one(e.support.transition.end,function(){i.removeClass([t,o].join(" ")).addClass("active"),r.removeClass(["active",o].join(" ")),a.sliding=!1,setTimeout(function(){a.$element.trigger("slid")},0)})}else{this.$element.trigger(f);if(f.isDefaultPrevented())return;r.removeClass("active"),i.addClass("active"),this.sliding=!1,this.$element.trigger("slid")}return s&&this.cycle(),this}};var n=e.fn.carousel;e.fn.carousel=function(n){return this.each(function(){var r=e(this),i=r.data("carousel"),s=e.extend({},e.fn.carousel.defaults,typeof n=="object"&&n),o=typeof n=="string"?n:s.slide;i||r.data("carousel",i=new t(this,s)),typeof n=="number"?i.to(n):o?i[o]():s.interval&&i.pause().cycle()})},e.fn.carousel.defaults={interval:5e3,pause:"hover"},e.fn.carousel.Constructor=t,e.fn.carousel.noConflict=function(){return e.fn.carousel=n,this},e(document).on("click.carousel.data-api","[data-slide], [data-slide-to]",function(t){var n=e(this),r,i=e(n.attr("data-target")||(r=n.attr("href"))&&r.replace(/.*(?=#[^\s]+$)/,"")),s=e.extend({},i.data(),n.data()),o;i.carousel(s),(o=n.attr("data-slide-to"))&&i.data("carousel").pause().to(o).cycle(),t.preventDefault()})}(window.jQuery),!function(e){"use strict";var t=function(t,n){this.$element=e(t),this.options=e.extend({},e.fn.collapse.defaults,n),this.options.parent&&(this.$parent=e(this.options.parent)),this.options.toggle&&this.toggle()};t.prototype={constructor:t,dimension:function(){var e=this.$element.hasClass("width");return e?"width":"height"},show:function(){var t,n,r,i;if(this.transitioning||this.$element.hasClass("in"))return;t=this.dimension(),n=e.camelCase(["scroll",t].join("-")),r=this.$parent&&this.$parent.find("> .accordion-group > .in");if(r&&r.length){i=r.data("collapse");if(i&&i.transitioning)return;r.collapse("hide"),i||r.data("collapse",null)}this.$element[t](0),this.transition("addClass",e.Event("show"),"shown"),e.support.transition&&this.$element[t](this.$element[0][n])},hide:function(){var t;if(this.transitioning||!this.$element.hasClass("in"))return;t=this.dimension(),this.reset(this.$element[t]()),this.transition("removeClass",e.Event("hide"),"hidden"),this.$element[t](0)},reset:function(e){var t=this.dimension();return this.$element.removeClass("collapse")[t](e||"auto")[0].offsetWidth,this.$element[e!==null?"addClass":"removeClass"]("collapse"),this},transition:function(t,n,r){var i=this,s=function(){n.type=="show"&&i.reset(),i.transitioning=0,i.$element.trigger(r)};this.$element.trigger(n);if(n.isDefaultPrevented())return;this.transitioning=1,this.$element[t]("in"),e.support.transition&&this.$element.hasClass("collapse")?this.$element.one(e.support.transition.end,s):s()},toggle:function(){this[this.$element.hasClass("in")?"hide":"show"]()}};var n=e.fn.collapse;e.fn.collapse=function(n){return this.each(function(){var r=e(this),i=r.data("collapse"),s=e.extend({},e.fn.collapse.defaults,r.data(),typeof n=="object"&&n);i||r.data("collapse",i=new t(this,s)),typeof n=="string"&&i[n]()})},e.fn.collapse.defaults={toggle:!0},e.fn.collapse.Constructor=t,e.fn.collapse.noConflict=function(){return e.fn.collapse=n,this},e(document).on("click.collapse.data-api","[data-toggle=collapse]",function(t){var n=e(this),r,i=n.attr("data-target")||t.preventDefault()||(r=n.attr("href"))&&r.replace(/.*(?=#[^\s]+$)/,""),s=e(i).data("collapse")?"toggle":n.data();n[e(i).hasClass("in")?"addClass":"removeClass"]("collapsed"),e(i).collapse(s)})}(window.jQuery),!function(e){"use strict";function r(){e(".dropdown-backdrop").remove(),e(t).each(function(){i(e(this)).removeClass("open")})}function i(t){var n=t.attr("data-target"),r;n||(n=t.attr("href"),n=n&&/#/.test(n)&&n.replace(/.*(?=#[^\s]*$)/,"")),r=n&&e(n);if(!r||!r.length)r=t.parent();return r}var t="[data-toggle=dropdown]",n=function(t){var n=e(t).on("click.dropdown.data-api",this.toggle);e("html").on("click.dropdown.data-api",function(){n.parent().removeClass("open")})};n.prototype={constructor:n,toggle:function(t){var n=e(this),s,o;if(n.is(".disabled, :disabled"))return;return s=i(n),o=s.hasClass("open"),r(),o||("ontouchstart"in document.documentElement&&e('<div class="dropdown-backdrop"/>').insertBefore(e(this)).on("click",r),s.toggleClass("open")),n.focus(),!1},keydown:function(n){var r,s,o,u,a,f;if(!/(38|40|27)/.test(n.keyCode))return;r=e(this),n.preventDefault(),n.stopPropagation();if(r.is(".disabled, :disabled"))return;u=i(r),a=u.hasClass("open");if(!a||a&&n.keyCode==27)return n.which==27&&u.find(t).focus(),r.click();s=e("[role=menu] li:not(.divider):visible a",u);if(!s.length)return;f=s.index(s.filter(":focus")),n.keyCode==38&&f>0&&f--,n.keyCode==40&&f<s.length-1&&f++,~f||(f=0),s.eq(f).focus()}};var s=e.fn.dropdown;e.fn.dropdown=function(t){return this.each(function(){var r=e(this),i=r.data("dropdown");i||r.data("dropdown",i=new n(this)),typeof t=="string"&&i[t].call(r)})},e.fn.dropdown.Constructor=n,e.fn.dropdown.noConflict=function(){return e.fn.dropdown=s,this},e(document).on("click.dropdown.data-api",r).on("click.dropdown.data-api",".dropdown form",function(e){e.stopPropagation()}).on("click.dropdown.data-api",t,n.prototype.toggle).on("keydown.dropdown.data-api",t+", [role=menu]",n.prototype.keydown)}(window.jQuery),!function(e){"use strict";var t=function(t,n){this.options=n,this.$element=e(t).delegate('[data-dismiss="modal"]',"click.dismiss.modal",e.proxy(this.hide,this)),this.options.remote&&this.$element.find(".modal-body").load(this.options.remote)};t.prototype={constructor:t,toggle:function(){return this[this.isShown?"hide":"show"]()},show:function(){var t=this,n=e.Event("show");this.$element.trigger(n);if(this.isShown||n.isDefaultPrevented())return;this.isShown=!0,this.escape(),this.backdrop(function(){var n=e.support.transition&&t.$element.hasClass("fade");t.$element.parent().length||t.$element.appendTo(document.body),t.$element.show(),n&&t.$element[0].offsetWidth,t.$element.addClass("in").attr("aria-hidden",!1),t.enforceFocus(),n?t.$element.one(e.support.transition.end,function(){t.$element.focus().trigger("shown")}):t.$element.focus().trigger("shown")})},hide:function(t){t&&t.preventDefault();var n=this;t=e.Event("hide"),this.$element.trigger(t);if(!this.isShown||t.isDefaultPrevented())return;this.isShown=!1,this.escape(),e(document).off("focusin.modal"),this.$element.removeClass("in").attr("aria-hidden",!0),e.support.transition&&this.$element.hasClass("fade")?this.hideWithTransition():this.hideModal()},enforceFocus:function(){var t=this;e(document).on("focusin.modal",function(e){t.$element[0]!==e.target&&!t.$element.has(e.target).length&&t.$element.focus()})},escape:function(){var e=this;this.isShown&&this.options.keyboard?this.$element.on("keyup.dismiss.modal",function(t){t.which==27&&e.hide()}):this.isShown||this.$element.off("keyup.dismiss.modal")},hideWithTransition:function(){var t=this,n=setTimeout(function(){t.$element.off(e.support.transition.end),t.hideModal()},500);this.$element.one(e.support.transition.end,function(){clearTimeout(n),t.hideModal()})},hideModal:function(){var e=this;this.$element.hide(),this.backdrop(function(){e.removeBackdrop(),e.$element.trigger("hidden")})},removeBackdrop:function(){this.$backdrop&&this.$backdrop.remove(),this.$backdrop=null},backdrop:function(t){var n=this,r=this.$element.hasClass("fade")?"fade":"";if(this.isShown&&this.options.backdrop){var i=e.support.transition&&r;this.$backdrop=e('<div class="modal-backdrop '+r+'" />').appendTo(document.body),this.$backdrop.click(this.options.backdrop=="static"?e.proxy(this.$element[0].focus,this.$element[0]):e.proxy(this.hide,this)),i&&this.$backdrop[0].offsetWidth,this.$backdrop.addClass("in");if(!t)return;i?this.$backdrop.one(e.support.transition.end,t):t()}else!this.isShown&&this.$backdrop?(this.$backdrop.removeClass("in"),e.support.transition&&this.$element.hasClass("fade")?this.$backdrop.one(e.support.transition.end,t):t()):t&&t()}};var n=e.fn.modal;e.fn.modal=function(n){return this.each(function(){var r=e(this),i=r.data("modal"),s=e.extend({},e.fn.modal.defaults,r.data(),typeof n=="object"&&n);i||r.data("modal",i=new t(this,s)),typeof n=="string"?i[n]():s.show&&i.show()})},e.fn.modal.defaults={backdrop:!0,keyboard:!0,show:!0},e.fn.modal.Constructor=t,e.fn.modal.noConflict=function(){return e.fn.modal=n,this},e(document).on("click.modal.data-api",'[data-toggle="modal"]',function(t){var n=e(this),r=n.attr("href"),i=e(n.attr("data-target")||r&&r.replace(/.*(?=#[^\s]+$)/,"")),s=i.data("modal")?"toggle":e.extend({remote:!/#/.test(r)&&r},i.data(),n.data());t.preventDefault(),i.modal(s).one("hide",function(){n.focus()})})}(window.jQuery),!function(e){"use strict";var t=function(e,t){this.init("tooltip",e,t)};t.prototype={constructor:t,init:function(t,n,r){var i,s,o,u,a;this.type=t,this.$element=e(n),this.options=this.getOptions(r),this.enabled=!0,o=this.options.trigger.split(" ");for(a=o.length;a--;)u=o[a],u=="click"?this.$element.on("click."+this.type,this.options.selector,e.proxy(this.toggle,this)):u!="manual"&&(i=u=="hover"?"mouseenter":"focus",s=u=="hover"?"mouseleave":"blur",this.$element.on(i+"."+this.type,this.options.selector,e.proxy(this.enter,this)),this.$element.on(s+"."+this.type,this.options.selector,e.proxy(this.leave,this)));this.options.selector?this._options=e.extend({},this.options,{trigger:"manual",selector:""}):this.fixTitle()},getOptions:function(t){return t=e.extend({},e.fn[this.type].defaults,this.$element.data(),t),t.delay&&typeof t.delay=="number"&&(t.delay={show:t.delay,hide:t.delay}),t},enter:function(t){var n=e.fn[this.type].defaults,r={},i;this._options&&e.each(this._options,function(e,t){n[e]!=t&&(r[e]=t)},this),i=e(t.currentTarget)[this.type](r).data(this.type);if(!i.options.delay||!i.options.delay.show)return i.show();clearTimeout(this.timeout),i.hoverState="in",this.timeout=setTimeout(function(){i.hoverState=="in"&&i.show()},i.options.delay.show)},leave:function(t){var n=e(t.currentTarget)[this.type](this._options).data(this.type);this.timeout&&clearTimeout(this.timeout);if(!n.options.delay||!n.options.delay.hide)return n.hide();n.hoverState="out",this.timeout=setTimeout(function(){n.hoverState=="out"&&n.hide()},n.options.delay.hide)},show:function(){var t,n,r,i,s,o,u=e.Event("show");if(this.hasContent()&&this.enabled){this.$element.trigger(u);if(u.isDefaultPrevented())return;t=this.tip(),this.setContent(),this.options.animation&&t.addClass("fade"),s=typeof this.options.placement=="function"?this.options.placement.call(this,t[0],this.$element[0]):this.options.placement,t.detach().css({top:0,left:0,display:"block"}),this.options.container?t.appendTo(this.options.container):t.insertAfter(this.$element),n=this.getPosition(),r=t[0].offsetWidth,i=t[0].offsetHeight;switch(s){case"bottom":o={top:n.top+n.height,left:n.left+n.width/2-r/2};break;case"top":o={top:n.top-i,left:n.left+n.width/2-r/2};break;case"left":o={top:n.top+n.height/2-i/2,left:n.left-r};break;case"right":o={top:n.top+n.height/2-i/2,left:n.left+n.width}}this.applyPlacement(o,s),this.$element.trigger("shown")}},applyPlacement:function(e,t){var n=this.tip(),r=n[0].offsetWidth,i=n[0].offsetHeight,s,o,u,a;n.offset(e).addClass(t).addClass("in"),s=n[0].offsetWidth,o=n[0].offsetHeight,t=="top"&&o!=i&&(e.top=e.top+i-o,a=!0),t=="bottom"||t=="top"?(u=0,e.left<0&&(u=e.left*-2,e.left=0,n.offset(e),s=n[0].offsetWidth,o=n[0].offsetHeight),this.replaceArrow(u-r+s,s,"left")):this.replaceArrow(o-i,o,"top"),a&&n.offset(e)},replaceArrow:function(e,t,n){this.arrow().css(n,e?50*(1-e/t)+"%":"")},setContent:function(){var e=this.tip(),t=this.getTitle();e.find(".tooltip-inner")[this.options.html?"html":"text"](t),e.removeClass("fade in top bottom left right")},hide:function(){function i(){var t=setTimeout(function(){n.off(e.support.transition.end).detach()},500);n.one(e.support.transition.end,function(){clearTimeout(t),n.detach()})}var t=this,n=this.tip(),r=e.Event("hide");this.$element.trigger(r);if(r.isDefaultPrevented())return;return n.removeClass("in"),e.support.transition&&this.$tip.hasClass("fade")?i():n.detach(),this.$element.trigger("hidden"),this},fixTitle:function(){var e=this.$element;(e.attr("title")||typeof e.attr("data-original-title")!="string")&&e.attr("data-original-title",e.attr("title")||"").attr("title","")},hasContent:function(){return this.getTitle()},getPosition:function(){var t=this.$element[0];return e.extend({},typeof t.getBoundingClientRect=="function"?t.getBoundingClientRect():{width:t.offsetWidth,height:t.offsetHeight},this.$element.offset())},getTitle:function(){var e,t=this.$element,n=this.options;return e=t.attr("data-original-title")||(typeof n.title=="function"?n.title.call(t[0]):n.title),e},tip:function(){return this.$tip=this.$tip||e(this.options.template)},arrow:function(){return this.$arrow=this.$arrow||this.tip().find(".tooltip-arrow")},validate:function(){this.$element[0].parentNode||(this.hide(),this.$element=null,this.options=null)},enable:function(){this.enabled=!0},disable:function(){this.enabled=!1},toggleEnabled:function(){this.enabled=!this.enabled},toggle:function(t){var n=t?e(t.currentTarget)[this.type](this._options).data(this.type):this;n.tip().hasClass("in")?n.hide():n.show()},destroy:function(){this.hide().$element.off("."+this.type).removeData(this.type)}};var n=e.fn.tooltip;e.fn.tooltip=function(n){return this.each(function(){var r=e(this),i=r.data("tooltip"),s=typeof n=="object"&&n;i||r.data("tooltip",i=new t(this,s)),typeof n=="string"&&i[n]()})},e.fn.tooltip.Constructor=t,e.fn.tooltip.defaults={animation:!0,placement:"top",selector:!1,template:'<div class="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>',trigger:"hover focus",title:"",delay:0,html:!1,container:!1},e.fn.tooltip.noConflict=function(){return e.fn.tooltip=n,this}}(window.jQuery),!function(e){"use strict";var t=function(e,t){this.init("popover",e,t)};t.prototype=e.extend({},e.fn.tooltip.Constructor.prototype,{constructor:t,setContent:function(){var e=this.tip(),t=this.getTitle(),n=this.getContent();e.find(".popover-title")[this.options.html?"html":"text"](t),e.find(".popover-content")[this.options.html?"html":"text"](n),e.removeClass("fade top bottom left right in")},hasContent:function(){return this.getTitle()||this.getContent()},getContent:function(){var e,t=this.$element,n=this.options;return e=(typeof n.content=="function"?n.content.call(t[0]):n.content)||t.attr("data-content"),e},tip:function(){return this.$tip||(this.$tip=e(this.options.template)),this.$tip},destroy:function(){this.hide().$element.off("."+this.type).removeData(this.type)}});var n=e.fn.popover;e.fn.popover=function(n){return this.each(function(){var r=e(this),i=r.data("popover"),s=typeof n=="object"&&n;i||r.data("popover",i=new t(this,s)),typeof n=="string"&&i[n]()})},e.fn.popover.Constructor=t,e.fn.popover.defaults=e.extend({},e.fn.tooltip.defaults,{placement:"right",trigger:"click",content:"",template:'<div class="popover"><div class="arrow"></div><h3 class="popover-title"></h3><div class="popover-content"></div></div>'}),e.fn.popover.noConflict=function(){return e.fn.popover=n,this}}(window.jQuery),!function(e){"use strict";function t(t,n){var r=e.proxy(this.process,this),i=e(t).is("body")?e(window):e(t),s;this.options=e.extend({},e.fn.scrollspy.defaults,n),this.$scrollElement=i.on("scroll.scroll-spy.data-api",r),this.selector=(this.options.target||(s=e(t).attr("href"))&&s.replace(/.*(?=#[^\s]+$)/,"")||"")+" .nav li > a",this.$body=e("body"),this.refresh(),this.process()}t.prototype={constructor:t,refresh:function(){var t=this,n;this.offsets=e([]),this.targets=e([]),n=this.$body.find(this.selector).map(function(){var n=e(this),r=n.data("target")||n.attr("href"),i=/^#\w/.test(r)&&e(r);return i&&i.length&&[[i.position().top+(!e.isWindow(t.$scrollElement.get(0))&&t.$scrollElement.scrollTop()),r]]||null}).sort(function(e,t){return e[0]-t[0]}).each(function(){t.offsets.push(this[0]),t.targets.push(this[1])})},process:function(){var e=this.$scrollElement.scrollTop()+this.options.offset,t=this.$scrollElement[0].scrollHeight||this.$body[0].scrollHeight,n=t-this.$scrollElement.height(),r=this.offsets,i=this.targets,s=this.activeTarget,o;if(e>=n)return s!=(o=i.last()[0])&&this.activate(o);for(o=r.length;o--;)s!=i[o]&&e>=r[o]&&(!r[o+1]||e<=r[o+1])&&this.activate(i[o])},activate:function(t){var n,r;this.activeTarget=t,e(this.selector).parent(".active").removeClass("active"),r=this.selector+'[data-target="'+t+'"],'+this.selector+'[href="'+t+'"]',n=e(r).parent("li").addClass("active"),n.parent(".dropdown-menu").length&&(n=n.closest("li.dropdown").addClass("active")),n.trigger("activate")}};var n=e.fn.scrollspy;e.fn.scrollspy=function(n){return this.each(function(){var r=e(this),i=r.data("scrollspy"),s=typeof n=="object"&&n;i||r.data("scrollspy",i=new t(this,s)),typeof n=="string"&&i[n]()})},e.fn.scrollspy.Constructor=t,e.fn.scrollspy.defaults={offset:10},e.fn.scrollspy.noConflict=function(){return e.fn.scrollspy=n,this},e(window).on("load",function(){e('[data-spy="scroll"]').each(function(){var t=e(this);t.scrollspy(t.data())})})}(window.jQuery),!function(e){"use strict";var t=function(t){this.element=e(t)};t.prototype={constructor:t,show:function(){var t=this.element,n=t.closest("ul:not(.dropdown-menu)"),r=t.attr("data-target"),i,s,o;r||(r=t.attr("href"),r=r&&r.replace(/.*(?=#[^\s]*$)/,""));if(t.parent("li").hasClass("active"))return;i=n.find(".active:last a")[0],o=e.Event("show",{relatedTarget:i}),t.trigger(o);if(o.isDefaultPrevented())return;s=e(r),this.activate(t.parent("li"),n),this.activate(s,s.parent(),function(){t.trigger({type:"shown",relatedTarget:i})})},activate:function(t,n,r){function o(){i.removeClass("active").find("> .dropdown-menu > .active").removeClass("active"),t.addClass("active"),s?(t[0].offsetWidth,t.addClass("in")):t.removeClass("fade"),t.parent(".dropdown-menu")&&t.closest("li.dropdown").addClass("active"),r&&r()}var i=n.find("> .active"),s=r&&e.support.transition&&i.hasClass("fade");s?i.one(e.support.transition.end,o):o(),i.removeClass("in")}};var n=e.fn.tab;e.fn.tab=function(n){return this.each(function(){var r=e(this),i=r.data("tab");i||r.data("tab",i=new t(this)),typeof n=="string"&&i[n]()})},e.fn.tab.Constructor=t,e.fn.tab.noConflict=function(){return e.fn.tab=n,this},e(document).on("click.tab.data-api",'[data-toggle="tab"], [data-toggle="pill"]',function(t){t.preventDefault(),e(this).tab("show")})}(window.jQuery),!function(e){"use strict";var t=function(t,n){this.$element=e(t),this.options=e.extend({},e.fn.typeahead.defaults,n),this.matcher=this.options.matcher||this.matcher,this.sorter=this.options.sorter||this.sorter,this.highlighter=this.options.highlighter||this.highlighter,this.updater=this.options.updater||this.updater,this.source=this.options.source,this.$menu=e(this.options.menu),this.shown=!1,this.listen()};t.prototype={constructor:t,select:function(){var e=this.$menu.find(".active").attr("data-value");return this.$element.val(this.updater(e)).change(),this.hide()},updater:function(e){return e},show:function(){var t=e.extend({},this.$element.position(),{height:this.$element[0].offsetHeight});return this.$menu.insertAfter(this.$element).css({top:t.top+t.height,left:t.left}).show(),this.shown=!0,this},hide:function(){return this.$menu.hide(),this.shown=!1,this},lookup:function(t){var n;return this.query=this.$element.val(),!this.query||this.query.length<this.options.minLength?this.shown?this.hide():this:(n=e.isFunction(this.source)?this.source(this.query,e.proxy(this.process,this)):this.source,n?this.process(n):this)},process:function(t){var n=this;return t=e.grep(t,function(e){return n.matcher(e)}),t=this.sorter(t),t.length?this.render(t.slice(0,this.options.items)).show():this.shown?this.hide():this},matcher:function(e){return~e.toLowerCase().indexOf(this.query.toLowerCase())},sorter:function(e){var t=[],n=[],r=[],i;while(i=e.shift())i.toLowerCase().indexOf(this.query.toLowerCase())?~i.indexOf(this.query)?n.push(i):r.push(i):t.push(i);return t.concat(n,r)},highlighter:function(e){var t=this.query.replace(/[\-\[\]{}()*+?.,\\\^$|#\s]/g,"\\$&");return e.replace(new RegExp("("+t+")","ig"),function(e,t){return"<strong>"+t+"</strong>"})},render:function(t){var n=this;return t=e(t).map(function(t,r){return t=e(n.options.item).attr("data-value",r),t.find("a").html(n.highlighter(r)),t[0]}),t.first().addClass("active"),this.$menu.html(t),this},next:function(t){var n=this.$menu.find(".active").removeClass("active"),r=n.next();r.length||(r=e(this.$menu.find("li")[0])),r.addClass("active")},prev:function(e){var t=this.$menu.find(".active").removeClass("active"),n=t.prev();n.length||(n=this.$menu.find("li").last()),n.addClass("active")},listen:function(){this.$element.on("focus",e.proxy(this.focus,this)).on("blur",e.proxy(this.blur,this)).on("keypress",e.proxy(this.keypress,this)).on("keyup",e.proxy(this.keyup,this)),this.eventSupported("keydown")&&this.$element.on("keydown",e.proxy(this.keydown,this)),this.$menu.on("click",e.proxy(this.click,this)).on("mouseenter","li",e.proxy(this.mouseenter,this)).on("mouseleave","li",e.proxy(this.mouseleave,this))},eventSupported:function(e){var t=e in this.$element;return t||(this.$element.setAttribute(e,"return;"),t=typeof this.$element[e]=="function"),t},move:function(e){if(!this.shown)return;switch(e.keyCode){case 9:case 13:case 27:e.preventDefault();break;case 38:e.preventDefault(),this.prev();break;case 40:e.preventDefault(),this.next()}e.stopPropagation()},keydown:function(t){this.suppressKeyPressRepeat=~e.inArray(t.keyCode,[40,38,9,13,27]),this.move(t)},keypress:function(e){if(this.suppressKeyPressRepeat)return;this.move(e)},keyup:function(e){switch(e.keyCode){case 40:case 38:case 16:case 17:case 18:break;case 9:case 13:if(!this.shown)return;this.select();break;case 27:if(!this.shown)return;this.hide();break;default:this.lookup()}e.stopPropagation(),e.preventDefault()},focus:function(e){this.focused=!0},blur:function(e){this.focused=!1,!this.mousedover&&this.shown&&this.hide()},click:function(e){e.stopPropagation(),e.preventDefault(),this.select(),this.$element.focus()},mouseenter:function(t){this.mousedover=!0,this.$menu.find(".active").removeClass("active"),e(t.currentTarget).addClass("active")},mouseleave:function(e){this.mousedover=!1,!this.focused&&this.shown&&this.hide()}};var n=e.fn.typeahead;e.fn.typeahead=function(n){return this.each(function(){var r=e(this),i=r.data("typeahead"),s=typeof n=="object"&&n;i||r.data("typeahead",i=new t(this,s)),typeof n=="string"&&i[n]()})},e.fn.typeahead.defaults={source:[],items:8,menu:'<ul class="typeahead dropdown-menu"></ul>',item:'<li><a href="#"></a></li>',minLength:1},e.fn.typeahead.Constructor=t,e.fn.typeahead.noConflict=function(){return e.fn.typeahead=n,this},e(document).on("focus.typeahead.data-api",'[data-provide="typeahead"]',function(t){var n=e(this);if(n.data("typeahead"))return;n.typeahead(n.data())})}(window.jQuery),!function(e){"use strict";var t=function(t,n){this.options=e.extend({},e.fn.affix.defaults,n),this.$window=e(window).on("scroll.affix.data-api",e.proxy(this.checkPosition,this)).on("click.affix.data-api",e.proxy(function(){setTimeout(e.proxy(this.checkPosition,this),1)},this)),this.$element=e(t),this.checkPosition()};t.prototype.checkPosition=function(){if(!this.$element.is(":visible"))return;var t=e(document).height(),n=this.$window.scrollTop(),r=this.$element.offset(),i=this.options.offset,s=i.bottom,o=i.top,u="affix affix-top affix-bottom",a;typeof i!="object"&&(s=o=i),typeof o=="function"&&(o=i.top()),typeof s=="function"&&(s=i.bottom()),a=this.unpin!=null&&n+this.unpin<=r.top?!1:s!=null&&r.top+this.$element.height()>=t-s?"bottom":o!=null&&n<=o?"top":!1;if(this.affixed===a)return;this.affixed=a,this.unpin=a=="bottom"?r.top-n:null,this.$element.removeClass(u).addClass("affix"+(a?"-"+a:""))};var n=e.fn.affix;e.fn.affix=function(n){return this.each(function(){var r=e(this),i=r.data("affix"),s=typeof n=="object"&&n;i||r.data("affix",i=new t(this,s)),typeof n=="string"&&i[n]()})},e.fn.affix.Constructor=t,e.fn.affix.defaults={offset:0},e.fn.affix.noConflict=function(){return e.fn.affix=n,this},e(window).on("load",function(){e('[data-spy="affix"]').each(function(){var t=e(this),n=t.data();n.offset=n.offset||{},n.offsetBottom&&(n.offset.bottom=n.offsetBottom),n.offsetTop&&(n.offset.top=n.offsetTop),t.affix(n)})})}(window.jQuery);
/**
 * lunr - http://lunrjs.com - A bit like Solr, but much smaller and not as bright - 0.4.0
 * Copyright (C) 2013 Oliver Nightingale
 * MIT Licensed
 * @license
 */
var lunr=function(t){var e=new lunr.Index;return e.pipeline.add(lunr.stopWordFilter,lunr.stemmer),t&&t.call(e,e),e};lunr.version="0.4.0","undefined"!=typeof module&&(module.exports=lunr),lunr.utils={},lunr.utils.warn=function(t){return function(e){t.console&&console.warn&&console.warn(e)}}(this),lunr.utils.zeroFillArray=function(){var t=[0];return function(e){for(;e>t.length;)t=t.concat(t);return t.slice(0,e)}}(),lunr.EventEmitter=function(){this.events={}},lunr.EventEmitter.prototype.addListener=function(){var t=Array.prototype.slice.call(arguments),e=t.pop(),n=t;if("function"!=typeof e)throw new TypeError("last argument must be a function");n.forEach(function(t){this.hasHandler(t)||(this.events[t]=[]),this.events[t].push(e)},this)},lunr.EventEmitter.prototype.removeListener=function(t,e){if(this.hasHandler(t)){var n=this.events[t].indexOf(e);this.events[t].splice(n,1),this.events[t].length||delete this.events[t]}},lunr.EventEmitter.prototype.emit=function(t){if(this.hasHandler(t)){var e=Array.prototype.slice.call(arguments,1);this.events[t].forEach(function(t){t.apply(void 0,e)})}},lunr.EventEmitter.prototype.hasHandler=function(t){return t in this.events},lunr.tokenizer=function(t){if(!t)return[];if(Array.isArray(t))return t;for(var t=t.replace(/^\s+/,""),e=t.length-1;e>=0;e--)if(/\S/.test(t.charAt(e))){t=t.substring(0,e+1);break}return t.split(/\s+/).map(function(t){return t.replace(/^\W+/,"").replace(/\W+$/,"").toLowerCase()})},lunr.Pipeline=function(){this._stack=[]},lunr.Pipeline.registeredFunctions={},lunr.Pipeline.registerFunction=function(t,e){e in this.registeredFunctions&&lunr.utils.warn("Overwriting existing registered function: "+e),t.label=e,lunr.Pipeline.registeredFunctions[t.label]=t},lunr.Pipeline.warnIfFunctionNotRegistered=function(t){var e=t.label&&t.label in this.registeredFunctions;e||lunr.utils.warn("Function is not registered with pipeline. This may cause problems when serialising the index.\n",t)},lunr.Pipeline.load=function(t){var e=new lunr.Pipeline;return t.forEach(function(t){var n=lunr.Pipeline.registeredFunctions[t];if(!n)throw Error("Cannot load un-registered function: "+t);e.add(n)}),e},lunr.Pipeline.prototype.add=function(){var t=Array.prototype.slice.call(arguments);t.forEach(function(t){lunr.Pipeline.warnIfFunctionNotRegistered(t),this._stack.push(t)},this)},lunr.Pipeline.prototype.after=function(t,e){lunr.Pipeline.warnIfFunctionNotRegistered(e);var n=this._stack.indexOf(t)+1;this._stack.splice(n,0,e)},lunr.Pipeline.prototype.before=function(t,e){lunr.Pipeline.warnIfFunctionNotRegistered(e);var n=this._stack.indexOf(t);this._stack.splice(n,0,e)},lunr.Pipeline.prototype.remove=function(t){var e=this._stack.indexOf(t);this._stack.splice(e,1)},lunr.Pipeline.prototype.run=function(t){for(var e=[],n=t.length,r=this._stack.length,i=0;n>i;i++){for(var o=t[i],s=0;r>s&&(o=this._stack[s](o,i,t),void 0!==o);s++);void 0!==o&&e.push(o)}return e},lunr.Pipeline.prototype.toJSON=function(){return this._stack.map(function(t){return lunr.Pipeline.warnIfFunctionNotRegistered(t),t.label})},lunr.Vector=function(t){this.elements=t},lunr.Vector.prototype.magnitude=function(){if(this._magnitude)return this._magnitude;for(var t,e=0,n=this.elements,r=n.length,i=0;r>i;i++)t=n[i],e+=t*t;return this._magnitude=Math.sqrt(e)},lunr.Vector.prototype.dot=function(t){for(var e=this.elements,n=t.elements,r=e.length,i=0,o=0;r>o;o++)i+=e[o]*n[o];return i},lunr.Vector.prototype.similarity=function(t){return this.dot(t)/(this.magnitude()*t.magnitude())},lunr.Vector.prototype.toArray=function(){return this.elements},lunr.SortedSet=function(){this.length=0,this.elements=[]},lunr.SortedSet.load=function(t){var e=new this;return e.elements=t,e.length=t.length,e},lunr.SortedSet.prototype.add=function(){Array.prototype.slice.call(arguments).forEach(function(t){~this.indexOf(t)||this.elements.splice(this.locationFor(t),0,t)},this),this.length=this.elements.length},lunr.SortedSet.prototype.toArray=function(){return this.elements.slice()},lunr.SortedSet.prototype.map=function(t,e){return this.elements.map(t,e)},lunr.SortedSet.prototype.forEach=function(t,e){return this.elements.forEach(t,e)},lunr.SortedSet.prototype.indexOf=function(t,e,n){var e=e||0,n=n||this.elements.length,r=n-e,i=e+Math.floor(r/2),o=this.elements[i];return 1>=r?o===t?i:-1:t>o?this.indexOf(t,i,n):o>t?this.indexOf(t,e,i):o===t?i:void 0},lunr.SortedSet.prototype.locationFor=function(t,e,n){var e=e||0,n=n||this.elements.length,r=n-e,i=e+Math.floor(r/2),o=this.elements[i];if(1>=r){if(o>t)return i;if(t>o)return i+1}return t>o?this.locationFor(t,i,n):o>t?this.locationFor(t,e,i):void 0},lunr.SortedSet.prototype.intersect=function(t){for(var e=new lunr.SortedSet,n=0,r=0,i=this.length,o=t.length,s=this.elements,l=t.elements;;){if(n>i-1||r>o-1)break;s[n]!==l[r]?s[n]<l[r]?n++:s[n]>l[r]&&r++:(e.add(s[n]),n++,r++)}return e},lunr.SortedSet.prototype.clone=function(){var t=new lunr.SortedSet;return t.elements=this.toArray(),t.length=t.elements.length,t},lunr.SortedSet.prototype.union=function(t){var e,n,r;return this.length>=t.length?(e=this,n=t):(e=t,n=this),r=e.clone(),r.add.apply(r,n.toArray()),r},lunr.SortedSet.prototype.toJSON=function(){return this.toArray()},lunr.Index=function(){this._fields=[],this._ref="id",this.pipeline=new lunr.Pipeline,this.documentStore=new lunr.Store,this.tokenStore=new lunr.TokenStore,this.corpusTokens=new lunr.SortedSet,this.eventEmitter=new lunr.EventEmitter,this._idfCache={},this.on("add","remove","update",function(){this._idfCache={}}.bind(this))},lunr.Index.prototype.on=function(){var t=Array.prototype.slice.call(arguments);return this.eventEmitter.addListener.apply(this.eventEmitter,t)},lunr.Index.prototype.off=function(t,e){return this.eventEmitter.removeListener(t,e)},lunr.Index.load=function(t){t.version!==lunr.version&&lunr.utils.warn("version mismatch: current "+lunr.version+" importing "+t.version);var e=new this;return e._fields=t.fields,e._ref=t.ref,e.documentStore=lunr.Store.load(t.documentStore),e.tokenStore=lunr.TokenStore.load(t.tokenStore),e.corpusTokens=lunr.SortedSet.load(t.corpusTokens),e.pipeline=lunr.Pipeline.load(t.pipeline),e},lunr.Index.prototype.field=function(t,e){var e=e||{},n={name:t,boost:e.boost||1};return this._fields.push(n),this},lunr.Index.prototype.ref=function(t){return this._ref=t,this},lunr.Index.prototype.add=function(t,e){var n={},r=new lunr.SortedSet,i=t[this._ref],e=void 0===e?!0:e;this._fields.forEach(function(e){var i=this.pipeline.run(lunr.tokenizer(t[e.name]));n[e.name]=i,lunr.SortedSet.prototype.add.apply(r,i)},this),this.documentStore.set(i,r),lunr.SortedSet.prototype.add.apply(this.corpusTokens,r.toArray());for(var o=0;r.length>o;o++){var s=r.elements[o],l=this._fields.reduce(function(t,e){var r=n[e.name].length;if(!r)return t;var i=n[e.name].filter(function(t){return t===s}).length;return t+i/r*e.boost},0);this.tokenStore.add(s,{ref:i,tf:l})}e&&this.eventEmitter.emit("add",t,this)},lunr.Index.prototype.remove=function(t,e){var n=t[this._ref],e=void 0===e?!0:e;if(this.documentStore.has(n)){var r=this.documentStore.get(n);this.documentStore.remove(n),r.forEach(function(t){this.tokenStore.remove(t,n)},this),e&&this.eventEmitter.emit("remove",t,this)}},lunr.Index.prototype.update=function(t,e){var e=void 0===e?!0:e;this.remove(t,!1),this.add(t,!1),e&&this.eventEmitter.emit("update",t,this)},lunr.Index.prototype.idf=function(t){if(this._idfCache[t])return this._idfCache[t];var e=this.tokenStore.count(t),n=1;return e>0&&(n=1+Math.log(this.tokenStore.length/e)),this._idfCache[t]=n},lunr.Index.prototype.search=function(t){var e=this.pipeline.run(lunr.tokenizer(t)),n=lunr.utils.zeroFillArray(this.corpusTokens.length),r=[],i=this._fields.reduce(function(t,e){return t+e.boost},0),o=e.some(function(t){return this.tokenStore.has(t)},this);if(!o)return[];e.forEach(function(t,e,o){var s=1/o.length*this._fields.length*i,l=this,u=this.tokenStore.expand(t).reduce(function(e,r){var i=l.corpusTokens.indexOf(r),o=l.idf(r),u=1,a=new lunr.SortedSet;if(r!==t){var h=Math.max(3,r.length-t.length);u=1/Math.log(h)}return i>-1&&(n[i]=s*o*u),Object.keys(l.tokenStore.get(r)).forEach(function(t){a.add(t)}),e.union(a)},new lunr.SortedSet);r.push(u)},this);var s=r.reduce(function(t,e){return t.intersect(e)}),l=new lunr.Vector(n);return s.map(function(t){return{ref:t,score:l.similarity(this.documentVector(t))}},this).sort(function(t,e){return e.score-t.score})},lunr.Index.prototype.documentVector=function(t){for(var e=this.documentStore.get(t),n=e.length,r=lunr.utils.zeroFillArray(this.corpusTokens.length),i=0;n>i;i++){var o=e.elements[i],s=this.tokenStore.get(o)[t].tf,l=this.idf(o);r[this.corpusTokens.indexOf(o)]=s*l}return new lunr.Vector(r)},lunr.Index.prototype.toJSON=function(){return{version:lunr.version,fields:this._fields,ref:this._ref,documentStore:this.documentStore.toJSON(),tokenStore:this.tokenStore.toJSON(),corpusTokens:this.corpusTokens.toJSON(),pipeline:this.pipeline.toJSON()}},lunr.Store=function(){this.store={},this.length=0},lunr.Store.load=function(t){var e=new this;return e.length=t.length,e.store=Object.keys(t.store).reduce(function(e,n){return e[n]=lunr.SortedSet.load(t.store[n]),e},{}),e},lunr.Store.prototype.set=function(t,e){this.store[t]=e,this.length=Object.keys(this.store).length},lunr.Store.prototype.get=function(t){return this.store[t]},lunr.Store.prototype.has=function(t){return t in this.store},lunr.Store.prototype.remove=function(t){this.has(t)&&(delete this.store[t],this.length--)},lunr.Store.prototype.toJSON=function(){return{store:this.store,length:this.length}},lunr.stemmer=function(){var t={ational:"ate",tional:"tion",enci:"ence",anci:"ance",izer:"ize",bli:"ble",alli:"al",entli:"ent",eli:"e",ousli:"ous",ization:"ize",ation:"ate",ator:"ate",alism:"al",iveness:"ive",fulness:"ful",ousness:"ous",aliti:"al",iviti:"ive",biliti:"ble",logi:"log"},e={icate:"ic",ative:"",alize:"al",iciti:"ic",ical:"ic",ful:"",ness:""},n="[^aeiou]",r="[aeiouy]",i=n+"[^aeiouy]*",o=r+"[aeiou]*",s="^("+i+")?"+o+i,l="^("+i+")?"+o+i+"("+o+")?$",u="^("+i+")?"+o+i+o+i,a="^("+i+")?"+r;return function(n){var o,h,c,p,f,d,v;if(3>n.length)return n;if(c=n.substr(0,1),"y"==c&&(n=c.toUpperCase()+n.substr(1)),p=/^(.+?)(ss|i)es$/,f=/^(.+?)([^s])s$/,p.test(n)?n=n.replace(p,"$1$2"):f.test(n)&&(n=n.replace(f,"$1$2")),p=/^(.+?)eed$/,f=/^(.+?)(ed|ing)$/,p.test(n)){var m=p.exec(n);p=RegExp(s),p.test(m[1])&&(p=/.$/,n=n.replace(p,""))}else if(f.test(n)){var m=f.exec(n);o=m[1],f=RegExp(a),f.test(o)&&(n=o,f=/(at|bl|iz)$/,d=RegExp("([^aeiouylsz])\\1$"),v=RegExp("^"+i+r+"[^aeiouwxy]$"),f.test(n)?n+="e":d.test(n)?(p=/.$/,n=n.replace(p,"")):v.test(n)&&(n+="e"))}if(p=/^(.+?)y$/,p.test(n)){var m=p.exec(n);o=m[1],p=RegExp(a),p.test(o)&&(n=o+"i")}if(p=/^(.+?)(ational|tional|enci|anci|izer|bli|alli|entli|eli|ousli|ization|ation|ator|alism|iveness|fulness|ousness|aliti|iviti|biliti|logi)$/,p.test(n)){var m=p.exec(n);o=m[1],h=m[2],p=RegExp(s),p.test(o)&&(n=o+t[h])}if(p=/^(.+?)(icate|ative|alize|iciti|ical|ful|ness)$/,p.test(n)){var m=p.exec(n);o=m[1],h=m[2],p=RegExp(s),p.test(o)&&(n=o+e[h])}if(p=/^(.+?)(al|ance|ence|er|ic|able|ible|ant|ement|ment|ent|ou|ism|ate|iti|ous|ive|ize)$/,f=/^(.+?)(s|t)(ion)$/,p.test(n)){var m=p.exec(n);o=m[1],p=RegExp(u),p.test(o)&&(n=o)}else if(f.test(n)){var m=f.exec(n);o=m[1]+m[2],f=RegExp(u),f.test(o)&&(n=o)}if(p=/^(.+?)e$/,p.test(n)){var m=p.exec(n);o=m[1],p=RegExp(u),f=RegExp(l),d=RegExp("^"+i+r+"[^aeiouwxy]$"),(p.test(o)||f.test(o)&&!d.test(o))&&(n=o)}return p=/ll$/,f=RegExp(u),p.test(n)&&f.test(n)&&(p=/.$/,n=n.replace(p,"")),"y"==c&&(n=c.toLowerCase()+n.substr(1)),n}}(),lunr.Pipeline.registerFunction(lunr.stemmer,"stemmer"),lunr.stopWordFilter=function(t){return-1===lunr.stopWordFilter.stopWords.indexOf(t)?t:void 0},lunr.stopWordFilter.stopWords=new lunr.SortedSet,lunr.stopWordFilter.stopWords.length=119,lunr.stopWordFilter.stopWords.elements=["","a","able","about","across","after","all","almost","also","am","among","an","and","any","are","as","at","be","because","been","but","by","can","cannot","could","dear","did","do","does","either","else","ever","every","for","from","get","got","had","has","have","he","her","hers","him","his","how","however","i","if","in","into","is","it","its","just","least","let","like","likely","may","me","might","most","must","my","neither","no","nor","not","of","off","often","on","only","or","other","our","own","rather","said","say","says","she","should","since","so","some","than","that","the","their","them","then","there","these","they","this","tis","to","too","twas","us","wants","was","we","were","what","when","where","which","while","who","whom","why","will","with","would","yet","you","your"],lunr.Pipeline.registerFunction(lunr.stopWordFilter,"stopWordFilter"),lunr.TokenStore=function(){this.root={docs:{}},this.length=0},lunr.TokenStore.load=function(t){var e=new this;return e.root=t.root,e.length=t.length,e},lunr.TokenStore.prototype.add=function(t,e,n){var n=n||this.root,r=t[0],i=t.slice(1);return r in n||(n[r]={docs:{}}),0===i.length?(n[r].docs[e.ref]=e,this.length+=1,void 0):this.add(i,e,n[r])},lunr.TokenStore.prototype.has=function(t){if(!t)return!1;for(var e=this.root,n=0;t.length>n;n++){if(!e[t[n]])return!1;e=e[t[n]]}return!0},lunr.TokenStore.prototype.getNode=function(t){if(!t)return{};for(var e=this.root,n=0;t.length>n;n++){if(!e[t[n]])return{};e=e[t[n]]}return e},lunr.TokenStore.prototype.get=function(t,e){return this.getNode(t,e).docs||{}},lunr.TokenStore.prototype.count=function(t,e){return Object.keys(this.get(t,e)).length},lunr.TokenStore.prototype.remove=function(t,e){if(t){for(var n=this.root,r=0;t.length>r;r++){if(!(t[r]in n))return;n=n[t[r]]}delete n.docs[e]}},lunr.TokenStore.prototype.expand=function(t,e){var n=this.getNode(t),r=n.docs||{},e=e||[];return Object.keys(r).length&&e.push(t),Object.keys(n).forEach(function(n){"docs"!==n&&e.concat(this.expand(t+n,e))},this),e},lunr.TokenStore.prototype.toJSON=function(){return{root:this.root,length:this.length}};
/**
 * Copyright (c) 2007-2012 Ariel Flesler - aflesler(at)gmail(dot)com | http://flesler.blogspot.com
 * Dual licensed under MIT and GPL.
 * @author Ariel Flesler
 * @version 1.4.3.1
 */
;(function($){var h=$.scrollTo=function(a,b,c){$(window).scrollTo(a,b,c)};h.defaults={axis:'xy',duration:parseFloat($.fn.jquery)>=1.3?0:1,limit:true};h.window=function(a){return $(window)._scrollable()};$.fn._scrollable=function(){return this.map(function(){var a=this,isWin=!a.nodeName||$.inArray(a.nodeName.toLowerCase(),['iframe','#document','html','body'])!=-1;if(!isWin)return a;var b=(a.contentWindow||a).document||a.ownerDocument||a;return/webkit/i.test(navigator.userAgent)||b.compatMode=='BackCompat'?b.body:b.documentElement})};$.fn.scrollTo=function(e,f,g){if(typeof f=='object'){g=f;f=0}if(typeof g=='function')g={onAfter:g};if(e=='max')e=9e9;g=$.extend({},h.defaults,g);f=f||g.duration;g.queue=g.queue&&g.axis.length>1;if(g.queue)f/=2;g.offset=both(g.offset);g.over=both(g.over);return this._scrollable().each(function(){if(e==null)return;var d=this,$elem=$(d),targ=e,toff,attr={},win=$elem.is('html,body');switch(typeof targ){case'number':case'string':if(/^([+-]=)?\d+(\.\d+)?(px|%)?$/.test(targ)){targ=both(targ);break}targ=$(targ,this);if(!targ.length)return;case'object':if(targ.is||targ.style)toff=(targ=$(targ)).offset()}$.each(g.axis.split(''),function(i,a){var b=a=='x'?'Left':'Top',pos=b.toLowerCase(),key='scroll'+b,old=d[key],max=h.max(d,a);if(toff){attr[key]=toff[pos]+(win?0:old-$elem.offset()[pos]);if(g.margin){attr[key]-=parseInt(targ.css('margin'+b))||0;attr[key]-=parseInt(targ.css('border'+b+'Width'))||0}attr[key]+=g.offset[pos]||0;if(g.over[pos])attr[key]+=targ[a=='x'?'width':'height']()*g.over[pos]}else{var c=targ[pos];attr[key]=c.slice&&c.slice(-1)=='%'?parseFloat(c)/100*max:c}if(g.limit&&/^\d+$/.test(attr[key]))attr[key]=attr[key]<=0?0:Math.min(attr[key],max);if(!i&&g.queue){if(old!=attr[key])animate(g.onAfterFirst);delete attr[key]}});animate(g.onAfter);function animate(a){$elem.animate(attr,f,g.easing,a&&function(){a.call(this,e,g)})}}).end()};h.max=function(a,b){var c=b=='x'?'Width':'Height',scroll='scroll'+c;if(!$(a).is('html,body'))return a[scroll]-$(a)[c.toLowerCase()]();var d='client'+c,html=a.ownerDocument.documentElement,body=a.ownerDocument.body;return Math.max(html[scroll],body[scroll])-Math.min(html[d],body[d])};function both(a){return typeof a=='object'?a:{top:a,left:a}}})(jQuery);
/*!
 * jQuery Cookie Plugin v1.4.0
 * https://github.com/carhartl/jquery-cookie
 *
 * Copyright 2013 Klaus Hartl
 * Released under the MIT license
 */
(function(e){if(typeof define==="function"&&define.amd){define(["jquery"],e)}else{e(jQuery)}})(function(e){function n(e){return u.raw?e:encodeURIComponent(e)}function r(e){return u.raw?e:decodeURIComponent(e)}function i(e){return n(u.json?JSON.stringify(e):String(e))}function s(e){if(e.indexOf('"')===0){e=e.slice(1,-1).replace(/\\"/g,'"').replace(/\\\\/g,"\\")}try{e=decodeURIComponent(e.replace(t," "));return u.json?JSON.parse(e):e}catch(n){}}function o(t,n){var r=u.raw?t:s(t);return e.isFunction(n)?n(r):r}var t=/\+/g;var u=e.cookie=function(t,s,a){if(s!==undefined&&!e.isFunction(s)){a=e.extend({},u.defaults,a);if(typeof a.expires==="number"){var f=a.expires,l=a.expires=new Date;l.setTime(+l+f*864e5)}return document.cookie=[n(t),"=",i(s),a.expires?"; expires="+a.expires.toUTCString():"",a.path?"; path="+a.path:"",a.domain?"; domain="+a.domain:"",a.secure?"; secure":""].join("")}var c=t?undefined:{};var h=document.cookie?document.cookie.split("; "):[];for(var p=0,d=h.length;p<d;p++){var v=h[p].split("=");var m=r(v.shift());var g=v.join("=");if(t&&t===m){c=o(g,s);break}if(!t&&(g=o(g))!==undefined){c[m]=g}}return c};u.defaults={};e.removeCookie=function(t,n){if(e.cookie(t)===undefined){return false}e.cookie(t,"",e.extend({},n,{expires:-1}));return!e.cookie(t)}})
///////////////
// search.js //
///////////////

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

    if($('#overview-content').length){
        add_to_search('/1.1/api/index.html');
    }
    else if($('#api-content').length){
        add_to_search('/1.1/overview/index.html');
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
    console.debug($.cookie("language"));
    function fix_sidebar() {
        var window_height = $(window).height();
        var top_of_sidebar = 65;
        var height_of_sidebar = window_height - top_of_sidebar;
        $('.nav.nav-list').css('height', height_of_sidebar);
    }

    $(window).resize(function (){
        fix_sidebar();
    });

    $("li").bind('activate', updateNavigation);

    var defaultLang = $.cookie('language');
    console.log(defaultLang);
    defaultLang = (defaultLang != null) ? defaultLang : 'bash';
    defaultLang_dd = $("[data-lang='" + defaultLang +"']");
    console.log(defaultLang_dd);
    console.log(defaultLang_dd.text());
    updateLangTitle(defaultLang_dd.text());
    defaultLang_dd.parent().hide();
    $("[class^='highlight-']").hide();
    $("[class^='section-']").hide();
    $(".highlight-" + defaultLang).show();
    $(".section-" + defaultLang).show();
    $('.highlight-javascript').show();
    $('.highlight-html').show();

    $('.lang-change').click(function () {
        var lang = $(this).attr('data-lang');
        $.cookie('language', lang, { expires: 7, path: '/' });
        var langtext = $(this).text();
        updateLangTitle(langtext);
        var parent = $(this).parent();
        parent.siblings().show();
        parent.hide();
        $("[class^='highlight-']").hide();
        $(".highlight-javascript").show();
        $(".highlight-" + lang).show();
    });   

    scrollToAnchor(window.location.hash);
    $("body").on("click", "a", scrollToAnchor);
    fix_sidebar();
});