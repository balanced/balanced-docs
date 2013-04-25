<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('debits.create')
  main.curl_create_template('debits.create', uri='debits_uri', ep=ep)
%>
