<template>
    <div class="chartWrapper">
      <div class="chartAreaWrapper">
        <div class="chartAreaWrapper2">
            <canvas id="myChart"></canvas>
        </div>
      </div>
      <vue-progress-bar></vue-progress-bar>  
      <canvas id="myChartAxis" height="300" width="0"></canvas>
    </div>
</template>

<script>
	import Chart from 'chart.js'
	const S = require("string");

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
			this.$Progress.start();
			this.getData();
		},
		mounted () {
			var chartOptions = {
					options: {
					  responsive: true,
					  maintainAspectRatio: false,
					  animation: {			            
				            onComplete: function(animation) {
						        var sourceCanvas = myLiveChart.chart.canvas;
		                        var copyWidth = myLiveChart.scales['y-axis-0'].width - 10;
		                        var copyHeight = myLiveChart.scales['y-axis-0'].height + myLiveChart.scales['y-axis-0'].top + 10;
		                        var targetCtx = document.getElementById("myChartAxis").getContext("2d");
		                        targetCtx.canvas.width = copyWidth;
		            		    targetCtx.drawImage(sourceCanvas, 0, 0, copyWidth, copyHeight, 0, 0, copyWidth, copyHeight);
				            }
				        }
					},
					type: 'line',
					data: {
						datasets: [
						    {
						        label: this.dateArr,
						        fillColor: "rgba(220,220,220,0.2)",
						        strokeColor: "rgba(220,220,220,1)",
						        pointColor: "rgba(220,220,220,1)",
						        pointStrokeColor: "#fff",
						        pointHighlightFill: "#fff",
						        pointHighlightStroke: "rgba(220,220,220,1)",
						        data: this.endArr
						    },

						]
			}};
			this.renderChart();
		},
		watch: {
		    data: function () {
				console.log("Reload data");

				this.renderChart();
			}
		},
		methods : {
			getData(){
				axios.get('http://localhost:3000/apis/home/market')
				.then(
					(response) => {
						this.data = response.data.data;
						//console.log('all have ' + (this.data).length + ' data');
						for(var i=((this.data).length)-100; i < (this.data).length;i++){
							this.dateArr.push((this.data)[i].date);
							this.endArr.push(S(S((this.data)[i].end).replaceAll(',','').s).toFloat());
							//console.log((this.data)[i]);
						}
						this.$Progress.finish();	
				},  (response) => {
						this.$Progress.failed();	
				})
			},

			renderChart(){
				var ctx = document.getElementById("myChart").getContext("2d");
				var chart = {
					options: {
					  responsive: true,
					  maintainAspectRatio: false,
					  animation: {			            
				            onComplete: function(animation) {
						        var sourceCanvas = myLiveChart.chart.canvas;
				                var copyWidth = myLiveChart.scales['y-axis-0'].width - 10;
				                var copyHeight = myLiveChart.scales['y-axis-0'].height + myLiveChart.scales['y-axis-0'].top + 10;
				                var targetCtx = document.getElementById("myChartAxis").getContext("2d");
				                targetCtx.canvas.width = copyWidth;
				    		    targetCtx.drawImage(sourceCanvas, 0, 0, copyWidth, copyHeight, 0, 0, copyWidth, copyHeight);
				            }
				        }
					},
					type: 'line',
					data: {
						datasets: [
						    {
						        label: this.dateArr,
						        fillColor: "rgba(220,220,220,0.2)",
						        strokeColor: "rgba(220,220,220,1)",
						        pointColor: "rgba(220,220,220,1)",
						        pointStrokeColor: "#fff",
						        pointHighlightFill: "#fff",
						        pointHighlightStroke: "rgba(220,220,220,1)",
						        data: this.endArr
						    },

						]
				}}
				var myLiveChart = new Chart(ctx, chart);
			}
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
          overflow-x: scroll;
            position: relative;
            width: 100%;
        }

        .chartAreaWrapper2 {
          
            position: relative;
            height: 300px;
        }
</style>