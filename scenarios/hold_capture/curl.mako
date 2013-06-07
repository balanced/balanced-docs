<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('customer_debits.create', select='any')
  main.curl_create_template('customer_debits.create', uri='debits_uri', ep=ep)
%>
