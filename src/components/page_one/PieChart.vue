<template>
	<div id="piechart"></div>
</template>

<script>

	const S = require("string");
	export default {
		name:'pie-chart',
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
			var chart = AmCharts.makeChart( "piechart", {
				"type": "pie",
				"theme": "light",
				"dataProvider": [{
					"Stock": "Ireland",
					"value": 0
					}, {
					"Stock": "Germany",
					"value": 0
					}, {
					"Stock": "泥尼: 0.25% down\n雅妮: 0.55% down\n跌家",						
					"value": 3
					}, {
					"Stock": "台泥: 0.85% up\n亞泥: 2.00% up\n漲家",
					"value": 10
					}, {
					"Stock": "Latvia",
					"value": 0
					},
					 {
					"Stock": "Lithuania",
					"value": 0
					}
				],
				"valueField": "value",
				"titleField": "Stock",
				"outlineAlpha": 0.4,
				"depth3D": 15,
				"balloonText": "[[title]]<br><span style='font-size:14px'><b>[[value]]</b> ([[percents]]%)</span>",
				"angle": 30,
				"export": {
				"enabled": true
				}
			} );
	

		},
		

		methods : {
	

		} 

	} 
</script>

<style>
#piechart {
	margin-top:20px;
	margin-right: 10px;
	margin-left: 10px;
	width: 100%;
	height: 500px;
}		
</style>