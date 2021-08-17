import { createWebHistory, createRouter } from "vue-router";

const routes =  [
  {
    path: "/",
    alias: "/eventos",
    name: "eventos",
    component: () => import("./components/EventosList")
  },
  {
    path: "/eventos/:id",
    name: "evento-details",
    component: () => import("./components/Eventos")
  },
  {
    path: "/add",
    name: "add",
    component: () => import("./components/AddEventos")
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;