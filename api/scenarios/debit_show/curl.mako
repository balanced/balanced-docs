<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('debits.show').force_shortest_url_path()
%>
% if request is UNDEFINED:
  ${ep.method} ${ep.full_url}
% else:
  <%
    slash = '\\'
  %>
   curl ${ep.qualified_url_for(request['uri'])} ${slash}
      -u ${api_key}:
% endif