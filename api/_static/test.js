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

function switchCode(switchText){
	$('.highlight').parents('.section').hide();
	$('.highlight-javascript').parents('.section').show();
	$('.highlight-' + switchText).parents('.section').show();
}