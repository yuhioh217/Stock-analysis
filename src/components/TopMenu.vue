<template>
	<div>
		<div class="ui secondary  menu">
		  <a class="item" style="color:#fff">
		    Today Detail
		  </a>
		  <a class="item" style="color:#fff">
		    Data Analysis
		  </a>
		  <a class="item" style="color:#fff">
		    About
		  </a>
		  <div class="right menu">
		    <div class="item">
		      <div class="ui icon input">
		        <input type="text" placeholder="Search...">
		        <i class="search link icon"></i>
		      </div>
		    </div>
		    <a class="ui item">
		      Update
		    </a>
		  </div>
		</div>
		<div class="content">
			<chart-one/>
			<table-one/>
	  
			<pie-chart stockdown="YX" stockup="DD" downval=11 upval=4></pie-chart>
			<pie-chartcement stockdown="XX" stockup="DD" downval=10 upval=3></pie-chartcement>
			<pie-chartfood stockdown="XX" stockup="DD" downval=10 upval=3></pie-chartfood>

			
			
		</div>
	</div>
</template>

<script>
	import TableOne from './page_one/TableOne.vue'
	import ChartOne from './page_one/ChartOne.vue'
	import PieChart from './page_one/PieChart.vue'
	import PieChartcement from './page_one/PieChartcement.vue'
	import PieChartfood from './page_one/PieChartfood.vue'

	export default {
		name:'top-menu',
		data(){
			return {

			}
		},
		components : {
			ChartOne,
			TableOne,
			PieChart,
			PieChartcement,
			PieChartfood
		}
	}

</script>

<style>
	.content {
		
	}
</style>