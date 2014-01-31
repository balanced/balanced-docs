<%def name="recursive_expand(dikt, delimiter='\\')" filter="trim">
<%
    if not dikt:
        raise StopIteration

    keys = sorted(dikt.keys(), key=lambda x: isinstance(dikt[x], dict))
    try:
        last = keys[-1]
    except IndexError:
        last = keys[0]

    lines = []
    for k in keys:
        if isinstance(dikt[k], dict):
            for subk, v, slash in recursive_expand(dikt[k], delimiter):
                lines.append(('{0}[{1}]'.format(k, subk), v, slash))
        else:
            lines.append((k, dikt[k], '' if k is last else delimiter))
    return lines
%>
</%def>

## http://stackoverflow.com/a/6701741/133514
<%def name="route_for_endpoint(endpoint, select='shortest')">
<%
  return context['Endpoint'](ctx, endpoint, select)
%>
</%def>

<%def name="interpolate_uri(uri, **kwargs)">
<%
  # this basically parses :bank_account_id to a string with {bank_account_id}
  # for much easier interpolation.
  import re
  # note that it shouldn't start with a digit!
  _uri = re.sub('(:([^\d]\w+))+', r'{\2}', uri)
  return _uri.format(**kwargs)
%>
</%def>

<%def name="make_endpoint(endpoint_name, select=None)">
<%
  return context['Endpoint'](ctx, endpoint_name, select)
%>
</%def>


<%def name="curl_show_template(endpoint_name, sel='shortest')">
<%
  ep = Endpoint(ctx, endpoint_name, select=sel)
%>
%if mode == 'definition':
  ${ep.method} ${ep.url}
%else:
  <%
    slash = '\\'
  %>
  curl ${Endpoint.qualify_uri(ctx, request['uri'])} ${slash}
  %if 'accept_type' in ctx.storage:
     -H "Accept: ${ctx.storage['accept_type']}" ${slash}
  %endif
     -u ${ctx.api_key}:
%endif
</%def>


<%def name="curl_create_template(endpoint_name, uri='uri', ep=None, sel='shortest')">
<%
  ep = ep if ep else Endpoint(ctx, endpoint_name, select=sel)
%>
%if mode == 'definition':
   ${ep.method} ${ep.url}
%elif mode == 'request':
  <%
    slash = '\\'
  %>
  curl ${Endpoint.qualify_uri(ctx, request[uri])} ${slash}
  %if 'accept_type' in ctx.storage:
     -H "Accept: ${ctx.storage['accept_type']}" ${slash}
  %endif
     -u ${ctx.api_key}: ${slash}
  %if 'payload' in request:
   %for k, v, slash in recursive_expand(request['payload']):
     -d "${k}=${v}" ${slash}
   %endfor
  %else:
     -X POST
  %endif
%endif
</%def>

<%def name="curl_update_template(endpoint_name, uri='uri', ep=None, sel='shortest')">
<%
  ep = Endpoint(ctx, endpoint_name, select=sel)
%>
%if mode == 'definition':
   ${ep.method} ${ep.url}
%elif mode == 'request':
  <%
    slash = '\\'
  %>
  curl ${Endpoint.qualify_uri(ctx, request[uri])} ${slash}
  %if 'accept_type' in ctx.storage:
     -H "Accept: ${ctx.storage['accept_type']}" ${slash}
  %endif
     -u ${ctx.api_key}: ${slash}
     -X PUT ${slash}
   %for k, v, slash in recursive_expand(request['payload']):
     -d "${k}=${v}" ${slash}
   %endfor
%endif
</%def>


<%def name="curl_list_template(endpoint_name, uri='uri', ep=None, sel='shortest')">
<%
  ep = Endpoint(ctx, endpoint_name, select=sel)
%>
%if mode == 'definition':
  ${ep.method} ${ep.url}
%elif mode == 'request':
  <%
    slash = '\\'
  %>
   curl ${Endpoint.qualify_uri(ctx, request[uri])} ${slash}
   %if 'accept_type' in ctx.storage:
      -H "Accept: ${ctx.storage['accept_type']}" ${slash}
   %endif
      -u ${ctx.api_key}:
%endif
</%def>

<%def name="curl_delete_template(endpoint_name, uri='uri', ep=None, sel='shortest')">
<%
  ep = Endpoint(ctx, endpoint_name, select=sel)
%>
%if mode == 'definition':
  ${ep.method} ${ep.url}
%elif mode == 'request':
  <%
    slash = '\\'
  %>
   curl ${Endpoint.qualify_uri(ctx, request[uri])} ${slash}
   %if 'accept_type' in ctx.storage:
     -H "Accept: ${ctx.storage['accept_type']}" ${slash}
   %endif
     -u ${ctx.api_key}: ${slash}
     -X DELETE
%endif
</%def>


<%def name="curl_query_template(endpoint_name, uri='uri', ep=None, sel='shortest')">
<%
  ep = Endpoint(ctx, endpoint_name, select=sel)
%>
%if mode == 'definition':
  ${ep.method} ${ep.url}
%elif mode == 'request':
  <%
    slash = '\\'
  %>
   curl ${Endpoint.qualify_uri(ctx, request[uri])} ${slash}
     -u ${ctx.api_key}: ${slash}
     -X DELETE
%endif
</%def>