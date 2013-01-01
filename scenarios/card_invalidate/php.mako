<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Card->save()

% else:
${main.php_boilerplate()}
$card = Balanced\Card::get("${request['uri']}");
$card->is_valid = false;
$card->save();
% endif
