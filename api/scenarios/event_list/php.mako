<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    \Balanced\Event->all()

% else:
    ${main.php_boilerplate()}
    \Balanced\Event->all()

% endif
