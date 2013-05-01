<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.route_for_endpoint('credits.create')
%>

% if mode == 'definition':
   POST ${ep.url}

% else:
   curl ${ep.url} <%text>\</%text>
      -u ${api_key}: <%text>\</%text>
   %for k, v, slash in main.recursive_expand(request):
      -d "${k}=${v}" ${slash}
   %endfor

% endif
