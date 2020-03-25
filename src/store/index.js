import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
	namespaced: true,
	state: {
		loading: false,
		imgNum: "",
		
		

	},
	mutations: {
		Loading_Change(state, val) {
			state.loading = val;
		},

		setBackImg(state, num) {
			state.imgNum = num;
			localStorage.setItem("imgNum",state.imgNum);
			document.body.style.backgroundImage =
				"url(" +"http://118.178.94.45:8080/壁纸/images/" + num + ".png" + ")";
			
		},

		
	},
	
	
	
})
