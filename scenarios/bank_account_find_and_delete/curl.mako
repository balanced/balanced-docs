<%namespace file='/_main.mako' name='main'/>

% if request is not UNDEFINED:
   curl ${request['uri']} <%text>\</%text>
      -u ${api_key}: <%text>\</%text>
      -X DELETE

% endif
