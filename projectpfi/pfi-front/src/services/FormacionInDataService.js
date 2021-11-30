import http from "../http-common";

class FormacionInDataService {
  getAll(evento_id) {
    return http.get(`/formacionIn/?evento_id=${evento_id}`);
  }

  getRaw() {
    return http.get(`/formacionIn`);
  }

  getUserExist(evento_id, matricula) {
    return http.get(`/formacionIn/?evento_id=${evento_id}&matricula=${matricula}`)
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