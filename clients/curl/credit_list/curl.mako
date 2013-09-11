<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.route_for_endpoint('credits.index')
%>

% if mode == 'definition':
   GET ${ep.url}

% else:
  <%
    url = ep.format(limit=2)
  %>
   curl ${url} <%text>\</%text>
      -u ${api_key}:
% endif
