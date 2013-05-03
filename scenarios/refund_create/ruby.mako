<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Debit.refund()

% else:
${main.ruby_boilerplate()}
debit = Balanced::Debit.find('${request['debit_uri']}')
debit.refund(
    :description => '${payload['description']}',
    :meta => {
    % for k, v in payload['meta'].iteritems():
        :'${k}' => '${v}',
    % endfor
    },
)

% endif
