<%namespace file='/_main.mako' name='main'/>
<%
  method, path = main.route_for_endpoint('credits.create')
  uri = context['api_location']
  uri += path
%>

% if mode == 'definition':
   POST ${uri}

% else:
   curl ${uri} <%text>\</%text>
      -u ${api_key}: <%text>\</%text>
   %for k, v, slash in recursive_expand(request):
      -d "${k}=${v}" ${slash}
   %endfor

% endif
