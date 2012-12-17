<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Debit.refund()

% else:
${main.python_boilerplate()}
debit = balanced.Debit.find('${request['debit_uri']}')
debit.refund()

% endif
