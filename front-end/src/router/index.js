import Vue from 'vue'
import VueRouter from 'vue-router'
import Ping from '../components/Ping.vue'
import Test from '../components/Test'
import Home from '../components/Home'
import Login from '../components/Login'
import Register from '../components/Register'
import Profile from '../components/Profile'
import Edit from '../components/Edit'
import EditProfile from '../components/EditProfile'
import ResetPasswordRequest from '@/components/ResetPasswordRequest'
import ResetPassword from '@/components/ResetPassword'

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
    // 用户修改自己的个人信息
    path: '/edit-profile',
    name: 'EditProfile',
    component: EditProfile,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/reset-password-request',
    name: 'ResetPasswordRequest',
    component: ResetPasswordRequest
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
  if (to.matched.some(record => record.meta.requiresAuth) && (!token || token === null)) {
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
