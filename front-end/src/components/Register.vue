<template>
  <el-container>
    <el-main>
      <el-row>
        <el-col :span="24" style="max-width: 370px;">
          <el-tag style="font-size: 18px;margin: 36px 40px 20px;" effect="dark">注册账号</el-tag>
          <el-form
            :model="registerForm"
            :rules="rules"
            label-width="140px"
            ref="registerForm"
            status-icon
          >
            <el-form-item label="昵称" prop="name" required>
              <el-input v-model="registerForm.name"></el-input>
            </el-form-item>
            <el-form-item label="手机号" prop="phone" required>
              <el-input v-model.number="registerForm.phone"></el-input>
            </el-form-item>
            <el-form-item label="验证码" prop="verCode" required>
              <el-input v-model.number="registerForm.verCode"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="pass" required>
              <el-input autocomplete="off" type="password" v-model="registerForm.pass"></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="pass2" required>
              <el-input autocomplete="off" type="password" v-model="registerForm.pass2"></el-input>
            </el-form-item>
            <el-form-item>
<!--              <el-button @click="resetForm('registerForm')">发送验证码</el-button>-->
              <el-button @click="submitForm('registerForm')" type="primary">提交</el-button>
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import axios from 'axios'
import store from '../store'

export default {
  name: 'Register',
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
    var checkCode = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('验证码不能为空'))
      }
      setTimeout(() => {
        if (!Number.isInteger(value)) {
          callback(new Error('请输入数字'))
        } else {
          if (value < 1000 || value > 9999) {
            callback(new Error('请输入正确的验证码'))
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
        if (this.registerForm.pass2 !== '') {
          this.$refs.registerForm.validateField('pass2')
        }
        callback()
      }
    }
    var checkPass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.registerForm.pass) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      registerForm: {
        name: '',
        pass: '',
        pass2: '',
        verCode: '',
        phone: ''
      },
      rules: {
        name: [
          { required: true, message: '请输入活动名称', trigger: 'blur' },
          { min: 3, max: 6, message: '昵称长度为 3 到 6 个字', trigger: 'blur' }
        ],
        phone: [
          { validator: checkPhone, trigger: 'blur' }
        ],
        pass: [
          { validator: checkPass, trigger: 'blur' }
        ],
        pass2: [
          { validator: checkPass2, trigger: 'blur' }
        ],
        verCode: [
          { validator: checkCode, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          const path = 'http://localhost:5000/v1/register'
          const payload = {
            name: this.registerForm.name,
            phone: this.registerForm.phone,
            password: this.registerForm.pass
          }
          axios.post(path, payload)
            .then((response) => {
              // 注册成功
              store.setNewAction()
              this.$router.push('/login')
            })
            .catch((error) => {
              console.log(error)
            })
          alert('已注册!')
        } else {
          console.log('错误提交!!')
          return false
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
