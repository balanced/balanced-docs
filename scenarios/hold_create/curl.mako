<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('holds.create', select='shortest')
%>
% if mode == 'definition':
  ${ep.method} ${ep.url}
% else:
  <%
    slash = '\\'
  %>
   curl ${Endpoint.qualify_uri(ctx, request['holds_uri'])} ${slash}
      -u ${api_key}: ${slash}
   % for k, v, slash in main.recursive_expand(request['payload']):
      -d "${k}=${v}" ${slash}
   % endfor
% endif
