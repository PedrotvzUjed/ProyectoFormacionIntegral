<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="unidadResponsable">Unidad responsable del evento</label>
        <select v-model="eventos.unidadResponsable"  class="form-control" 
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

      <div class="form-group">
        <label for="tituloEvento">Titulo del evento</label>
        <input
          class="form-control"
          id="tituloEvento"
          required
          v-model="eventos.tituloEvento"
          name="tituloEvento"
        />
      </div>
      
      <div class="form-group">
        <label for="descripcionEvento">Descripción del evento</label>
      
        <textarea v-model="eventos.descripcionEvento" class="form-control" id="descripcionEvento" 
        placeholder="Descripción del evento" required name="descripcionEvento"></textarea>
      </div>

      <div class="form-group">
        <label for="eventoDedicadoA">Evento dedicado a</label>
        <input
          class="form-control"
          id="eventoDedicadoA"
          required
          v-model="eventos.eventoDedicadoA"
          name="eventoDedicadoA"
        />
      </div>
      
      <div class="form-group">
        <label for="fechaEvento">Fecha del evento</label>
        <input type="date"
          class="form-control"
          id="fechaEvento"
          required
          v-model="eventos.fechaEvento"
          name="fechaEvento"
        />
      </div>

      <div class="form-group">
        <label for="inicioEvento">Hora de inicio del evento</label>
        <input type="time"
          class="form-control"
          id="inicioEvento"
          required
          v-model="eventos.inicioEvento"
          name="inicioEvento"
        />
      </div>

      <div class="form-group">
        <label for="finEvento">Hora del final del evento</label>
        <input type="time"
          class="form-control"
          id="finEvento"
          required
          v-model="eventos.finEvento"
          name="finEvento"
        />
      </div>
      
       <div class="form-group">
        <label for="sede">Sede del evento</label>
        <select v-model="eventos.sede"  class="form-control" 
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

        <div class="form-group">
        <label for="cupo">Cupo del evento</label>
        <input 
          class="form-control"
          id="cupo"
          required
          v-model="eventos.cupo"
          name="cupo"
          type="number"  maxlength="4"
          min="1" max="1000"
          placeholder="maximo mil personas"
          oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
        />
      </div>

      <div class="form-group">
        <label for="descripcion">Descripción:</label>
        <input
          class="form-control"
          id="descripcion"
          required
          v-model="eventos.descripcion"
          name="descripcion"
        />
      </div>

      <div class="form-group">
        <label for="creditos">Creditos otorgados en el evento</label>
        <input
          class="form-control"
          id="creditos"
          required
          v-model="eventos.creditos"
          name="creditos"
          type="number"  maxlength="4"
          min="0" max="10"
          placeholder="maximo 10 creditos"
          oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"

        />
      </div>

       <div class="form-group">
        <label for="categorias">Categoria del evento</label>
        <select v-model="eventos.categorias"  class="form-control" 
        id="categorias" name="categorias">
        <!-- <select v-model="eventos.categorias"  class="form-control" 
        id="categorias" :required="!selected" name="categorias"> -->
        <option disabled value="">Seleccione la categoria del evento</option>
        <option>Música</option>
        <option>Teatro</option>
        <option>Fotografía</option>
        <option>Canto, Danza</option>
        <option>Cine, TV, Radio</option>
        <option>Cívicas</option>
        <option>Visitas guiadas, otras</option>
        <option>Deportes de conjunto</option>
        <option>Deportes individuales</option>
        <option>Participación recreativa</option>
        <option>Aeróbicos, Gimnasio</option>
        <option>Ajedrez</option>
        <option>Congresos disciplinares, foros</option>
        <option>Conferencias, cursos, seminarios</option>
        <option>Materias electivas</option>
        <option>Idioma (certificación A1, B1 y B2)</option>
        <option>Verano de investigación</option>
        <option>Brigadas-campañas</option>
        <option>Tutorías</option>
        <option>Valores</option>
        <option>Serv. Socical Universitario</option>
        <option>Estancias</option>
        </select>
      </div>
   <br>
      <button @click="saveEvento" class="btn btn-success">Crear evento</button>
    </div>

    <div v-else>
      <button class="btn btn-success" @click="newEvento">Capturar otro evento</button>
    </div>
  </div>
</template>

<script>
import swal from 'sweetalert'		
import EventosDataService from "../../services/EventosDataService";

export default {
  name: "add-evento",
 
  data() {
    return {
      eventos: {
        id: null,
        tituloEvento: "",
        unidadResponsable: "",
        descripcionEvento: "",
        eventoDedicadoA:"",
        fechaEvento:"",
        inicioEvento:"",
        finEvento:"",
        sede:"",
        cupo:"",
        descripcion:"",
        creditos:"",
        categorias:""
      },
      
      submitted: false,
      colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
    };
  },
  methods: {
    saveEvento() {
      this.createEvento();
    },
    
    newEvento() {
      this.submitted = false;
      this.eventos = {};
    },
    createEvento(){
      var data = {
        tituloEvento: this.eventos.tituloEvento,
        unidadResponsable: this.eventos.unidadResponsable,
        descripcionEvento:this.eventos.descripcionEvento,
        eventoDedicadoA:this.eventos.eventoDedicadoA,
        fechaEvento:this.eventos.fechaEvento,
        inicioEvento:this.eventos.inicioEvento,
        finEvento:this.eventos.finEvento,
        sede:this.eventos.sede,
        cupo:this.eventos.cupo,
        descripcion:this.eventos.descripcion,
        creditos:this.eventos.creditos,
        categorias:this.eventos.categorias,
        
      };

      EventosDataService.create(data)
        .then(response => {
          this.eventos.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
            swal("El evento se ha registrado correctamente!!","","success")
            this.createCalendario(response.data);
        })
        .catch(e => {
          console.log(e);
            swal("No se pudo registrar el evento. Verifique que lleno correctamente todos los campos.","","error")
        });
    },
    createCalendario(dataEvento){
      var campos = {
        name : dataEvento.tituloEvento,
        color : this.colors[this.rnd(0, this.colors.length - 1)],
        start : dataEvento.fechaEvento + ' ' + dataEvento.inicioEvento,
        end : dataEvento.fechaEvento + ' ' + dataEvento.finEvento,
        details : dataEvento.descripcionEvento,
        evento : dataEvento.id
      }
      EventosDataService.createCalendario(campos)
        .then(response => {
          console.log(response.data);
          this.submitted = true;
            swal("El evento se registro y agrego al calendario!!","","success")
        })
        .catch(e => {
          console.log(e);
            swal("No se pudo agregar al calendario","","error")
        });
    },
    rnd (a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a
    },
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>