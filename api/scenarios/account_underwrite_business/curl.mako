<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('accounts.create')
%>
% if request is UNDEFINED:
  ${ep.method} ${ep.full_url}
% else:
    curl ${ep.qualified_url_for(request['accounts_uri'])} ${'\\'}
        -u ${api_key}: ${'\\'}
      % for k, v, slash in recursive_expand(request['payload']):
        -d "${k}=${v}" ${slash}
      % endfor
% endif