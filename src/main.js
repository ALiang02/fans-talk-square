import Vue from 'vue'
import App from './App.vue'
import ElenmentUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import router from "./router";
import store from "./store"
import Vuex from 'vuex'
import './assets/backg.css'





Vue.use(Vuex)

Vue.use(ElenmentUI);
Vue.config.productionTip = false

new Vue({
	store,
	router,
	render: h => h(App),
}).$mount('#app')
