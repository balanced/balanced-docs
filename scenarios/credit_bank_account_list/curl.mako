<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.route_for_endpoint('bank_account_credits.index')
%>

% if mode == 'definition':
   GET ${ep.url}

% else:
  <%
    r = context['request']
    url = ep.format(bank_account_id=r['id'], limit=2)
  %>
   curl ${url} <%text>\</%text>
      -u ${api_key}:
% endif
