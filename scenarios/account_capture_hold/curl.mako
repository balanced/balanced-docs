<%namespace file='/_main.mako' name='main'/>
<%
    ep = main.make_endpoint('debits.create')
    ep.force_path(key=lambda r: 'accounts/:account_id' in r[1])
    main.curl_create_template('debits.create', ep=ep)
%>