<%namespace file='/_main.mako' name='main'/>
<%
  method, path = main.route_for_endpoint()
  uri = context['api_location']
  uri += path
%>

% if request is UNDEFINED:
   GET ${uri}

% else:
  <%
    r = context['request']
    uri = main.interpolate_uri(uri, bank_account_id=r['id'])
    uri += '?limit=2'
  %>
   curl ${uri} <%text>\</%text>
      -u ${api_key}:
% endif
