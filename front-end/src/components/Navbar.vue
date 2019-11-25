<template>
  <nav class="navbar navbar-expand-lg navbar-dark" style="margin-bottom: 20px; background-color: #FF7D9B">
    <div class="container">
      <router-link to="/" class="navbar-brand">
        <img src="../assets/logo.png" width="36" height="36" class="d-inline-block align-top" alt="">
      </router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul v-if="sharedState.is_auth" class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item active">
            <router-link to="/" class="nav-link">首页 <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link " href="#">推荐</a>
          </li>
          <li class="nav-item">
            <a class="nav-link " href="#">认证</a>
          </li>
        </ul>

        <ul v-else class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item active">
            <router-link to="/" class="nav-link">首页 <span class="sr-only">(current)</span></router-link>
          </li>
        </ul>

        <ul v-if="sharedState.is_auth" class="nav navbar-nav navbar-right">
          <li class="nav-item">
            <a class="nav-link disabled" href="#"><i class="el-icon-message"></i></a>
          </li>
          <li class="nav-item">
            <router-link v-bind:to="{ name: 'Profile', params: { id: sharedState.user_id }}" class="nav-link">Profile</router-link>
          </li>
          <li class="nav-item">
            <a v-on:click="logout" class="nav-link" href="#"></a>
          </li>
        </ul>
        <ul v-else class="nav navbar-nav navbar-right">
          <li class="nav-item">
            <router-link to="/login" class="nav-link">登录</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import store from '../store'
export default {
  name: 'Navbar',
  data () {
    return {
      sharedState: store.state
    }
  },
  methods: {
    logout (e) {
      store.logoutAction()
      this.$router.push('login')
    }
  }
}
</script>

<style scoped>

</style>
