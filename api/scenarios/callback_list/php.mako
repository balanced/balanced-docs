<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    \Balanced\Callback->all()

% else:
    ${main.php_boilerplate()}
    \Balanced\Callback->all()

% endif
