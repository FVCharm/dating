<template>
	<div>
		<button type="button" class="btn btn-raised btn-primary">{{ msg }}</button>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'Ping',
	data() {
		return {
			msg: ''
		}
	},
	methods: {
		getMessage() {
			const path = 'http://localhost:5000/v1/ping'
			axios
				.get(path)
				.then(res => {
					this.msg = res.data
				})
				.catch(error => {
					// eslint-disable-next-line
            console.error(error);
				})
		}
	},
	created() {
		this.getMessage()
	}
}
</script>
