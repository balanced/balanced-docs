<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Debit.save()

% else:
${main.ruby_boilerplate()}
debit = Balanced::Debit.find('${request['uri']}')
debit.description = '${payload['description']}'
debit.meta = {
% for k, v in payload['meta'].iteritems():
  :'${k}' => '${v}',
% endfor
}
debit.save

% endif
