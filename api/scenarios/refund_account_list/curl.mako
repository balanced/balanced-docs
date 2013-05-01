<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('refunds.index', select=('marketplace_id', 'account_id'))
  main.curl_list_template('refunds.index', ep=ep)
%>
