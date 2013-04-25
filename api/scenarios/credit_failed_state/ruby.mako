<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Credit.save

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

bank_account_info = {
% for k, v in request['bank_account'].iteritems():
  :${k} => '${v}',
% endfor
}
credit = Balanced::Credit.new(
  :amount => ${request['amount']},
  :bank_account => bank_account_info
).save

% endif
