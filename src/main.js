import Vue from 'vue'
import App from './App.vue'
import MuseUI from 'muse-ui'
import 'muse-ui/dist/muse-ui.css'
import 'muse-ui/dist/theme-light.css' // use carbon theme
import 'vue-material/dist/vue-material.css'

var VueMaterial = require('vue-material');
Vue.use(MuseUI);
Vue.use(VueResource);
Vue.use(VueMaterial);

const app = new Vue({
	el: 'app',
	components: { App }
})