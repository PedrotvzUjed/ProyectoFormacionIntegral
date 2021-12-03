<template lang="html">
  <div v-if="currentEvento" class="edit-form">
    <v-container>
      <v-card>
        <v-card-title>
          Actualizar Evento
        </v-card-title>
        <v-container>
          <form>
            <v-row>
              <v-col>
                <div class="form-group">
                  <label for="tituloEvento">Titulo del evento</label>
                  <input type="text" class="form-control" id="tituloEvento"
                    v-model="currentEvento.tituloEvento"
                  />
                </div>
              </v-col>
              <v-col>
                <div class="form-group">
                  <label for="unidadResponsable">Unidad responsable del evento</label>
                  <!-- <input type="text" class="form-control" id="unidadResponsable"
                    v-model="currentEvento.unidadResponsable"
                  /> -->
                  <select v-model="currentEvento.unidadResponsable"  class="form-control" 
                  id="unidadResponsable" required name="unidadResponsable">
                  <option disabled value="">Seleccione la unidad responsable del evento</option>
                  <option>CEDU</option>
                  <option>IMAC</option>
                  <option>ICED</option>
                  <option>FACULTAD DE DERECHO Y CIENCIAS POLÍTICAS</option>
                  <option>FACULTAD DE CIENCIAS EXACTAS</option>
                  <option>ESCUELA DE LENGUAS</option>
                  <option>FACULTAD DE ODONTOLOGÍA</option>
                  <option>FACULTAD DE CIENCIAS QUÍMICAS DGO.</option>
                  <option>FACULTAD DE CIENCIAS, CULTURA FÍSICA</option>
                  <option>ESCUELA SUPERIOR DE MÚSICA</option>
                  <option>ESCUELA DE PINTURA, ESCULTURA Y ARTE</option>
                  <option>FACULTAD DE PSICOLOGÍA Y TERAPIA COM</option>
                  <option>FACULTAD DE CIENCIAS FORESTALES</option>
                  <option>FACULTAD DE ENFERMERÍA Y OBSTETRICIA</option>
                  <option>FACULTAD DE MEDICINA VETERINARIA Y ZOOT</option>
                  <option>FACULTAD DE CIENCIAS DE LA SALUD</option>
                  <option>FACULTAD DE CIENCIAS BIOLÓGICAS</option>
                  <option>FACULTAD DE INGENIERÍA, CIENCIAS Y ARQUI</option>
                  <option>FACULTAD DE AGRICULTURA Y ZOOTECNIA</option>
                  <option>FACULTAD DE TRABAJO SOCIAL (*)</option>
                  <option>FACULTAD DE MEDICINA Y NUTRICIÓN</option>
                  <option>MUSEO REGIONAL</option>
                  <option>FACULTAD DE CIENCIAS QUIMICAS DE GOMEZ PALACIO (*)</option>
                  <option>FACULTAD DE CIENCIAS QUÍMICAS</option>
                  <option>DIRECCIÓN DE DIFUSIÓN CULTURAL</option>
                  <option>FACULTAD DE TRABAJO SOCIAL</option>
                  <option>FACULTAD DE ECONOMÍA, CONTADURÍA Y ADM</option>
                  <option>RADIO UNIVERSIDAD</option>
                  <option>DIRECCIÓN DE EXTENSIÓN UNIVERSITARIA</option>
                  <option>TV UJED</option>
                  <option>DIRECCIÓN DE PLAN Y DESARROLLO ACAD</option>
                  <option>COORDINACION INSTITUCIONAL FI</option>
                  <option>UNIVERSIDAD JUÁREZ DEL ESTADO DE DURANGO</option>
                  <option>COORDINACIÓN DE VINCULACIÓN EMPRES</option>        
                  </select>

                </div>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <div class="form-group">
                  <label for="descripcionEvento">Descripción del evento</label>
                  <textarea v-model="currentEvento.descripcionEvento" class="form-control" id="descripcionEvento"></textarea>
                </div>
              </v-col>
              <v-col>
                <div class="form-group">
                  <label for="eventoDedicadoA">Evento dedicado a:</label>
                  <input type="text" class="form-control" id="eventoDedicadoA"
                    v-model="currentEvento.eventoDedicadoA"
                  />
                </div>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <div class="form-group">
                  <label for="fechaEvento">Fecha del evento:</label>
                  <input type="date" class="form-control" id="fechaEvento"
                    v-model="currentEvento.fechaEvento"
                  />
                </div> 
              </v-col>
              <v-col>
                <div class="form-group">
                  <label for="inicioEvento">Hora de inicio del evento:</label>
                  <input type="time" class="form-control" id="inicioEvento"
                    v-model="currentEvento.inicioEvento"
                  />
                </div>
              </v-col>
              <v-col>
                <div class="form-group">
                  <label for="finEvento">Hora del final del evento:</label>
                  <input type="time" class="form-control" id="finEvento"
                    v-model="currentEvento.finEvento"
                  />
                </div> 
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <div class="form-group">
                  <label for="sede">Sede del evento:</label>
                  <input type="text" class="form-control" id="sede"
                    v-model="currentEvento.sede"
                  />
                  <select v-model="currentEvento.sede"  class="form-control" 
                  id="sede" required name="sede">
                  <option disabled value="">Seleccione la sede del evento</option>
                  <option>Bellas Artes UJED</option>
                  <option>Bellas Artes UJED Lerdo</option>
                  <option>Biblioteca Central Universitaria</option>
                  <option>Bicentenario</option>
                  <option>BIOPARQUE, DURANGO</option>
                  <option>Bioparque estrella, Mty., NL.</option>
                  <option>Bolsón de Mapimí</option>
                  <option>Bosque Venustiano Carranza. Torreón, Coah.</option>
                  <option>Calle 5 de Febrero Esquina con Bruno Martínez, Zona Centro</option>
                  <option>Campus Gómez Palacio</option>
                  <option>Cancha de Santa Lucía</option>
                  <option>Cancha de usos múltiples, FCF</option>
                  <option>Cancha Frente a Facultad de Ciencias Químicas</option>
                  <option>Cancha "Robelto Silva", Carretera a Mazatlán km 1.5</option>
                  <option>Cancún, Quintana Roo</option>
                  <option>Carretera Durango Mazatlan y Calle Opalo</option>
                  <option>Casa Cuervo, Guadalajara, Jalisco</option>
                  <option>Casa de Cultura CITIBANAMEX</option>
                  <option>Casa de la Cultura de Cd. Lerdo,Durango</option>
                  <option>Casa de la Cultura de Ciudad Lerdo Durango.  Av. Francisco I. Madero 52 Nte. Col. Centro CP 35150, Lerdo, Durango </option>
                  <option>Casa de la cultura de Gómez Palacio, Campestre GP</option>
                  <option>Casa de la Cultura Durango, Calle Negrete 900 poniente</option>
                  <option>Casa de las Banquetas Altas,Gómez Palacio Dgo.</option>
                  <option>Casa Municipal del Arte y la Cultura, Hacienda de los Laureles112, Fracc. Hacienda de Tapias </option>
                  <option>Casa Nava avenida, Madero esquina con Ocampo., Ciudad Lerdo, Dgo.</option>
                  <option>Casino Murano, Hotel las Rosas, Gómez Palacio, Dgo.</option>
                  <option>Catedral Basílica Menor, Ave. 20 de Noviembre y Constitución</option>
                  <option>CBTA 3</option>
                  <option>CBTIS 110</option>
                  <option>CBTIS 89</option>
                  <option>CCH</option>
                  <option>Cd. de Mexico</option>
                  <option>Cdu (Promocion Deportiva)</option>
                  <option>CENTRAL UJED</option>
                  <option>Centro Cultural BANAMEX , 5 de Febrero Esq. con Francisco I. Madero</option>
                  <option>Centro Cultural y de Convenciones Bicentenario</option>
                  <option>Centro de Convenciones Bicentenario</option>
                  <option>Centro de Convenciones, Gómez Palacio </option>
                  <option>Centro de Convenciones, Posada del Río. Gómez Palacio, Dgo.</option>
                  <option>Centro de Integración Laboral, Fracc. Huizache</option>
                  <option>CENTRO DE INV. Y DE ESTUDIOS AVANZADOS CINVESTAV </option>
                  <option>centro de la ciudad de durango </option>
                  <option>Centro Escolar Revolución, Sección A Gómez Farías entre Luna y Urrea, Barrio de Tierra Blanca</option>
                  <option>Centro Especializado de Reintegración y Tratamiento para menores infractores (CERMI)</option>
                  <option>Centro Monterrey, Nuevo León</option>
                  <option>Centro Recreativo Tapias </option>
                  <option>Centro Regional de Educación para la Conservación (CRECO)</option>
                  <option>Cerro de Los Remedios, Durango,Dgo.</option>
                  <option>CIAC (Aquiles Serdán y Bruno Martínez)</option>
                  <option>CIIDIR IPN,Calle Sigma 119 Fracc. 20 de Noviembre II</option>
                  <option>Cine CITICINEMAS, Real del Mezquital 101 </option>
                  <option>Cinemex</option>
                  <option>Cineteca Municipal Silvestre Revueltas. Juárez 217 Nte., Zona Centro</option>
                  <option>CIUDAD DE MEXICO</option>
                  <option>Ciudad del anciano</option>
                  <option>CIUDAD UNIVERSITARIA, CDMX</option>
                  <option>Club de Leones de Durango </option>
                  <option>COLEGIO DE BACHILLERES DEL ESTADO DE DURANGO</option>
                  <option>Colegio De Ciencias Y Humanidades</option>
                  <option>Colegio de Ginecología </option>
                  <option></option>
                  </select>
                </div> 
              </v-col>
              <v-col>
                <div class="form-group">
                  <label for="cupo">Cupo del evento:</label>
                  <input class="form-control" id="cupo"
                    v-model="currentEvento.cupo"
                      name="cupo"
                    type="number"  maxlength="4"
                    min="1" max="1000"
                    placeholder="maximo mil personas"
                    oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
                  />
                </div>
              </v-col>
              <v-col>
                <div class="form-group">
                  <label for="descripcion">Descripción:</label>
                  <input type="text" class="form-control" id="descripcion" required="true"
                    v-model="currentEvento.descripcion"
                  />
                </div>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <div class="form-group">
                  <label for="creditos">Creditos del evento:</label>
                  <input class="form-control" id="creditos"
                    v-model="currentEvento.creditos"
                    name="creditos"
                    type="number"  maxlength="4"
                    min="0" max="10"
                    placeholder="maximo 10 creditos"
                    oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
                  />
                </div>
              </v-col>
              <v-col>
                <div class="form-group">
                  <label for="categorias">Categoria del evento:</label>
                  <input type="text" class="form-control" id="categorias"
                    v-model="currentEvento.categorias"
                  />
                </div>
              </v-col>
            </v-row>
          </form>
          <v-row style="padding: 20px 0px 20px 0px">
            <div class="d-grid gap-2 d-md-flex justify-content-md-end">
              <button class="btn btn-outline-danger mr-2" 
                @click="deleteEvento"
              >
                Eliminar
              </button>

              <button type="submit" class="btn btn-outline-success" 
                @click="updateEvento"
              >
                Actualizar evento
              </button>
                <p>{{ message }}</p>
            </div>
          </v-row>
        </v-container>
      </v-card>
    </v-container>
    <br>
  </div>  
  <div v-else>
    <br />
    <p>Por favor selecciona un evento...</p>
  </div>
