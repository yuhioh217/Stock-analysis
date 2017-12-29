<template>
	<div class="table_content">
		<p class="tradingshort_title">融券大於3000張, 資券比 > 20%, 資券比 < 40% (有機會尬空股)</p>
		<div class="table1">
			<md-table>
			  <md-table-header>
			    <md-table-row>
				      <md-table-head>ID </md-table-head>
				      <md-table-head>Today (%)</md-table-head>
				      <md-table-head>YesterDay (%)</md-table-head>
				      <md-table-head>Diff (%)</md-table-head>
				      <md-table-head>Foreign Investors </md-table-head>
				      <md-table-head>Investment Trust </md-table-head>
				      <md-table-head>Dealer </md-table-head>
			    </md-table-row>
			  </md-table-header>

			  <md-table-body>
			    <md-table-row v-for="(item, index) in data.rankByPercent" :key="index">
			      <md-table-cell><a v-bind:href="link_rankByPercent[index]">{{item.id}}</a></md-table-cell>
			      <md-table-cell>{{item.one}}</md-table-cell>
			      <md-table-cell>{{item.two}}</md-table-cell>
			      <md-table-cell>{{item.dif}}</md-table-cell>
			      <md-table-cell>{{item.foreignInvestors}}</md-table-cell>
			      <md-table-cell>{{item.investmentTrust}}</md-table-cell>
			      <md-table-cell>{{item.dealer}}</md-table-cell>
			    </md-table-row>
			  </md-table-body>
			</md-table>
		</div>
		<p class="tradingshort_title">融券大於3000張, 資券比較昨天增加比例高於 2% (有機會尬空股)</p>
		<div class="table2">
			<md-table>
			  <md-table-header>
			    <md-table-row>
				      <md-table-head>ID </md-table-head>
				      <md-table-head>Today (%)</md-table-head>
				      <md-table-head>YesterDay (%)</md-table-head>
				      <md-table-head>Diff (%)</md-table-head>
				      <md-table-head>Foreign Investors </md-table-head>
				      <md-table-head>Investment Trust </md-table-head>
				      <md-table-head>Dealer </md-table-head>
			    </md-table-row>
			  </md-table-header>

			  <md-table-body>
			    <md-table-row v-for="(item, index) in data.rankByDiff" :key="index">
			      <md-table-cell><a v-bind:href="link_rankByDiff[index]">{{item.id}}</a></md-table-cell>
			      <md-table-cell>{{item.one}}</md-table-cell>
			      <md-table-cell>{{item.two}}</md-table-cell>
			      <md-table-cell>{{item.dif}}</md-table-cell>
			      <md-table-cell>{{item.foreignInvestors}}</md-table-cell>
			      <md-table-cell>{{item.investmentTrust}}</md-table-cell>
			      <md-table-cell>{{item.dealer}}</md-table-cell>
			    </md-table-row>
			  </md-table-body>
			</md-table>
		</div>
	</div>


</template>

<script>

	export default {
		name:'table-one',
		data(){
			return {
				data               : {},
				link_rankByPercent : [],
				link_rankByDiff    : []
			}
		},
		created : function(){
			this.getData();
		},
		methods : {
			getData(){

		      axios.get('http://localhost:3000/apis/home/table1/1/') //restful api to get the tradingshort database.
		      .then(response => {
		        this.data = response.data.data;
		        
		        for(var i=0;i<(this.data.rankByPercent).length;i++){  //rankByPercent
		        	(this.link_rankByPercent).push("https://statementdog.com/analysis/tpe/" + (this.data.rankByPercent)[i].id);
		        } // push the stock info link string to array.

		        for(var i=0;i<(this.data.rankByDiff).length;i++){     //rankByDiff
		        	(this.link_rankByDiff).push("https://statementdog.com/analysis/tpe/" + (this.data.rankByDiff)[i].id);
		        } // push the stock info link string to array.

		      })
		    }
		}

	}

</script>

<style>
.table2 {
	margin-top: 20px;
}

.table_content {
	margin-top: 20px;
}

.tradingshort_title {
	text-align: center;
	margin-top: 5px;
	margin-bottom: 5px;
}
</style>