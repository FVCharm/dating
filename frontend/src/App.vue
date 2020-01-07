<template>
	<div id="app">
		<navbar></navbar>
		<router-view />
	</div>
</template>

<script>
import Navbar from '_c/Navbar'
export default {
	components: { Navbar }
}
</script>

<style lang="scss"></style>
