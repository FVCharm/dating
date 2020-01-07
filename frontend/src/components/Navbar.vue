<template>
	<section>
		<div class="container">
			<nav
				class="navbar navbar-expand-lg navbar-dark"
				style="margin-bottom: 20px; background-color: #ff7a8e"
			>
				<router-link to="/" class="navbar-brand">
					<img
						src="../assets/logo.png"
						width="30"
						height="30"
						class="d-inline-block align-top"
						alt=""
					/>
					首页
				</router-link>
				<button
					class="navbar-toggler"
					type="button"
					data-toggle="collapse"
					data-target="#navbarSupportedContent"
					aria-controls="navbarSupportedContent"
					aria-expanded="false"
					aria-label="Toggle navigation"
				>
					<span class="navbar-toggler-icon"></span>
				</button>

				<div class="collapse navbar-collapse" id="navbarSupportedContent">
					<ul class="navbar-nav mr-auto mt-2 mt-lg-0">
						<li class="nav-item active">
							<router-link to="/" class="nav-link">
								<span class="sr-only">(current)</span></router-link
							>
						</li>
					</ul>

					<ul
						v-if="sharedState.is_authenticated"
						class="nav navbar-nav navbar-right"
					>
						<li class="nav-item">
							<router-link class="nav-link " to="/edit">编辑</router-link>
						</li>
						<li class="nav-item">
							<router-link
								v-bind:to="{
									name: 'Profile',
									params: { id: sharedState.user_id }
								}"
								class="nav-link"
								>详情</router-link
							>
						</li>
						<li class="nav-item">
							<a v-on:click="handlerLogout" class="nav-link" href="#">登出</a>
						</li>
					</ul>
					<ul v-else class="nav navbar-nav navbar-right">
						<li class="nav-item">
							<router-link to="/login" class="nav-link">登录</router-link>
						</li>
					</ul>
				</div>
			</nav>
		</div>
	</section>
</template>

<script>
import store from '../store.js'
export default {
	name: 'Navbar',
	data() {
		return {
			sharedState: store.state
		}
	},
	methods: {
		// eslint-disable-next-line no-unused-vars
		handlerLogout(e) {
			store.logoutAction()
			this.$router.push('login')
		}
	}
}
</script>

<style scoped></style>
