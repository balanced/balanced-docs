## http://stackoverflow.com/a/6701741/133514
<%def name="route_for_endpoint(endpoint)">
<%
  import _utils
  method, path = _utils.routify(endpoint)
  return method, path
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

<%def name="make_endpoint(endpoint_name)">
<%
  return context['Endpoint'](context, endpoint_name)
%>
</%def>

<%def name="php_boilerplate()">
## i'm putting this between an interpolation because pycharm's introspection
## correctly detects that this is an unclosed tag and warns me..annoying.
${"<?php"}

require(__DIR__ . '/vendor/autoload.php');

Httpful\Bootstrap::init();
RESTful\Bootstrap::init();
Balanced\Bootstrap::init();

%if 'api.balancedpayments.com' not in api_location:
Balanced\Settings::configure("${api_location}", "${api_key}");
%else:
Balanced\Settings::$api_key = "${api_key}";
%endif

</%def>

<%def name="python_boilerplate()">
import balanced

%if 'api.balancedpayments.com' not in api_location:
balanced.config.root_uri = "${api_location}"
%endif
balanced.configure("${api_key}")
</%def>

<%def name="ruby_boilerplate()">
require 'balanced'
%if 'api.balancedpayments.com' not in api_location:
<%
  import urlparse
  parsed_url = urlparse.urlparse(api_location)
  _root_url = parsed_url.netloc
  if ':' in _root_url:
      _root_url, _, _ = parsed_url.netloc.partition(':')

%>
options = {
  :scheme => 'http',
  :host => '${_root_url}',
  :port => 5000,
}
Balanced.configure('${api_key}', options)
%else:
Balanced.configure('${api_key}')
%endif
</%def>


<%def name="curl_show_template(endpoint_name)">
<%
  ep = make_endpoint(endpoint_name).force_shortest_url_path()
%>
% if request is UNDEFINED:
   ${ep.method} ${ep.full_url}
% else:
  <%
    slash = '\\'
  %>
  curl ${ep.qualified_url_for(request['uri'])} ${slash}
     -u ${api_key}:
% endif
</%def>


<%def name="curl_create_template(endpoint_name, uri='uri', ep=None)">
<%
  ep = ep or make_endpoint(endpoint_name).force_shortest_url_path()
%>
%if request is UNDEFINED:
   ${ep.method} ${ep.full_url}
%else:
  <%
    slash = '\\'
  %>
  curl ${ep.qualified_url_for(request[uri])} ${slash}
     -u ${api_key}: ${slash}
  %if 'payload' in request:
   %for k, v, slash in recursive_expand(request['payload']):
     -d "${k}=${v}" ${slash}
   %endfor
  %else:
     -X POST
  %endif
%endif
</%def>

<%def name="curl_update_template(endpoint_name, uri='uri', ep=None)">
<%
  ep = ep or make_endpoint(endpoint_name).force_shortest_url_path()
%>
%if request is UNDEFINED:
   ${ep.method} ${ep.full_url}
%else:
  <%
    slash = '\\'
  %>
  curl ${ep.qualified_url_for(request[uri])} ${slash}
     -u ${api_key}: ${slash}
     -X PUT ${slash}
   %for k, v, slash in recursive_expand(request['payload']):
     -d "${k}=${v}" ${slash}
   %endfor
%endif
</%def>


<%def name="curl_list_template(endpoint_name, limit=2, ep=None)">
<%
  ep = ep or make_endpoint(endpoint_name).force_shortest_url_path()
%>
% if request is UNDEFINED:
  ${ep.method} ${ep.full_url}
% else:
  <%
    slash = '\\'
  %>
   curl ${ep.qualified_url_for(request['uri'], limit=limit)} ${slash}
      -u ${api_key}:
% endif
</%def>

<%def name="curl_delete_template(endpoint_name, ep=None)">
<%
  ep = ep or make_endpoint(endpoint_name)
%>
% if request is UNDEFINED:
  ${ep.method} ${ep.full_url}
% else:
  <%
    slash = '\\'
  %>
   curl ${ep.qualified_url_for(request['uri'])} ${slash}
     -u ${api_key}: ${slash}
     -X DELETE
% endif
</%def>

