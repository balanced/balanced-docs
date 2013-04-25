<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::BadRequest

% else:
${main.ruby_boilerplate()}
bank_account = Balanced::BankAccount.new(
 :uri => '${request['uri']}',
% for k, v in payload.iteritems():
 :${k} => '${v}',
% endfor
)

begin
  bank_account.save
rescue Balanced::BadRequest => ex
  raise "Key is not returned!" unless ex.extras.has_key? "routing_number"
end

% endif
