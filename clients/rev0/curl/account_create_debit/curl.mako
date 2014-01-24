<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('debits.create', select=['marketplace_id', 'account_id'])
  main.curl_create_template('debits.create', ep=ep)
%>
