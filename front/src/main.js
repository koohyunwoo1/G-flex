import  PiniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const pinia = createPinia()
const app = createApp(App)

pinia.use(PiniaPluginPersistedstate)

app.use(createPinia())
app.use(router)
app.use(pinia)

app.mount('#app')
