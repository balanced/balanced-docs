<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Card.save()

% else:
${main.ruby_boilerplate()}
card = Balanced::Card.find('${request['uri']}')
card.meta = {
% for k, v in payload['meta'].iteritems():
  :'${k}' => '${v}',
% endfor
}
card.save

% endif