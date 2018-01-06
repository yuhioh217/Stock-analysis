import Vue from 'vue'
import App from './App.vue'
import MuseUI from 'muse-ui'
import 'muse-ui/dist/muse-ui.css'
import 'muse-ui/dist/theme-light.css' // use carbon theme
import 'vue-material/dist/vue-material.css'
import VueProgressBar from 'vue-progressbar'

var VueMaterial = require('vue-material');
Vue.use(MuseUI);
Vue.use(VueResource);
Vue.use(VueMaterial);
const options = {
  color: '#bffaf3',
  failedColor: '#874b4b',
  thickness: '5px',
  transition: {
    speed: '0.2s',
    opacity: '0.6s',
    termination: 300
  },
  autoRevert: true,
  location: 'left',
  inverse: false
}

Vue.use(VueProgressBar, options)

const app = new Vue({
	el: 'app',
	components: { App }
})