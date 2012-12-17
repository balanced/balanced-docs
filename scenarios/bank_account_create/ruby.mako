<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::BankAccount.save

% else:
${main.ruby_boilerplate()}
bank_account = Balanced::BankAccount.new(
% for k, v in payload.iteritems():
  :${k} => '${v}',
% endfor
).save

% endif
