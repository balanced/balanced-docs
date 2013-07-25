<%namespace file='/_main.mako' name='main'/>
<%
    ep = main.make_endpoint('customers/debits.create')
%>
% if mode == 'definition':

    POST https://api.balancedpayments.com/v1/customers/:customer_id/debits
% else:
    curl ${request['url']} <%text>\</%text>
    -u ${api_key}: <%text>\</%text>
    -d card_number=${request['payload']['card_number']}  <%text>\</%text>
    -d expiration_month=${request['payload']['expiration_month']}  <%text>\</%text>
    -d expiration_year=${request['payload']['expiration_year']}  <%text>\</%text>
    -d security_code=${request['payload']['security_code']}

% endif