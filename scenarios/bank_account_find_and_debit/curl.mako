<%namespace file='/_main.mako' name='main'/>
<%
    ep = main.make_endpoint('customers/debits.create')
%>
% if mode == 'definition':
    POST https://api.balancedpayments.com/v1/bank_accounts/:bank_account_id/debits
% else:
    curl ${request['debits_uri']} <%text>\</%text>
    -u ${api_key}: <%text>\</%text>
    -d amount=${request['amount']}

% endif