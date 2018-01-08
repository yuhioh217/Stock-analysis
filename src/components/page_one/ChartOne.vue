<template>
	<div id="chartdiv"></div>
</template>

<script>

	const S = require("string");
	export default {
		name:'chart-one',
		data () {
			return {
				data    : {},
				dateArr : [],
				endArr  : []
			}
		},
		created () {
			this.getData();
		},

		mounted () {
			
					

		},
		

		methods : {
			getData(){
				axios.get('http://localhost:3000/apis/home/market')
				.then(
					(response) => {
						this.data = response.data.data;
						//console.log('all have ' + (this.data).length + ' data');
						for(var i=0; i < (this.data).length;i++){
							this.dateArr.push((this.data)[i].date);
							this.endArr.push(S(S((this.data)[i].end).replaceAll(',','').s).toFloat());
							//console.log((this.data)[i]);
						}
						this.$Progress.finish();


						var chartData = this.generateChartData();
						var chart = AmCharts.makeChart("chartdiv", {
						"type": "serial",
						"theme": "light",
						"marginRight": 80,
						"autoMarginOffset": 20,
						"marginTop": 7,
						"dataProvider": chartData,
						"valueAxes": [{
						    "axisAlpha": 0.2,
						    "dashLength": 1,
						    "position": "left"
						}],
						"mouseWheelZoomEnabled": true,
						"graphs": [{
						    "id": "g1",
						    "balloonText": "[[value]]",
						    "bullet": "round",
						    "bulletBorderAlpha": 1,
						    "bulletColor": "#FFFFFF",
						    "hideBulletsCount": 50,
						    "title": "red line",
						    "valueField": "visits",
						    "useLineColorForBulletBorder": true,
						    "balloon":{
						        "drop":true
						    }
						}],
						"chartScrollbar": {
						    "autoGridCount": true,
						    "graph": "g1",
						    "scrollbarHeight": 40
						},
						"chartCursor": {
						   "limitToGraph":"g1"
						},
						"categoryField": "date",
						"categoryAxis": {
						    "parseDates": true,
						    "axisColor": "#DADADA",
						    "dashLength": 1,
						    "minorGridEnabled": true
						},
						"export": {
						    "enabled": true
						}
					});
					chart.addListener("rendered", this.zoomChart(chart,chartData));
					this.zoomChart(chart, chartData);	
				},  (response) => {
						this.$Progress.failed();	
				})
			},
			zoomChart(chart,chartData) {
			    // different zoom methods can be used - zoomToIndexes, zoomToDates, zoomToCategoryValues
			    chart.zoomToIndexes(chartData.length - 40, chartData.length - 1);
			},
			generateChartData() {
			    var chartData = [];

			    for (var i = 0; i < (this.endArr).length; i++) {
			        var newDate = new Date();
			        console.log('dateArr : '  + this.dateArr[i]);
			        var year = S(S(this.dateArr[i]).splitLeft('/')[0]).toInt();
			        var month = S(S(this.dateArr[i]).splitLeft('/')[1]).toInt();
			        var day = S(S(this.dateArr[i]).splitLeft('/')[2]).toInt();

			        newDate.setYear(year + 1911);
			        newDate.setMonth(month - 1);
			        newDate.setDate(day);
			        chartData.push({
			            date: newDate,
			            visits: this.endArr[i]
			        });
			    }
			    return chartData;
			}

		} 

	} 
</script>

<style>
#chartdiv {
	margin-top: 100px;
	width	: 100%;
	height	: 500px;
}		
</style>