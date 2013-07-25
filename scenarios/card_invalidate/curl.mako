<%namespace file='/_main.mako' name='main'/>
<%
   if ctx.storage['api_rev'] == 'rev0':
       main.curl_update_template('marketplaces/cards.update')
   else:
       main.curl_delete_template('cards.delete')
%>
