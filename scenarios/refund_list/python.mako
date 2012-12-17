<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Refund.query()

% else:
${main.python_boilerplate()}
refunds = balanced.Refund.query.all();

% endif
