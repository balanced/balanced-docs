<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Account.promote_to_merchant

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

merchant_data = {
% for k, v in payload['merchant'].iteritems():
  :${k} => '${v}',
% endfor
}

account = Balanced::Marketplace.my_marketplace.create_account

begin
  account.promote_to_merchant(merchant_data)
rescue Balanced::MoreInformationRequired => error
  # could not identify this account.
  puts 'redirect merchant to: ' + error.redirect_uri
rescue Balanced::Error => error
  # TODO: handle 400 and 409 exceptions as required
  raise
end

% endif

