<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('debits.create', select='shortest')
%>
% if mode == 'definition':
  ${ep.method} ${ep.url}
% else:
  <%
    slash = '\\'
  %>
   curl ${Endpoint.qualify_uri(ctx, request['debits_uri'])} ${slash}
      -u ${ctx.api_key}: ${slash}
  %if 'accept_type' in ctx.storage:
      -H "Accept-Type: ${ctx.storage['accept_type']}" ${slash}
  %endif
   % for k, v, slash in main.recursive_expand(request['payload']):
      -d "${k}=${v}" ${slash}
   % endfor
% endif
