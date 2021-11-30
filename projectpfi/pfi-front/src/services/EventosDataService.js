import http from "../http-common";
import axios from "axios";
const API = "http://127.0.0.1:8000";

class EventosDataService {
  getAll() {
    return http.get("/eventos");
  }

  get(id) {
    return http.get(`/eventos/${id}`);
  }

  create(data) {
    return axios.post(API+"/eventos/create/", data);
  }

  update(id, data) {
    return http.put(`/eventos/update/${id}/`, data);
  }

  delete(id) {
    return http.delete(`/eventos/delete/${id}`);
  }

  deleteAll() {
    return http.delete(`/eventos`);
  }
  findByTitle(tituloEvento) {
    return http.get(`/eventos?tituloEvento=${tituloEvento}`);
  }

  getTodayEvents(today){
    return http.get(`/eventos?fechaEvento=${today}`);
  }
  /* Calendario */
  createCalendario(data) {
    return http.post("/eventos/create/calendario/", data);
  }
  getAllCalendario() {
    return http.get("/eventos/calendario");
  }
  
}

export default new EventosDataService();