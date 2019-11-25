<template>
  <div class="container">
    <alert
      v-for="(alert, index) in alerts" :key="index"
      v-bind:variant="alert.alertVariant"
      v-bind:message="alert.alertMessage">
    </alert>
    <button type="button" class="btn btn-primary">首页</button>
  </div>
</template>

<script>
import Alert from './Alert'

export default {
  name: 'Home', // this is the name of the component
  components: {
    alert: Alert
  },
  data () {
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
  }
}
</script>

<style scoped>

</style>
