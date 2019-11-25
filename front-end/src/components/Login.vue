<template>
  <el-container>
    <el-main>
      <alert
        v-if="sharedState.is_new"
        v-bind:variant="alertVariant"
        v-bind:message="alertMessage">
      </alert>
      <section class="loginSection">
        <el-row>
          <el-col
            :xs="{ span: 12, offset: 6 }"
            :sm="{ span: 10, offset: 7 }"
            :md="{ span: 7, offset: 12 }"
            :lg="{ span: 5, offset: 14 }"
          >
            <el-card style="margin-top:80px; ">
              <div slot="header" style="text-align: center;">登录</div>
              <el-col>
                <el-form
                  :model="loginForm"
                  :rules="rules"
                  ref="loginForm"
                  status-icon
                  style="margin-bottom: 12px;"
                >
                  <el-form-item prop="phone">
                    <el-input
                      placeholder="请输入手机号"
                      v-model.number="loginForm.phone"
                    ></el-input>
                  </el-form-item>
                  <el-form-item prop="pass">
                    <el-input
                      autocomplete="off"
                      placeholder="请输入密码"
                      type="password"
                      v-model="loginForm.pass"
                    ></el-input>
                  </el-form-item>
                  <el-row>
                    <el-col :span="12">
                      <div style="text-align: left;">
                        <router-link
                          :underline="false"
                          tag="el-link"
                          to="/register"
                          type="primary"
                          >忘记密码？</router-link
                        >
                      </div>
                    </el-col>
                    <el-col :span="12">
                      <div style="text-align: right;">
                        <router-link
                          :underline="false"
                          tag="el-link"
                          to="/register"
                          type="primary"
                          >现在注册</router-link
                        >
                      </div>
                    </el-col>
                  </el-row>
                  <el-form-item style="margin-top: 12px; margin-bottom: 0;">
                    <el-button @click="submitForm('loginForm')" type="primary"
                      >登录</el-button
                    >
                  </el-form-item>
                </el-form>
                <!--                <hr style="border-width: 0.5px; margin: 12px 0 16px;" />-->
                <el-row style="margin-bottom: 8px;">
                  <el-col
                    :span="10"
                    style="margin-bottom: 4px; text-align: left;"
                  >
                    <router-link tag="el-link" to="/" type="primary"
                      >游客登录</router-link
                    >
                  </el-col>
                  <el-col :span="14">
                    <div style="text-align: right">
                      <span style="font-size: 14px; color: #52575d;"
                        >其他登录方式：</span
                      >
                      <el-link>
                        <el-image
                          :src="require('../assets/icons/wechat.png')"
                          style="width:26px; height:26px;vertical-align:middle;"
                        ></el-image>
                      </el-link>
                    </div>
                  </el-col>
                </el-row>
              </el-col>
            </el-card>
          </el-col>
        </el-row>
      </section>
    </el-main>
  </el-container>
</template>

<script>
import Alert from './Alert'
import store from '../store'
import axios from 'axios'
export default {
  name: 'login',
  components: {
    alert: Alert
  },
  data () {
    var checkPhone = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('手机号不能为空'))
      }
      setTimeout(() => {
        if (!Number.isInteger(value)) {
          callback(new Error('请输入数字'))
        } else {
          if (value < 10000000000 || value > 99999999999) {
            callback(new Error('请输入正确的手机号'))
          } else {
            callback()
          }
        }
      }, 1000)
    }
    return {
      sharedState: store.state,
      alertVariant: 'info',
      alertMessage: '恭喜注册成功！',
      loginForm: {
        phone: '',
        pass: ''
      },
      rules: {
        phone: [{ validator: checkPhone, trigger: 'blur' }],
        pass: [{ required: true, message: '请输入密码', trigger: 'blur' }]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          const path = 'http://localhost:5000/v1/tokens'
          axios.post(path, {}, {
            auth: {
              'username': this.loginForm.phone.toString(),
              'password': this.loginForm.pass
            }
          }).then((response) => {
            window.localStorage.setItem('dating-token', response.data.token)
            store.resetNotNewAction()
            store.loginAction()

            if (typeof this.$route.query.redirect === 'undefined') {
              this.$router.push('/')
            } else {
              this.$router.push(this.$route.query.redirect)
            }
          }).catch((error) => {
            // eslint-disable-next-line eqeqeq
            console.log(error.response)
          })
          alert('登录提交成功！')
        } else {
          console.log('提交失败！！')
          return false
        }
      })
    }
  }
}
</script>

<style scoped></style>
