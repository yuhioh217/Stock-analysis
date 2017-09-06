<template>
	<div id="app">
		<icon-menu></icon-menu>
		<three-tabs></three-tabs>
		<five-day></five-day>
		<back-top></back-top>
	</div>
</template>

<script>
	import IconMenu from './components/IconMenu.vue'
	import ThreeTabs from './components/ThreeTabs.vue'
	import FiveDay from './components/FiveDay.vue'
	import BackTop from './components/BackTop.vue'
	export default{
		data() {
			return {
			
			}
		},
		components : {
			IconMenu,
			ThreeTabs,
			FiveDay,
			BackTop
		}
	}
</script>

<style>
	body {
		font-family: Helvetica, sans-serif;
	}
</style>