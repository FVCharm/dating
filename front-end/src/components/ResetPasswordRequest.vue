<template>
  <div class="container">
    <h1>重置你的密码</h1>
    <el-row style="margin-top: 40px">
      <el-col :span="6" :offset="9">
        <form @submit.prevent="onSubmit">
          <div class="form-group" v-bind:class="{'u-has-error-v1': resetPasswordForm.emailError}" >
            <label for="email">邮箱地址</label>

            <input type="email" v-model="resetPasswordForm.email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="">
             <label for="phone">手机号</label>
             <input v-model="resetPasswordForm.phone" class="form-control" id="phone" placeholder="">
            <small class="form-control-feedback" v-show="resetPasswordForm.emailError">{{ resetPasswordForm.emailError }}</small>

          <button type="submit" class="btn btn-primary">重置密码</button>
          </div>
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
        email: '',
        phone: '',
        errors: 0, // 表单是否在前端验证通过，0 表示没有错误，验证通过
        emailError: null
      }
    }
  },
  methods: {
    onSubmit (e) {
      this.resetPasswordForm.errors = 0 // 重置
      if (!this.resetPasswordForm.email) {
        this.resetPasswordForm.errors++
        this.resetPasswordForm.emailError = '必须填写邮箱.'
      } else if (!this.validEmail(this.resetPasswordForm.email)) {
        this.resetPasswordForm.errors++
        this.resetPasswordForm.emailError = '邮箱格式错误.'
      } else {
        this.resetPasswordForm.emailError = null
      }
      if (this.resetPasswordForm.errors > 0) {
        // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
        return false
      }
      const path = '/reset-password-request'
      const payload = {
        confirm_email_base_url: window.location.href.split('/', 4).join('/') + '/reset-password/?token=',
        email: this.resetPasswordForm.email,
        phone: this.resetPasswordForm.phone
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

          this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })
    },
    validEmail: function (email) {
      /* eslint-disable no-useless-escape */
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      return re.test(email)
    }
  }
}
</script>
