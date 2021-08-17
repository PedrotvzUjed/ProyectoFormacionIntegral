import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import Listeventos from '@/components/eventos/Listeventos'
import EditEventos from '@/components/eventos/EditEventos'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/eventos',
      name: '/Listeventos',
      component: Listeventos
    }, {
      path: '/eventos/:id/edit',
      name: '/EditEventos',
      component: EditEventos
    }
  ],
  mode: 'history'
})
