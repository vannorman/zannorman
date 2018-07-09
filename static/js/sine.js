var d1 = 1.1;
var d2 = 10.5;
var speed = 1;
var frequency = 20;
var step = -4;
var mode = 3;

$(document).ready(function(){
	init();
	$('body').append("<div id='debug'></div>");
	$(document).mousemove(function( event ) {
//		frequency = event.pageX;
//		step = event.pageY;
	});


});

function plotSine(ctx, xOffset, yOffset) {
	$('#debug').text('step:'+step.toFixed(2)+', freq:'+frequency+", d1:"+d1.toFixed(2)+", d2:"+d2.toFixed(2));
	var width = ctx.canvas.width;
	var height = ctx.canvas.height;
	var scale = 20;
	ctx.beginPath();
	ctx.lineWidth = 2;
	ctx.strokeStyle = "rgba(255,125,0,0.2)";
	
	var x = 4;
	var y = 0;
	var amplitude = 40;
	ctx.moveTo(x, 50);
	yy = "";
	while (x < width) {
		var dx = (x+xOffset)/frequency ;
		y = height/2 + amplitude * Math.sin(dx);
		y2 = 100 + (-x * 25 + ctx.canvas.width)    ;
		if (y < y2){
			y = y2;
		}
		if (x < 10) {
			ctx.moveTo(x,y);
		}
		ctx.lineTo(x, y);
		ctx.lineTo(x,ctx.canvas.height);
			
		x++;
	}
	ctx.stroke();
}
function draw() {
	var canvas = document.getElementById("canvas");
	var context = canvas.getContext("2d");
	context.clearRect(0, 0, 500, 500);
	plotSine(context, step, 50);
	step -= speed;
	
	window.requestAnimationFrame(draw);
}
function init() {
	window.requestAnimationFrame(draw);
}


document.onkeydown = checkKey;
function checkKey(e) {
    e = e || window.event;

	var sign = event.shiftKey ? 1 : -1;

	switch(e.keyCode){
		
		// R
		case 82: /* R */	rgb = 0;					break;		
		case 71: /* G */	rgb = 1;					break;		
		case 66: /* B */	rgb = 2;					break;

		case 49: /* 1 */	d1 += sign * 0.01;			break;	
		case 50: /* 2 */	d2 += sign * 0.1;			break;	
		case 51: /* 3 */	mode = 3;					break;	
		case 52: /* 4 */	mode = 4;					break;	
		case 53: /* 5 */	mode = 5;					break;	
		case 54: /* 6 */	mode = 6;					break;	
		case 55: /* 7 */	SetColor('rgb(205,85,0');	break;	
		case 56: /* 8 */	SetColor('rgb(185,65,0');	break;	
		case 57: /* 9 */	SetColor('rgb(255,0,255');	break;	
		case 48: /* 0 */	SetColor('rgb(125,0,125');	break;	
		default:
			break;
    }

}


