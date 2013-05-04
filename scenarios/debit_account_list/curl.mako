<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('debits.index', select='any')
%>
% if mode == 'definition':
  ${ep.method} ${ep.url}
% else:
  <%
    slash = '\\'
  %>
   curl ${Endpoint.qualify_uri(ctx, request['debits_uri'], limit=2)} ${slash}
      -u ${api_key}:
% endif
