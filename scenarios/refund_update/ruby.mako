<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Refund.save()

% else:
${main.ruby_boilerplate()}
refund = Balanced::Refund.find('${request['uri']}')
refund.description = '${payload['description']}'
refund.meta = {
% for k, v in payload['meta'].iteritems():
  :'${k}' => '${v}',
% endfor
}
refund.save

% endif
