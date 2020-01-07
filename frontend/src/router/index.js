import Vue from 'vue'
import VueRouter from 'vue-router'
import Ping from '@/views/test/Ping.vue'
import Test from '@/views/test/Test'
import Home from '@/views/Home'
import Login from '@/views/Login'
import Register from '@/views/Register'
import Profile from '@/views/Profile'
import Edit from '@/views/Edit'
import ResetPassword from '@/views/ResetPassword'

Vue.use(VueRouter)

const routes = [
	{
		path: '/ping',
		name: 'Ping',
		component: Ping
	},
	{
		path: '/test',
		name: 'Test',
		component: Test
	},
	{
		path: '/',
		name: 'Home',
		component: Home,
		meta: {
			requiresAuth: true
		}
	},
	{
		path: '/login',
		name: 'Login',
		component: Login
	},
	{
		path: '/register',
		name: 'Register',
		component: Register
	},
	{
		path: '/user/:id',
		name: 'Profile',
		component: Profile,
		meta: {
			requiresAuth: true
		}
	},
	{
		path: '/edit',
		name: 'Edit',
		component: Edit,
		meta: {
			requiresAuth: true
		}
	},
	{
		path: '/reset-password',
		name: 'ResetPassword',
		component: ResetPassword
	}
]

const router = new VueRouter({
	routes
})

router.beforeEach((to, from, next) => {
	const token = window.localStorage.getItem('dating-token')
	if (
		to.matched.some(record => record.meta.requiresAuth) &&
		(!token || token === null)
	) {
		next({
			path: '/login',
			query: { redirect: to.fullPath }
		})
	} else if (token && to.name === 'Login') {
		// 用户已登录，但又去访问登录页面时不让他过去
		next({
			path: from.fullPath
		})
	} else {
		next()
	}
})

export default router
