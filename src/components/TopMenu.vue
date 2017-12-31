<template>
	<div>
		<div class="ui secondary  menu">
		  <a class="item">
		    Today Detail
		  </a>
		  <a class="item">
		    Data Analysis
		  </a>
		  <a class="item">
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
			<table-one></table-one>
		</div>
	</div>
</template>

<script>
	import TableOne from './page_one/TableOne.vue'
	export default {
		name:'top-menu',
		data(){
			return {

			}
		},
		components : {
			TableOne
		}
	}

</script>

<style>
	.content {
		margin: 10px 20px 10px 20px;
	}
</style>