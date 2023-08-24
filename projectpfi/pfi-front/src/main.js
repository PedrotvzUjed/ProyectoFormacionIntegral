import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import router from './router'
import GSignInButton from 'vue-google-signin-button'
Vue.use(GSignInButton)

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  GSignInButton,
  render: h => h(App)
}).$mount('#app')
