<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Hold.capture(...)

% else:
${main.ruby_boilerplate()}
hold = Balanced::Hold.find('${request['hold_uri']}')
debit = hold.capture(
% for k, v in payload.iteritems():
  % if k != 'hold_uri':
  :${k} => '${v}',
  % endif
% endfor
)

% endif
