<template>
  <div class="container">
    <h1>重置您的密码</h1>
    <el-row style="margin-top: 50px">
      <el-col :span="6" :offset="9">
        <form @submit.prevent="onSubmit">
          <div class="form-group" v-bind:class="{'u-has-error-v1': resetPasswordForm.passwordError}">
            <label for="password">新密码</label>
            <input type="password" v-model="resetPasswordForm.password" class="form-control" id="password" placeholder="">
            <small class="form-control-feedback" v-show="resetPasswordForm.passwordError">{{ resetPasswordForm.passwordError }}</small>
          </div>
          <button type="submit" class="btn btn-primary">点击重置</button>
        </form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'ResetPassword', // this is the name of the component
  data () {
    return {
      resetPasswordForm: {
        password: '',
        errors: 0, // 表单是否在前端验证通过，0 表示没有错误，验证通过
        passwordError: null
      }
    }
  },
  methods: {
    onSubmit (e) {
      this.resetPasswordForm.errors = 0 // 重置
      if (!this.resetPasswordForm.password) {
        this.resetPasswordForm.errors++
        this.resetPasswordForm.passwordError = '必须填写新密码.'
      } else {
        this.resetPasswordForm.passwordError = null
      }
      if (this.resetPasswordForm.errors > 0) {
        // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
        return false
      }
      const token = this.$route.query.token
      const path = `/reset-password/${token}`
      const payload = {
        password: this.resetPasswordForm.password
      }
      this.$axios.post(path, payload)
        .then((response) => {
          // handle success
          this.$message({
            showClose: true,
            message: '发送成功，请查收邮箱',
            type: 'success',
            center: true
          })
          this.$router.push('/login')
        })
        .catch((error) => {
          // handle error
          console.log(error.response.data)
          this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })
    }
  }
}
</script>
