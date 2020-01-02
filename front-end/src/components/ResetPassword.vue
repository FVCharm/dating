<template>
    <div>
    <el-row class="passwordForm">
        <el-col :offset="1" :span="22">
            <el-card shadow="hover">
            <div slot="header" style="text-align:center">修改密码</div>
            <div>
                <el-steps
                :active="activeStep"
                finish-status="success"
                process-status="finish"
                >
                <el-step icon="el-icon-position" title="手机验证"></el-step>
                <el-step icon="el-icon-unlock" title="修改密码"></el-step>
                <el-step icon title="完成"></el-step>
                </el-steps>
            </div>
            <el-row justify="center" type="flex">
                <el-form
                :model="codeForm"
                ref="codeForm"
                label-width="100px"
                v-if="activeStep === 0"
                :rules="rules"
                >
                <el-form-item label="手机号" style="margin-top: 20px;" prop="phone">
                    <el-input v-model.number="codeForm.phone"></el-input>
                    <el-button v-model.number="codeForm.phone" @click="sendCode(codeForm)" :style="{ marginLeft: '20px' }">发送验证码</el-button>
                </el-form-item>
                <el-form-item label="验证码" prop="verCode">
                    <el-input v-model.number="codeForm.verCode"></el-input>
                </el-form-item>
                <div align="center">
                    <el-button @click="nextStep1('codeForm')" style="margin-top: 12px;">下一步</el-button>

                </div>
                </el-form>
                <el-form
                :model="passwordForm"
                label-width="100px"
                ref="passwordForm"
                style="margin: 16px 0;"
                v-else-if="activeStep === 1"
                :rules="rules"
                >
                    <el-form-item label="新密码" style="margin-top: 20px;" prop="newPassword">
                        <el-input v-model="passwordForm.newPassword"></el-input>
                    </el-form-item>
                    <el-form-item label="确认密码" prop="newPassword2">
                        <el-input v-model="passwordForm.newPassword2"></el-input>
                    </el-form-item>
                    <div align="center">
                        <el-button @click="nextStep2('passwordForm')" style="margin-top: 12px;">下一步</el-button>
                    </div>
                </el-form>
                <el-form label-width="100px" v-else>
                <el-alert
                    center
                    show-icon
                    style="padding: 10px 30px; margin: 24px 0;"
                    title="密码修改成功"
                    type="success"
                ></el-alert>
                <div align="center">
                    <el-button @click="nextStep3" style="margin-top: 12px;">完成</el-button>
                </div>
                </el-form>
            </el-row>
            </el-card>
        </el-col>
        </el-row>
    </div>
</template>

<script>
export default {
  data () {
    var checkCode = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('验证码不能为空'))
      }
      setTimeout(() => {
        if (!Number.isInteger(value)) {
          callback(new Error('请输入数字'))
        } else {
          if (value !== this.codeForm.code) {
            callback(new Error('请输入正确的验证码'))
          } else {
            callback()
          }
        }
      }, 1000)
    }
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
    var checkPass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.passwordForm.newPassword2 !== '') {
          this.$refs.passwordForm.validateField('newPassword2')
        }
        callback()
      }
    }
    var checkPass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.passwordForm.newPassword) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      activeStep: 0,
      codeForm: {
        phone: '',
        verCode: '',
        code: ''
      },
      passwordForm: {
        newPassword: '',
        newPassword2: ''
      },
      rules: {
        phone: [
          { validator: checkPhone, trigger: 'blur' }
        ],
        newPassword: [
          { validator: checkPass, trigger: 'blur' },
          { min: 6, message: '密码长度至少为6位', trigger: 'blur' }
        ],
        newPassword2: [
          { validator: checkPass2, trigger: 'blur' }
        ],
        verCode: [
          { validator: checkCode, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    sendCode (formName) {
      // eslint-disable-next-line standard/object-curly-even-spacing
      const path = '/send-code'
      const payload = {
        phone: Number(this.codeForm.phone)
      }
      this.$axios.post(path, payload)
        .then((response) => {
          console.log(response.data)
          if (response.data.error_code === 0) {
            this.codeForm.code = response.data.code
            this.$message({
              showClose: true,
              message: '短信已发送，请注意查收',
              type: 'info',
              duration: 5000,
              center: true
            })
          }
        })
        .catch((error) => {
          console.log(error.response)
          if (error.response.data.error_code === 1002) {
            this.$message({
              showClose: true,
              message: '短信发送过于频繁，请稍后再试',
              type: 'error',
              duration: 5000,
              center: true
            })
          } else if (error.response.data.error_code === 1006) {
            this.$message({
              showClose: true,
              message: '该手机号尚未注册，请输入正确的手机号',
              type: 'error',
              duration: 5000,
              center: true
            })
          } else if (error.response.data.error_code === 999) {
            this.$message({
              showClose: true,
              message: '短信功能异常，请联系客服',
              type: 'warning',
              duration: 5000,
              center: true
            })
          }
        })
    },
    nextStep1 (formName) {
      console.log(formName)
      this.$refs[formName].validateField('verCode', (valid) => {
        console.log(valid)
        if (valid === '') {
          if (this.activeStep++ > 2) this.activeStep = 0
          this.$message({
            showClose: true,
            message: '验证成功，请填写新密码',
            type: 'success',
            center: true
          })
        } else {
          this.$message({
            showClose: true,
            message: '验证码错误，请输入正确的验证码',
            type: 'error',
            center: true
          })
        }
      })
    },
    nextStep2 (formName) {
      console.log(formName)
      this.$refs[formName].validateField(['newPassword', 'newPassword2'], (valid) => {
        const path = '/reset-pw'
        const payload = {
        //   phone: Number(this.codeForm.phone),
          phone: 13823332664,
          password: this.passwordForm.newPassword
        }
        this.$axios.post(path, payload)
          .then((response) => {
            this.$message({
              showClose: true,
              message: '密码修改成功',
              type: 'success',
              center: true
            })
            // 验证成功
            if (this.activeStep++ > 2) this.activeStep = 0
          })
          .catch((error) => {
            if (error) {
              this.$message({
                showClose: true,
                message: '未知错误',
                type: 'info',
                duration: 5000,
                center: true
              })
            }
          })
        console.log('valid: ' + valid)
      })
    },
    nextStep3 () {
      if (this.activeStep++ > 2) this.activeStep = 3
    }
  }

}
</script>

<style scoped>
.passwordForm {
    background-color: black;
    display: flex;
    align-items: center;
    width: 1120px;
    }
</style>
