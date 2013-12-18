<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('legacy_accounts.create')
%>
% if mode == 'definition':
  ${ep.method} ${ep.url}
% else:
    curl ${Endpoint.qualify_uri(ctx, request['accounts_uri'])} ${'\\'}
        -u ${api_key}: ${'\\'}
      % for k, v, slash in main.recursive_expand(request['payload']):
        -d "${k}=${v}" ${slash}
      % endfor
% endif
