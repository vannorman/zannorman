$(document).ready(function(){
	$('#tabButtonAbout').click(function(){
		ShowTab($(this),$('#tabAbout'));
	});
	$('#tabButtonPortfolio').click(function(){
		ShowTab($(this),$('#tabPortfolio'));
	});
	$('#tabButtonContact').click(function(){
		ShowTab($(this),$('#tabContact'));
	});
});

function HideTabs () {
	$('.tab').each(function(){
		$(this).fadeOut();
	});
	$('.tabButton').each(function(){
		$(this).removeClass('selected');
	});

}

function ShowTab($button,$el) {
	if ($button.hasClass('selected')) return;
	HideTabs();
	$el.fadeIn();
	$button.addClass('selected');
//	window.history.pushState({},"", "#"+$el.attr('id'));
 
}
