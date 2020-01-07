<template>
	<div class="container">
		<section>
			<div style="padding:4px 60px;">
				<el-card>
					<el-row>
						<el-col :span="4" style="text-align:center">
							<el-avatar :size="120" :src="require('../assets/logo.png')">
							</el-avatar>
						</el-col>
						<el-col :span="4">
							<h4 style="margin:0 0 12px;">王思聪</h4>
							<div style="margin-bottom:4px;">
								<router-link tag="el-link" to="/register" type="primary"
									>我的信箱：30</router-link
								>
							</div>
							<div style="margin-bottom:4px;">
								<router-link tag="el-link" to="/register" type="primary"
									>我的关注：10</router-link
								>
							</div>
							<div style="margin-bottom:4px;">
								<router-link tag="el-link" to="/register" type="primary"
									>我的余额：20</router-link
								>
							</div>
							<div style="margin-bottom:4px;">
								<router-link tag="el-link" to="/register" type="primary"
									>最近访问：20</router-link
								>
							</div>
						</el-col>
						<el-col :span="10">
							<div style="margin-top:2px;">
								<span>我的认证</span>
								<el-image
									:src="require('../assets/logo.png')"
									style="width:26px; height:26px;vertical-align:middle"
								></el-image>
								<el-image
									:src="require('../assets/logo.png')"
									style="width:26px; height:26px;vertical-align:middle"
								></el-image>
								<el-button
									@click="modifyDialog = false"
									plain
									round
									size="mini"
									style="margin-left: 60px"
									type="primary"
								>
									<router-link tag="div" to="/auth">更多认证</router-link>
								</el-button>
							</div>
							<div style="margin-top:24px; vertical-align:top">
								<span>我的资料完善度</span>
								<el-progress :percentage="42" style="width: 84%"></el-progress>
							</div>
							<div>
								<el-button
									@click="modifyDialog = false"
									plain
									round
									size="mini"
									type="primary"
								>
									<router-link tag="div" to="/edit">完善资料</router-link>
								</el-button>
								<el-button
									@click="modifyDialog = false"
									plain
									round
									size="mini"
									style="margin-left: 30px"
									type="primary"
								>
									<router-link tag="div" to="/detail">主页预览</router-link>
								</el-button>
							</div>
						</el-col>
						<el-col :span="3" style="text-align:left">
							<div>安全提示：</div>
							<span>请加强自我防范意识，提高警惕，谨防各类诈骗手段</span>
						</el-col>
					</el-row>
				</el-card>
			</div>
		</section>
		<button type="button" class="btn btn-primary">首页</button>
	</div>
</template>

<script>
export default {
	name: 'Home', // this is the name of the component
	data() {
		return {
			alerts: [
				{
					showAlert: true,
					alertVariant: 'danger',
					alertMessage: '这是测试'
				},
				{
					showAlert: true,
					alertVariant: 'info',
					alertMessage: '其他的页面会边写好功能边放上来'
				},
				{
					showAlert: true,
					alertVariant: 'dark',
					alertMessage: '现在还没有'
				}
			]
		}
	},
	methods: {
		getUser(id) {
			// eslint-disable-next-line no-template-curly-in-string
			const path = '/users/${id}'
			console.log(id)
			this.$axios
				.get(path)
				.then(res => {
					console.log(res.data)
				})
				.catch(error => {
					console.error(error)
				})
		}
	},
	created() {
		const userId = this.$route.params.id
		console.log(userId)
		this.getUser(userId)
	}
}
</script>

<style scoped></style>
