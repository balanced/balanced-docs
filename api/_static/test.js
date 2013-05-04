$(function(){
	$('.langbar li:first').addClass('selected');
	switchCode('bash');
	$('.langbar li').on('click', function(e){
		var $this = $(this);
		var switchText;
		if($this.html() === 'curl'){
			switchText = 'bash';
		}
		else{
			switchText = $this.html();
		}
		e.preventDefault();
		$('.langbar li').removeClass('selected');
		$this.addClass('selected');
		switchCode(switchText);
	});
});

function switchCode(language){
	$('.highlight').closest('.code-block').parent().hide();
    $('.highlight-javascript').closest('.code-block').parent().show();
    $('.highlight-' + language).closest('.code-block').parent().show();
}