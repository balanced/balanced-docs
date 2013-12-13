<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.route_for_endpoint('credits.show')
%>

% if mode == 'definition':
   GET ${ep.uri}

% else:
  <%
    r = context['request']
    url = ep.format(credit_id=r['id'])
  %>
   curl ${url} <%text>\</%text>
      -u ${api_key}:
% endif
