import http from "../http-common";

class EventosDataService {
  getAll() {
    return http.get("/eventos");
  }

  get(id) {
    return http.get(`/eventos/${id}`);
  }

  create(data) {
    return http.post("/eventos/create/", data);
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
}

export default new EventosDataService();