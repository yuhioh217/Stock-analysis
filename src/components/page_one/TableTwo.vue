<template>
	<div class="table_container">
		<canvas ref="canvas" width="900" height="400"></canvas>
		<vue-progress-bar></vue-progress-bar>
	</div>
</template>

<script>
	import VueChartJs from 'vue-chartjs'
	
	const S = require("string");



	export default {
		name:'table-two',
		extends: VueChartJs.Line,
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
			
			
			this.renderChart({
			  labels: this.dateArr,
			  datasets: [
			    {
			      label: '大盤指數',
			      backgroundColor: '#00AAAA',
			      data: this.endArr
			    }

			  ]
			}, {responsive: true, maintainAspectRatio: false})

		},
		watch: {
		    data: function () {
		      console.log("Reload data");
		     this.$data._chart.destroy();
		      this.renderChart({
				  labels: this.dateArr,
				  datasets: [
				    {
				      label: '大盤指數',
				      backgroundColor: '#00AAAA',
				      data: this.endArr
				    }

				  ]
				}, {responsive: true, maintainAspectRatio: false})
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
			}
		} 

	} 
</script>

<style>
.table_container{height:300px; margin-top: 50px; margin-bottom: 50px;}
</style>