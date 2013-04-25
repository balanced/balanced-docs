<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced::Callback.all
% else:
    ${main.ruby_boilerplate()}
    marketplace = Balanced::Marketplace.my_marketplace

    callbacks = Balanced::Callback.all(:limit => 2)
% endif
