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

  filtroCategoria(categoria){
    return http.get(`/eventos?categorias=${categoria}`);
  }

  delete(id) {
    return http.delete(`/eventos/delete/${id}`);
  }

  findByTitle(tituloEvento) {
    return http.get(`/eventos?tituloEvento=${tituloEvento}`);
  }

  /* Calendario */
  createCalendario(data) {
    return http.post("/eventos/create/calendario/", data);
  }

  getAllCalendario() {
    return http.get("/eventos/calendario");
  }

  getTodayEvents(today){
    return http.get(`/eventos?fechaEvento=${today}`);
  }
  
  /* Evidencias */
  createEvidencia(formData) {
    return axios.post(API+'/eventos/create/evidencia',
            formData,
            {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
  }
  updateEvidencia(formData, evidencia) {
    return axios.put(API+`/eventos/update/evidencia/${evidencia}/`,
            formData,
            {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
  }

  getEvidencias(evento, alumno) {
    return http.get(`/eventos/evidencia?evento=${evento}&alumno=${alumno}`);
  }

  getClasificacion(){
    return http.get("/eventos/clasificacion_eve");
  }

  getCategorias1(clasif_id){
    return http.get(`/eventos/categorias1_eve?clasificacion=${clasif_id}`);
  }

  getCategorias2(cat_id){
    return http.get(`/eventos/categorias2_eve?catalogo=${cat_id}`);
  }

  getCategoriasArte(cat_id){
    return http.get(`/eventos/categoriasArte_eve?categoria=${cat_id}`);
  }
}

export default new EventosDataService();