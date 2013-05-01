<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('accounts.create')
%>
% if mode == 'definition':
  ${ep.method} ${ep.url}
% else:
  <%
    slash = '\\'
  %>
   curl ${Endpoint.qualify_uri(ctx, request['accounts_uri'])} ${slash}
        -u ${api_key}: ${slash}
      % for k, v, slash in recursive_expand(request['payload']):
        -d "${k}=${v}" ${slash}
      % endfor
% endif