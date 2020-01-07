<template>
	<el-container>
		<el-main>
			<el-row>
				<el-col
					:xs="{ span: 18, offset: 3 }"
					:sm="{ span: 13, offset: 6 }"
					:md="{ span: 10, offset: 7 }"
					:lg="{ span: 7, offset: 8 }"
				>
					<el-card>
						<el-tag
							style="font-size: 20px;margin: 24px 36px 32px;"
							effect="light"
							>注册账号</el-tag
						>
						<el-form
							:model="registerForm"
							:rules="rules"
							label-width="102px"
							ref="registerForm"
							style="margin-right: 44px;"
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
								<el-input
									autocomplete="off"
									type="password"
									v-model="registerForm.pass"
								></el-input>
							</el-form-item>
							<el-form-item label="确认密码" prop="pass2" required>
								<el-input
									autocomplete="off"
									type="password"
									v-model="registerForm.pass2"
								></el-input>
							</el-form-item>
							<el-form-item>
								<el-button @click="sendCode('registerForm')"
									>发送验证码</el-button
								>
								<el-button @click="submitForm('registerForm')" type="primary"
									>注册</el-button
								>
							</el-form-item>
						</el-form>
					</el-card>
				</el-col>
			</el-row>
		</el-main>
	</el-container>
</template>

<script>
export default {
	name: 'Register',
	data() {
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
					if (value !== this.registerForm.code) {
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
				code: '',
				phone: ''
			},
			rules: {
				name: [
					{ required: true, message: '输入你在网站昵称', trigger: 'blur' },
					{ min: 2, message: '昵称最少两个字', trigger: 'blur' },
					{ max: 8, message: '昵称最长8个字', trigger: 'blur' }
				],
				phone: [{ validator: checkPhone, trigger: 'blur' }],
				pass: [
					{ validator: checkPass, trigger: 'blur' },
					{ min: 6, message: '密码长度至少为6位', trigger: 'blur' }
				],
				pass2: [{ validator: checkPass2, trigger: 'blur' }],
				verCode: [{ validator: checkCode, trigger: 'blur' }]
			}
		}
	},
	methods: {
		submitForm(formName) {
			this.$refs[formName].validate(valid => {
				if (valid) {
					const path = 'http://localhost:5001/v1/register'
					const payload = {
						name: this.registerForm.name,
						phone: this.registerForm.phone,
						password: this.registerForm.pass
					}
					this.$axios
						.post(path, payload)
						// eslint-disable-next-line no-unused-vars
						.then(response => {
							// 注册成功
							this.$router.push('/login')
						})
						.catch(error => {
							if (error.response.data.error_code === 1000) {
								this.$message({
									showClose: true,
									message: '该手机号已注册，请直接登录',
									type: 'info',
									duration: 5000,
									center: true
								})
							}
						})
					this.$message({
						showClose: true,
						message: '注册成功，请前往登录',
						type: 'success',
						center: true
					})
				} else {
					console.log('错误提交!!')
					return false
				}
			})
		},
		sendCode(formName) {
			this.$refs[formName].validateField('phone', valid => {
				if (valid === '') {
					// eslint-disable-next-line standard/object-curly-even-spacing
					const path = 'http://localhost:5001/v1/verify'
					const payload = {
						phone: this.registerForm.phone
					}
					this.$axios
						.post(path, payload)
						.then(response => {
							console.log(response.data)
							if (response.data.error_code === 0) {
								this.registerForm.code = response.data.code
								this.$message({
									showClose: true,
									message: '短信已发送，请注意查收',
									type: 'info',
									duration: 5000,
									center: true
								})
							}
						})
						.catch(error => {
							if (error.response.data.error_code === 1002) {
								this.$message({
									showClose: true,
									message: '短信发送过于频繁，请稍后再试',
									type: 'warning',
									duration: 5000,
									center: true
								})
							} else if (error.response.data.error_code === 1003) {
								this.$message({
									showClose: true,
									message: '该手机号不存在，请输入正确的手机号',
									type: 'warning',
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
				} else {
					console.log(valid)
					return false
				}
			})
		}
	}
}
</script>

<style scoped></style>
