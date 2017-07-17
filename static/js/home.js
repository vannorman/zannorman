$(document).ready(function(){
/*	$('#tabButtonAbout').click(function(){
		ShowTab($(this),$('#tabAbout'));
	});
	$('#tabButtonPortfolio').click(function(){
		ShowTab($(this),$('#tabPortfolio'));
	});
	$('#tabButtonContact').click(function(){
		ShowTab($(this),$('#tabContact'));
	}); */
	$('.tabButton').click(function(){
		$('.tabButton').each(function(){
			$(this).removeClass('selected');
		});
		ShowTab($(this).index());
		$(this).addClass('selected');
	});
//	ShowTab($('#tabButtonPortfolio'),$('#tabPortfolio'));
});

function ShowTab(i){
	$('.tab').each(function(){
		if ($(this).index() == i){
			$(this).fadeIn();
		} else {
			$(this).fadeOut();
		}
	});

}


