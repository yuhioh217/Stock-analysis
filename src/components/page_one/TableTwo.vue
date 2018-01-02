<template>
	<div class="table_container">
		<canvas ref="canvas" width="900" height="400"></canvas>
	</div>
</template>

<script>
	import VueChartJs from 'vue-chartjs'

	export default {
		name:'table-two',
		extends: VueChartJs.Line,
		mounted () {
			this.renderChart({
			  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
			  datasets: [
			    {
			      label: '大盤指數',
			      backgroundColor: '#00AAAA',
			      data: [40, 39, 10, 40, 39, 80, 40]
			    }
			  ]
			}, {responsive: true, maintainAspectRatio: false})
		}

	} 
</script>

<style>
.table_container{height:300px; margin-top: 50px; margin-bottom: 50px;}
</style>