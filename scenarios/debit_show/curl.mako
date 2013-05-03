<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('debits.show', select='shortest')
%>
% if mode == 'definition':
  ${ep.method} ${ep.url}
% else:
  <%
    slash = '\\'
  %>
   curl ${Endpoint.qualify_uri(ctx, request['uri'])} ${slash}
      -u ${api_key}:
% endif