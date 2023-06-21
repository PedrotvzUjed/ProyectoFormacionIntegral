<template>
  <div class="submit-form">
    <v-card>
      <v-card-title>
        Registro de evento
      </v-card-title>
      <div v-if="!submitted">
        <v-container style="padding: 0px 40px 40px 40px">
          <v-form 
          ref="form"
          v-model="valid"
          lazy-validation>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  md="6"
                  sm="12"
                  lg="6"
                  xl="6"
                  
                >
                  <v-text-field
                    :rules="[v => !!v || 'Campo requerido']"
                    :counter="100"
                    label="Titulo de Evento"
                    id="tituloEvento"
                    v-model="eventos.tituloEvento"
                    name="tituloEvento"
                    required
                    outlined
                  ></v-text-field>
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                  sm="12"
                  lg="6"
                  xl="6"
                >
                  <v-combobox
                    :rules="[v => !!v || 'Campo requerido']"
                    v-model="eventos.unidadResponsable"
                    :items="unidades"
                    id="unidadResponsable" 
                    name="unidadResponsable"
                    label="Unidad responsable"
                    outlined
                    :counter="100"
                    required
                  ></v-combobox>
                  
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                  sm="12"
                  lg="6"
                  xl="6"
                >
                  <v-textarea
                    v-model="eventos.descripcionEvento" 
                    id="descripcionEvento" 
                    name="descripcionEvento"
                    label="Descripción del evento"
                    :counter="200"
                    rows="2"
                    required
                    outlined
                    :rules="[v => !!v || 'Campo requerido']"
                  ></v-textarea>
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                  sm="12"
                  lg="6"
                  xl="6"
                >
                  <v-text-field
                    id="eventoDedicadoA"
                    required
                    v-model="eventos.eventoDedicadoA"
                    name="eventoDedicadoA"
                    :rules="[v => !!v || 'Campo requerido']"
                    :counter="100"
                    label="Evento dedicado a"
                    outlined
                    
                  ></v-text-field>
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                  sm="12"
                  lg="4"
                  xl="4"
                >
                  <v-text-field
                    id="fechaEvento"
                    v-model="eventos.fechaEvento"
                    name="fechaEvento"
                    :rules="[v => !!v || 'Campo requerido']"
                    label="Fecha del evento"
                    required
                    outlined
                    type="date"
                  ></v-text-field>
                </v-col>
                
                <v-col
                  cols="12"
                  md="4"
                  sm="6"
                  lg="4"
                  xl="4"
                >
                  <v-text-field
                    id="inicioEvento"
                    required
                    v-model="eventos.inicioEvento"
                    name="inicioEvento"
                    :rules="[v => !!v || 'Campo requerido']"
                    label="Hora de inicio del evento"
                    outlined
                    type="time"
                  ></v-text-field>
                </v-col>
                
                <v-col
                  cols="12"
                  md="4"
                  sm="6"
                  lg="4"
                  xl="4"
                >
                  <v-text-field
                    id="finEvento"
                    required
                    v-model="eventos.finEvento"
                    name="finEvento"
                    :rules="[v => !!v || 'Campo requerido']"
                    label="Hora del final del evento"
                    outlined
                    type="time"
                  ></v-text-field>
                </v-col>
                
                <v-col
                  cols="12"
                  md="4"
                  sm="6"
                  lg="4"
                  xl="4"
                >
                  <v-combobox
                    v-model="eventos.sede"  
                    id="sede" 
                    required 
                    name="sede"
                    :rules="[v => !!v || 'Campo requerido']"
                    :counter="100"
                    label="Sede del evento"
                    outlined
                    :items="unidades"
                  ></v-combobox>
                </v-col>
                
                <v-col
                  cols="12"
                  md="4"
                  sm="6"
                  lg="4"
                  xl="4"
                >
                  <v-text-field
                    id="cupo"
                    required
                    v-model="eventos.cupo"
                    name="cupo"
                    type="number"  maxlength="4"
                    min="1" max="1000"
                    placeholder="maximo mil personas"
                    oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
                    :rules="[v => !!v || 'Campo requerido']"
                    label="Cupo del evento"
                    outlined
                  ></v-text-field>
                </v-col>
                
                <v-col
                  cols="12"
                  md="4"
                  sm="12"
                  lg="4"
                  xl="4"
                >
                  <v-text-field
                    id="descripcion"
                    required
                    v-model="eventos.descripcion"
                    name="descripcion"
                    :rules="[v => !!v || 'Campo requerido']"
                    :counter="150"
                    label="Descripción del lugar"
                    outlined
                  ></v-text-field>
                </v-col>
                
                <v-col
                  cols="12"
                  md="6"
                  sm="12"
                  lg="6"
                  xl="6"
                >
                  <v-text-field
                    id="creditos"
                    required
                    v-model="eventos.creditos"
                    name="creditos"
                    type="number"  maxlength="4"
                    min="0" max="10"
                    placeholder="maximo 10 creditos"
                    oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
                    :rules="[v => !!v || 'Campo requerido']"
                    label="Creditos otorgados en el evento"
                    outlined
                  ></v-text-field>
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                  sm="12"
                  lg="6"
                  xl="6"
                >
                  <v-combobox
                    v-model="eventos.categorias"  
                    id="categorias" 
                    name="categorias"
                    :items="categoriaEvento"
                    label="Categoria del evento"
                    required
                    outlined
                    :rules="[v => !!v || 'Campo requerido']"
                  ></v-combobox>
                </v-col>
              </v-row>
            </v-container>
            <v-row>
              <button @click.prevent="saveEvento" class="btn btn-success">Crear evento</button>
            </v-row>
          </v-form>
          <!-- <v-row>
            <v-col>
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
            </v-col>
            <v-col>
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
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <div class="form-group">
                <label for="descripcionEvento">Descripción del evento</label>
              
                <textarea v-model="eventos.descripcionEvento" class="form-control" id="descripcionEvento" 
                placeholder="Descripción del evento" required name="descripcionEvento"></textarea>
              </div>
            </v-col>
            <v-col>
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
            </v-col>
          </v-row>
          <v-row>
            <v-col>
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
            </v-col>
            <v-col>
              
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
            </v-col>
            <v-col>
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
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <div class="form-group">
                <label for="sede">Sede del evento</label>
                <select v-model="eventos.sede"  class="form-control" 
                id="sede" required name="sede">
                <option disabled value="">Seleccione la sede del evento</option>
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
                <option> </option>        
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
                <label for="cupo">Cupo del evento</label>
                <input 
                  class="form-control"
                  id="cupo"
                  required
                  v-model="eventos.cupo"
                  name="cupo"
                  type="number"  
                  maxlength="4"
                  min="1" max="1000"
                  placeholder="maximo mil personas"
                  oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
                />
              </div>
            </v-col>
            <v-col>
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
            </v-col>
          </v-row>
          <v-row>
            <v-col>
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
            </v-col>
            <v-col>
              <div class="form-group">
                <label for="categorias">Categoria del evento</label>
                <select v-model="eventos.categorias"  class="form-control" 
                id="categorias" name="categorias">
                 <select v-model="eventos.categorias"  class="form-control" 
                id="categorias" :required="!selected" name="categorias">
                <option disabled value="">Seleccione la categoria del evento</option>
                  <option>Arte</option>
                  <option>Ciencia</option>
                  <option>Deporte</option>
                  <option>Civismo</option>
                </select>
              </div>
            </v-col>
          </v-row> -->
          
        </v-container>
      </div>
      <div v-else>
        <v-container style="padding: 60px">
          <v-row>
            <button class="btn btn-success" @click="newEvento">Capturar otro evento</button>
          </v-row>
        </v-container>
      </div>
    </v-card>
    
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
        categorias:"",
      },
      unidades: ['CEDU',
                'IMAC',
                'ICED',
                'FACULTAD DE DERECHO Y CIENCIAS POLÍTICAS',
                'FACULTAD DE CIENCIAS EXACTAS',
                'ESCUELA DE LENGUAS',
                'FACULTAD DE ODONTOLOGÍA',
                'FACULTAD DE CIENCIAS QUÍMICAS DGO.',
                'FACULTAD DE CIENCIAS, CULTURA FÍSICA',
                'ESCUELA SUPERIOR DE MÚSICA',
                'ESCUELA DE PINTURA, ESCULTURA Y ARTE',
                'FACULTAD DE PSICOLOGÍA Y TERAPIA COM',
                'FACULTAD DE CIENCIAS FORESTALES',
                'FACULTAD DE ENFERMERÍA Y OBSTETRICIA',
                'FACULTAD DE MEDICINA VETERINARIA Y ZOOT',
                'FACULTAD DE CIENCIAS DE LA SALUD',
                'FACULTAD DE CIENCIAS BIOLÓGICAS',
                'FACULTAD DE INGENIERÍA, CIENCIAS Y ARQUI',
                'FACULTAD DE AGRICULTURA Y ZOOTECNIA',
                'FACULTAD DE TRABAJO SOCIAL (*)',
                'FACULTAD DE MEDICINA Y NUTRICIÓN',
                'MUSEO REGIONAL',
                'FACULTAD DE CIENCIAS QUIMICAS DE GOMEZ PALACIO (*)',
                'FACULTAD DE CIENCIAS QUÍMICAS',
                'DIRECCIÓN DE DIFUSIÓN CULTURAL',
                'FACULTAD DE TRABAJO SOCIAL',
                'FACULTAD DE ECONOMÍA, CONTADURÍA Y ADM',
                'RADIO UNIVERSIDAD',
                'DIRECCIÓN DE EXTENSIÓN UNIVERSITARIA',
                'TV UJED',
                'DIRECCIÓN DE PLAN Y DESARROLLO ACAD',
                'COORDINACION INSTITUCIONAL FI',
                'UNIVERSIDAD JUÁREZ DEL ESTADO DE DURANGO',
                'COORDINACIÓN DE VINCULACIÓN EMPRES',      ],
      categoriaEvento: ['Arte','Ciencia', 'Deporte', 'Civismo', 'Responsabilidad social universitaria', 'Emprendimiento'],
      submitted: false,
      valid: true,
      colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
    };
  },
  methods: {
    validate () {
      this.valid = this.$refs.form.validate()
    },
    saveEvento() {
      this.validate();
      if (this.valid == true) {
        this.createEvento();
      }
      else{
        console.log('Evento no Validado ' + false)
      }
      
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
  
</style>