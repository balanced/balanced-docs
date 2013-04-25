<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('debits.index').force_shortest_url_path()
%>
% if request is UNDEFINED:
  ${ep.method} ${ep.full_url}
% else:
  <%
    slash = '\\'
  %>
   curl ${ep.qualified_url_for(request['uri'], limit=2)} ${slash}
      -u ${api_key}:
% endif