<%namespace file='/_main.mako' name='main'/>
<%
    ep = main.make_endpoint('events.index', select='shortest')
%>
% if mode == 'definition':
    ${ep.method} ${ep.url}
% else:
    <%
        slash = '\\'
    %>
    curl ${Endpoint.qualify_uri(ctx, request['uri'], limit=2)} ${slash}
       -u ${api_key}: ${slash}
    %if 'accept_type' in ctx.storage:
       -H "Accept-Type: ${ctx.storage['accept_type']}"
    %endif
% endif
