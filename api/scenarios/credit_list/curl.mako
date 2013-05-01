<%namespace file='/_main.mako' name='main'/>
<%
  method, path = main.route_for_endpoint('credits.index')
  uri = context['api_location']
  uri += path
%>

% if mode == 'definition':
   GET ${uri}

% else:
  <%
    uri += '?limit=2'
  %>
   curl ${uri} <%text>\</%text>
      -u ${api_key}:
% endif
