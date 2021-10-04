import http from "../http-common";

class FormacionInDataService {
  getAll() {
    return http.get("/formacionIn");
  }

  get(id) {
    return http.get(`/formacionIn/${id}`);
  }

  create(data) {
    return http.post("/formacionIn/create/", data);
  }

  update(id, data) {
    return http.put(`/formacionIn/update/${id}/`, data);
  }

  delete(id) {
    return http.delete(`/formacionIn/delete/${id}`);
  }

}

export default new FormacionInDataService();