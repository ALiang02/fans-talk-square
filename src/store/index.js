import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
	namespaced: true,
	state: {
		loading: false,
		imgNum: ""

	},
	mutations: {
		Loading_Change(state, val) {
			state.loading = val;
		},

		setBackImg(state, num) {
			state.imgNum = num;
			localStorage.setItem("imgNum",state.imgNum);
			document.body.style.backgroundImage =
				"url(" +"http://127.0.0.1/壁纸/images/" + num + ".png" + ")";
			console.log(document.body.style.backgroundImage.toString());
		}
	},
	
	
	
})
