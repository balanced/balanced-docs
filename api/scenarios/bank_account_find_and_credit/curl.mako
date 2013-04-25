<%namespace file='/_main.mako' name='main'/>

% if request is not UNDEFINED:
   curl ${request['credits_uri']} <%text>\</%text>
      -u ${api_key}: <%text>\</%text>
      -d amount=${request['amount']}

% endif
