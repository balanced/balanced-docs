<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Account.debit(...)

% else:
${main.python_boilerplate()}
buyer = balanced.Account.find('${request['account_uri']}')
buyer.debit(
% for k, v in payload.iteritems():
    ${k}='${v}',
% endfor
)

% endif
