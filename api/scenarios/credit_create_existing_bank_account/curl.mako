<%namespace file='/_main.mako' name='main'/>
<%
  method, path = main.route_for_endpoint('bank_account_credits.create')
  uri = context['api_location']
  uri += path
%>

% if request is UNDEFINED:
   POST ${uri}

% else:
  <%
    uri = main.interpolate_uri(uri, bank_account_id=request['id'])
    uri += '?limit=2'
  %>
   curl ${uri} <%text>\</%text>
      -u ${api_key}: <%text>\</%text>
      -d amount=${payload['amount']}
% endif
