<template>
	<div id="piechartcement"></div>
</template>

<script>

	const S = require("string");
	export default {
		name:'pie-chartcement',
		props: ['stockup','stockdown','upval','downval'],
		data () {
			return {
				data    : {},
				dateArr : [],
				endArr  : []
			}
		},
		created () {
			console.log("----" + this.stockup);
		},

		mounted () {
			var chart = AmCharts.makeChart( "piechartcement", {
				"type": "pie",
				"theme": "black",
				"dataProvider": [{
					"Stock": this.stockdown,//"泥尼: 0.25% down\n雅妮: 0.55% down\n跌家",						
					"value": this.downval//3
					}, {
					"Stock": "Germany",
					"value": 0
					}, {
					"Stock": "Ireland",
					"value": 0
					}, {
					"Stock": "Latvia",
					"value": 0
					}, {
					"Stock": this.stockup,//"台泥: 0.85% up\n亞泥: 2.00% up\n漲家",
					"value": this.upval//10
					},
					 {
					"Stock": "Lithuania",
					"value": 0
					}
				],
				"valueField": "value",
				"titleField": "Stock",
				"outlineAlpha": 0.6,
				"depth3D": 15,
				"balloonText": "[[title]]<br><span style='font-size:14px;'><b>[[value]]</b> ([[percents]]%)</span>",
				"angle": 42.6,
				"export": {
				"enabled": false
				}
			} );
		},
		methods : {
	

		} 

	} 
</script>

<style>
#piechartcement {
	margin-top:20px;
	margin-right: 10px;
	margin-left: 10px;
	width: 100%;
	height: 500px;
}

.cementchart {
	background-color: #000;
}
</style>