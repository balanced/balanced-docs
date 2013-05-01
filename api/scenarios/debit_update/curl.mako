<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('debits.update', select='shortest')
%>
% if request is UNDEFINED:
  ${ep.method} ${ep.url}
% else:
  <%
    slash = '\\'
  %>
   curl ${Endpoint.qualify_uri(ctx, request['uri'])} ${slash}
      -u ${api_key}: ${slash}
      -X PUT ${slash}
   % for k, v, slash in main.recursive_expand(request['payload']):
      -d "${k}=${v}" ${slash}
   % endfor
% endif