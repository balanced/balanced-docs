<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Marketplace.create_buyer
% else:
${main.ruby_boilerplate()}
buyer = Balanced::Marketplace.my_marketplace.create_buyer(
% for k, v in payload.iteritems():
  :${k} => '${v}',
% endfor
)
% endif