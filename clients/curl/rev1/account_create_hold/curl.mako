<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.route_for_endpoint('holds.create', select=['marketplace_id', 'account_id'])
  url = ep.format(
      marketplace_id=ctx.storage['marketplace_id'],
      account_id=request['account_id'],
  )
%>

% if mode == 'definition':
  ${ep.method} ${url}

% else:
   curl ${url} <%text>\</%text>
     -u ${api_key}: <%text>\</%text>
     -d amount=1000
% endif
