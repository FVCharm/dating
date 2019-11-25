export default {
  debug: true,
  state: {
    is_new: false,
    is_auth: !!window.localStorage.getItem('dating-token')
  },
  setNewAction () {
    if (this.debug) {
      console.log('setNewAction triggered')
    }
    this.state.is_new = true
  },
  resetNotNewAction () {
    if (this.debug) {
      console.log('resetNotNewAction triggered')
    }
    this.state.is_new = false
  },
  loginAction () {
    if (this.debug) {
      console.log('loginAction triggered')
    }
    this.state.is_auth = true
  },
  logoutAction () {
    if (this.debug) {
      console.log('logoutAction triggered')
    }
    this.state.is_auth = false
  }
}
