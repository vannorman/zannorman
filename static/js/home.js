$(document).ready(function(){
	$('#tabButtonAbout').click(function(){
		ShowTab($('#tabAbout'));
	});
	$('#tabButtonPortfolio').click(function(){
		ShowTab($('#tabPortfolio'));
	});
	$('#tabButtonContact').click(function(){
		ShowTab($('#tabContact'));
	});
});

function HideTabs () {
	$('#tabAbout').fadeOut();
	$('#tabPortfolio').fadeOut();
	$('#tabContact').fadeOut();	
}

function ShowTab($el) {
	console.log('%c show:'+$el.name+';','color:#07f');
	HideTabs();
	$el.fadeIn();	
}
