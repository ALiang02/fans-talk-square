import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
	namespaced: true,
	state: {
		loading: false,
		imgSrc: "http://127.0.0.1/壁纸/images/"
	},
	mutations: {
		Loading_Change(state, val) {
			state.loading = val;
		},

		setBackImg(state, num) {
			document.body.style.backgroundImage =
				"url(" + state.imgSrc + num + ".png" + ")";
			console.log(document.body.style.backgroundImage.toString());
		}
	},
	actions: {

	},
	modules: {}
})
