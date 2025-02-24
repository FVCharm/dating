export default {
	debug: true,
	state: {
		is_authenticated: !!window.localStorage.getItem('dating-token'),
		// 用户登录后，就算刷新页面也能再次计算出 user_id
		user_id: window.localStorage.getItem('dating-token')
			? JSON.parse(
					atob(window.localStorage.getItem('dating-token').split('.')[1])
			  ).user_id
			: 0
	},
	loginAction() {
		if (this.debug) {
			console.log('loginAction triggered')
		}
		this.state.is_authenticated = true
		this.state.user_id = JSON.parse(
			atob(window.localStorage.getItem('dating-token').split('.')[1])
		).user_id
	},
	logoutAction() {
		if (this.debug) console.log('logoutAction triggered')
		window.localStorage.removeItem('dating-token')
		this.state.is_authenticated = false
		this.state.user_id = 0
	}
}
