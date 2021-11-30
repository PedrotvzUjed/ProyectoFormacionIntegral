import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    alias: "/inicio",
    name: "inicio",
    component: () => import("../components/Inicio")
  },
  /* Eventos */
  {
    path: "/eventos",
    name: "eventos",
    component: () => import("../components/Eventos/EventosList")
  },
  {
    path: "/eventos/:id",
    name: "evento-details",
    component: () => import("../components/Eventos/Eventos")
  },
  {
    path: "/add",
    name: "add-evento",
    component: () => import("../components/Eventos/AddEventos")
  },
  {
    path: "/calendario",
    name: "calendario",
    component: () => import("../components/Eventos/CalendarioEventos")
  },
  /* Formacion Integral */
  {
    path: "/formacionI",
    name: "formacionIntegral",
    component: () => import("../components/FormacionIntegral/FormacionIntegral")
  },
  {
    path: "/fi-registro/:id",
    name: "registro",
    component: () => import("../components/FormacionIntegral/Registro")
  },
  {
    path: "/fi-asistencia/:id",
    name: "asistencia",
    component: () => import("../components/FormacionIntegral/Asistencia")
  },
  {
    path: "/fi-alumnos",
    name: "fi-alumnos",
    component: () => import("../components/Alumnos/Alumnos")
  },
  {
    path: "/alumnos-vista-eventos",
    name: "alumnos-vista-eventos",
    component: () => import("../components/AlumnosVista/EventosAlumno")
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
