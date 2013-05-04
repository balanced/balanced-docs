<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.route_for_endpoint('bank_account_credits.create')
%>

% if mode == 'definition':
   POST ${ep.url}

% else:
  <%
    url = main.interpolate_uri(ep.url, bank_account_id=request['id'])
    url += '?limit=2'
  %>
   curl ${url} <%text>\</%text>
      -u ${api_key}: <%text>\</%text>
      -d amount=${payload['amount']}
% endif
