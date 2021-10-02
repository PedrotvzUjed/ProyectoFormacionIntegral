import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    alias: "/eventos",
    name: "eventos",
    component: () => import("../components/EventosList")
  },
  {
    path: "/eventos/:id",
    name: "evento-details",
    component: () => import("../components/Eventos")
  },
  {
    path: "/add",
    name: "add",
    component: () => import("../components/AddEventos")
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
