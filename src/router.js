import Vue from 'vue'
import Router from 'vue-router'

const PersonalCenter = () =>
    import('./views/PersonalCenter.vue')
const PersonalSetting = () =>
    import('./views/PersonalSetting.vue')
const SquareCenter = () =>
    import('./views/SquareCenter.vue')
const SquareInfo = () =>
    import('./views/SquareInfo.vue')


Vue.use(Router)

const routes = [{
        path: '/',
        alias: '/SquareCenter',
        name: 'SquareCenter',
        component: SquareCenter
    },
    {
        path: '/PersonalCenter',
        name: 'PersonalCenter',
        component: PersonalCenter
    },{
        path: '/PersonalSetting',
        name: 'PersonalSetting',
        component: PersonalSetting
    },{
        path: '/SquareInfo',
        name: 'SquareInfo',
        component: SquareInfo
    },

]

const router = new Router({
    //使用什么方式切换路由
    mode: 'history', //html5 API的history
    // base: process.env.BASE_URL,
    base: "/",
    routes
})

export default router;