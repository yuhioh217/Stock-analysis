<template>
	<div class="chartWrapper">
	    <div class="chartAreaWrapper">
	        <canvas id="myChart" height="300" width="1200"></canvas>
	    </div>
	    <canvas id="myChartAxis" height="300" width="0"></canvas>
	</div>
</template>

<script>
	import Chart from 'chart.js'

	export default {
		name: 'scrollable-chart',
		data () {
			return {
				data    : {},
				dateArr : [],
				endArr  : []
			}
		},
		created () {

		},
		mounted () {
			var ctx = document.getElementById("myChart").getContext("2d");
			var data = {
			    labels: ["January", "February", "March", "April", "May", "June", "July"],
			    datasets: [
			        {
			            label: "My First dataset",
			            fillColor: "rgba(220,220,220,0.2)",
			            strokeColor: "rgba(220,220,220,1)",
			            pointColor: "rgba(220,220,220,1)",
			            pointStrokeColor: "#fff",
			            pointHighlightFill: "#fff",
			            pointHighlightStroke: "rgba(220,220,220,1)",
			            data: [65, 59, 80, 81, 56, 55, 40]
			        },
			        {
			            label: "My Second dataset",
			            fillColor: "rgba(151,187,205,0.2)",
			            strokeColor: "rgba(151,187,205,1)",
			            pointColor: "rgba(151,187,205,1)",
			            pointStrokeColor: "#fff",
			            pointHighlightFill: "#fff",
			            pointHighlightStroke: "rgba(151,187,205,1)",
			            data: [28, 48, 40, 19, 86, 27, 90]
			        }
			    ]
			};	
			new Chart(ctx,{
				type:"line",
				data:data,
				option:{
				    onAnimationComplete: function () {
				        var sourceCanvas = this.chart.ctx.canvas;
				        var copyWidth = this.scale.xScalePaddingLeft - 5;
				        // the +5 is so that the bottommost y axis label is not clipped off
				        // we could factor this in using measureText if we wanted to be generic
				        var copyHeight = this.scale.endPoint + 5;
				        var targetCtx = document.getElementById("myChartAxis").getContext("2d");
				        targetCtx.canvas.width = copyWidth;
				        targetCtx.drawImage(sourceCanvas, 0, 0, copyWidth, copyHeight, 0, 0, copyWidth, copyHeight);
				    },
				    responsive: true, maintainAspectRatio: false
				}
			});
		}
	} 
</script>

<style>
.chartWrapper {
    position: relative;
}

.chartWrapper > canvas {
    position: absolute;
    left: 0;
    top: 0;
    pointer-events:none;
}

.chartAreaWrapper {
    width: 600px;
    overflow-x: scroll;
}
</style>