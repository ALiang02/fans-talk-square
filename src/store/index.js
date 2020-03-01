import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
	namespaced: true,
	state: {
		loading : false
	},
	mutations: {
		Loading_Change(state,val){			
			state.loading = val;
		}
	},
	actions: {
		
	},
	modules: {}
})
