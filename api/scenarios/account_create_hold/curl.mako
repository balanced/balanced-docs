<%namespace file='/_main.mako' name='main'/>
<%
  method, path = main.route_for_endpoint('holds.create')
  uri = context['api_location']
  uri += path
%>

% if mode == 'definition':
  ${method} ${uri}

% else:
  <%
    uri = context['api_location'] + request['uri']
  %>
   curl ${uri} <%text>\</%text>
     -u ${api_key}: <%text>\</%text>
     -d amount=1000
% endif
