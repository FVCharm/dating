import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap-material-design/dist/css/bootstrap-material-design.css'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme/index.css'
import axios from './http'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.prototype.$axios = axios

new Vue({
	router,
	render: h => h(App)
}).$mount('#app')
