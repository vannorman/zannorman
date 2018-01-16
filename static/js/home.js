$(document).ready(function(){
	curTab = window.location.href.substr(window.location.href.lastIndexOf('/') + 1);
	curTab = parseInt(curTab.replace("#",""));
	console.log("curtab:"+curTab);
	if (Number.isInteger(curTab) && curTab != 0){
		ShowTab(curTab);
	}
	$('.tabButton').click(function(){
		ShowTab($(this).index());
	});
});

function ShowTab(i){
//	console.log('showtab '+i);
	$('.tabButton').each(function(){
		if ($(this).index() == i){
			$(this).addClass('selected');

		} else {
			$(this).removeClass('selected');
		}
	});
	var index = 0;
	$('.tab').each(function(){
//		console.log('tabeach:'+$(this).className+", index;"+$(this).index()+", i;"+i);
//		if ($(this).index() == i){
		if (index == i){
//			console.log('fadein '+i);
			window.history.pushState("object or string", "Charlie Van Norman", "#"+i); //+$(this).attr('id'));
			$(this).fadeIn();
		} else {
//			console.log('fadeout '+i);
			$(this).fadeOut();
		}
		index ++;
	});

}