</template>

<script>
import EventosDataService from "../../services/EventosDataService";
import swal from 'sweetalert'
export default {
  name: "evento",
  data() {
    return {
      currentEvento: null,
      message: ''
    };
  },
  methods: {
    getEvento(id) {
      EventosDataService.get(id)
        .then(response => {
          this.currentEvento = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },


    updateEvento() {
      EventosDataService.update(this.currentEvento.id, this.currentEvento)
        .then(response => {
          console.log(response.data);
          /*this.message = 'El evento se actualizo correctamente!';*/
            swal("El evento se actualizo correctamente!","","success")
        })
        .catch(e => {
          console.log(e);
           swal("No se pudo actualizar el evento correctamente (asegurese de llenar los campos correctamente)","","error")
        });
    },

    deleteEvento() {
      EventosDataService.delete(this.currentEvento.id)
        .then(response => {
          console.log(response.data);
          swal("El evento se elimino correctamente!","","success")
          this.$router.push({ name: "eventos" });
        })
        .catch(e => {
          console.log(e);
          swal("Ocurrio un error al eliminar el evento","","error")
        });
    }
  },
  mounted() {
    this.message = '';
    this.getEvento(this.$route.params.id);
    console.log(this.$route.params.id)
  }
};
</script>

<style>
.edit-form {
  /* max-width: 800px;
  margin: auto; */
}
</style>