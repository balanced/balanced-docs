<%namespace file='/_main.mako' name='main'/>
<%
  method, path = main.route_for_endpoint('credits.show')
  uri = context['api_location']
  uri += path
%>

% if request is UNDEFINED:
   GET ${uri}

% else:
  <%
    r = context['request']
    uri = main.interpolate_uri(uri, credit_id=r['id'])
  %>
   curl ${uri} <%text>\</%text>
      -u ${api_key}:
% endif
