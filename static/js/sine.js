var d1 = 1.1;
var d2 = 0.5;
var speed = 0.2;
var frequency = 20;

function Lerp(fr,to,dt){
	var d = to - fr;
	fr += d * dt * dt;
	return fr;
}


$(document).ready(function(){
	init();
});
       function showAxes(ctx,axes) {
            var width = ctx.canvas.width;
            var height = ctx.canvas.height;
            var xMin = 0;
            
            ctx.beginPath();
            ctx.strokeStyle = "rgba(100,30,0,0.4)";
            
            // X-Axis
            ctx.moveTo(xMin, height/2);
            ctx.lineTo(width, height/2);
            
            // Y-Axis
            ctx.moveTo(width/2, 0);
            ctx.lineTo(width/2, height);
            // Starting line
            ctx.moveTo(0, 0);
            ctx.lineTo(0, height);
            
            ctx.stroke();
        }
        function drawPoint(ctx, y) {            
            var radius = 3;
            ctx.beginPath();
            // Hold x constant at 4 so the point only moves up and down.
            ctx.arc(4, y, radius, 0, 2 * Math.PI, false);
            ctx.fillStyle = 'red';
            ctx.fill();
            ctx.lineWidth = 1;
            ctx.stroke();
        }
        function plotSine(ctx, xOffset, yOffset) {
            var width = ctx.canvas.width;
            var height = ctx.canvas.height;
            var scale = 20;
            ctx.beginPath();
            ctx.lineWidth = 2;
            ctx.strokeStyle = "rgba(66,44,255,0.2)";
            // console.log("Drawing point...");
            // drawPoint(ctx, yOffset+step);
            
            var x = 4;
            var y = 0;
            var amplitude = 40;
            //ctx.moveTo(x, y);
            ctx.moveTo(x, 50);
			
            while (x < width) {
				// width is 500
				// x is zero to width
//                y = height/2 + amplitude * Math.sin(Math.sin(Math.pow(
//					(x+xOffset)/frequency,dt))+dt1);
				var dx = (x+xOffset)/frequency ;
                y = height/2 + amplitude * Math.sin(Math.pow(d1,dx - d2));
/*
				if (dn < 0.1){
					if (n1 > n2) {
						frequency -= dn;
//						frequency = Math.pow(frequency,1.001);
					} else {
						frequency += dn;
						//frequency = Math.pow(frequency,0.999);

					}
				} else {
					if (frequency > origFrequency) {
						frequency -= frst;
					} else {
						frequency += frst;
	
					}
//						frequency = origFrequency; //Lerp(frequency,origFrequency,0.1);
				}
*/
				// if focus is 0, n is 500
				// if focus is 1, n is 250
				// if focus is 2, n is 250
//				if (x < width * (focus + 1)/4)  frequency = Math.pow(frequency,0.999);
//				else if (x < width * (focus + 2)/4) frequency = frequency;
//				else  frequency = Math.pow(frequency,1.001);
					
                ctx.lineTo(x, y);
				ctx.lineTo(x,ctx.canvas.height);
				x++;
//				step1 += stepm;
//                x+= 1 * step1;
//                console.log("x="+x+" y="+y);
            }
            ctx.stroke();
            ctx.save();
//            console.log("Drawing point at y=" + y);
            drawPoint(ctx, y);
            ctx.stroke();
            ctx.restore();
        }
        function draw() {
			frequency = 20;
            var canvas = document.getElementById("canvas");
            var context = canvas.getContext("2d");
            context.clearRect(0, 0, 500, 500);
            showAxes(context);
            context.save();            
            
            plotSine(context, step, 50);
            context.restore();
			step += speed;
			// step1 += step1m; 
//            step += speed + step1;
            window.requestAnimationFrame(draw);
        }
//        function spirograph() {            
//            var canvas2 = document.getElementById("canvas2");
//            var context = canvas2.getContext("2d");
//            
//            showAxes(context);
//            context.save();
//            // var imageData = context.getImageData(0, 0, canvas.width, canvas.height);
//            var step = 4;
//            for (var i = -4; i < canvas.height; i += step) {
//                // context.putImageData(imageData, 0, 0);
//                plotSine(context, i, 54 + i);
//            }
//        }
        function init() {
            window.requestAnimationFrame(draw);
            //spirograph();
        }
        var step = -4;
