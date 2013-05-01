<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('debits.index', select='shortest')
%>
% if request is UNDEFINED:
  ${ep.method} ${ep.url}
% else:
  <%
    slash = '\\'
  %>
   curl ${Endpoint.qualify_uri(ctx, request['uri'], limit=2)} ${slash}
      -u ${api_key}:
% endif