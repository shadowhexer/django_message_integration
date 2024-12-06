import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const theme = {
  colors: {
    background: '#212121'
  }
}

const app = createApp(App);
const vuetify = createVuetify({
    components,
    directives,
    theme: {
      defaultTheme: 'theme',
      themes: {
        theme,
      }
    }
  });

app.use(router).use(vuetify).mount('#app')
