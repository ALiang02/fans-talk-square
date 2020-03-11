import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'


const PersonalCenter = () =>
	import('../views/PersonalCenter.vue')
const PersonalSetting = () =>
	import('../views/PersonalSetting.vue')
const SquareCenter = () =>
	import('../views/SquareCenter.vue')
const SquareInfo = () =>
	import('../views/SquareInfo.vue')
const SquareLive = () =>
	import('../views/SquareLive.vue')
const SquareWallPaper = () =>
	import('../views/SquareWallPaper.vue')


Vue.use(Router)

const routes = [{
		path: '/',
		alias: '/SquareCenter',
		name: 'SquareCenter',
		component: SquareCenter
	}, {
		path: '/PersonalCenter',
		name: 'PersonalCenter',
		component: PersonalCenter
	}, {
		path: '/PersonalSetting',
		name: 'PersonalSetting',
		component: PersonalSetting
	}, {
		path: '/SquareInfo',
		name: 'SquareInfo',
		component: SquareInfo
	},{
		path: '/SquareLive',
		name: 'SquareLive',
		component: SquareLive
	},{
		path: '/SquareWallPaper',
		name: 'SquareWallPaper',
		component: SquareWallPaper
	},

]

const router = new Router({
	//使用什么方式切换路由
	mode: 'hash', //html5 API的history
	// base: process.env.BASE_URL,
	base: "/",
	routes
})

router.beforeEach((to,from,next) => {
	store.commit("Loading_Change",true);	
	setTimeout(() => {next();},1000)
})

router.afterEach(() => {
	store.commit("Loading_Change",false);
})


export default router;
