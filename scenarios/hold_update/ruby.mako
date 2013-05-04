<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Hold.save()

% else:
${main.ruby_boilerplate()}
hold = Balanced::Hold.find('${request['uri']}')
hold.description = '${payload['description']}'
hold.meta = {
% for k, v in payload['meta'].iteritems():
  :'${k}' => '${v}',
% endfor
}
hold.save

% endif
