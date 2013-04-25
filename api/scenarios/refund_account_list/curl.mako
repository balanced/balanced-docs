<%namespace file='/_main.mako' name='main'/>
<%
  ep = main.make_endpoint('refunds.index')
  ep.force_path(comparator=max)
  main.curl_list_template('refunds.index', ep=ep)
%>