<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Card.new

% else:
${main.ruby_boilerplate()}
card = Balanced::Card.new(
  :uri => '${request['uri']}',
% for k, v in payload.iteritems():
  :${k} => '${v}',
% endfor
).save
% endif
