<template lang="html">
  <div v-if="currentEvento" class="edit-form">
    <v-container>
      <v-card>
        <v-card-title>
          Actualizar Evento
        </v-card-title>
        <v-container>
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
                    v-model="currentEvento.tituloEvento"
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
                    v-model="currentEvento.unidadResponsable"
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
                    v-model="currentEvento.descripcionEvento" 
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
                    v-model="currentEvento.eventoDedicadoA"
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
                    v-model="currentEvento.fechaEvento"
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
                    v-model="currentEvento.inicioEvento"
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
                    v-model="currentEvento.finEvento"
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
                    v-model="currentEvento.sede"  
                    id="sede" 
                    required 
                    name="sede"
                    :rules="[v => !!v || 'Campo requerido']"
                    :counter="100"
                    label="Sede del evento"
                    outlined
                    :items="sede"
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
                    v-model="currentEvento.cupo"
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
                    v-model="currentEvento.descripcion"
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
                    v-model="currentEvento.creditos"
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
                    v-model="currentEvento.categorias"  
                    id="categorias" 
                    name="categorias"
                    :items="clasificacion"
                    label="Categoria del evento"
                    required
                    outlined
                    :rules="[v => !!v || 'Campo requerido']"
                    @change="getCategorias1($event.id, true)"
                  ></v-combobox>
                </v-col>

                <v-col v-if="currentEvento.categorias != ''" cols="12" md="6" sm="12" lg="6" xl="6">
                  <v-combobox
                    v-model="currentEvento.subCategoria1"
                    :rules="[(v) => !!v || 'Campo requerido']"
                    :items="categoria1"
                    id="categorias_1"
                    name="categorias_1"
                    label="Categoria"
                    outlined
                    :counter="100"
                    required
                    @change="getCategorias2($event.id, true)"
                  ></v-combobox>
                </v-col>

                <p v-if="currentEvento.subCategoria1 != '' && currentEvento.subCategoria1.id >= 23"> Objetivo: {{currentEvento.subCategoria1.objetivo}}</p>

                <template  v-if="currentEvento.subCategoria1 != ''">
                  <v-col v-if="currentEvento.categorias.id == 18 || currentEvento.subCategoria1.id >= 23" cols="12" md="6" sm="12" lg="6" xl="6">
                    <!-- <v-combobox
                      v-model="eventos.categorias_2"
                      :rules="[(v) => !!v || 'Campo requerido']"
                      :items="categoria2"
                      id="categorias_2"
                      name="categorias_2"
                      label="Categoria s"
                      outlined
                      :counter="100"
                      required
                      @change="imprimirVal($event)"
                    ></v-combobox> -->
                  </v-col>

                  <v-col v-else-if="currentEvento.subCategoria1 != '' && currentEvento.subCategoria1.id != '18'" cols="12" md="6" sm="12" lg="6" xl="6">
                    <v-combobox
                      v-model="currentEvento.subCategoria2"
                      :rules="[(v) => !!v || 'Campo requerido']"
                      :items="categoria2"
                      id="categorias_2"
                      name="categorias_2"
                      label="Categoria"
                      outlined
                      :counter="100"
                      required
                      @change="getCategoriasArte($event.id)"
                    ></v-combobox>
                  </v-col>
                </template>
                
                <v-col v-if="currentEvento.subCategoria2 != '' && currentEvento.categorias.id == 1 && currentEvento.subCategoria2.id < 64 " cols="12" md="6" sm="12" lg="6" xl="6">
                  <v-combobox
                    v-model="currentEvento.subCategoriaArte"
                    :rules="[(v) => !!v || 'Campo requerido']"
                    :items="categoriaArte"
                    id="categorias_arte"
                    name="categorias_arte"
                    label="Categoria Arte"
                    outlined
                    :counter="100"
                    required
                    @change="imprimirVal($event)"
                  ></v-combobox>
                </v-col>
              </v-row>
            </v-container>
          
            <v-row style="padding: 20px 0px 20px 0px">
              <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                <!-- <button class="btn btn-outline-danger mr-2" 
                  @click="deleteEvento"
                >
                  Eliminar
                </button> -->

                <button type="submit" class="btn btn-outline-success" 
                  @click.prevent="updateEvento"
                >
                  Actualizar evento
                </button>
                  <p>{{ message }}</p>
              </div>
            </v-row>
          </v-form>
          
          
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
import swal from "sweetalert";
export default {
  name: "evento",
  data() {
    return {
      currentEvento: null,
      valid: true,
      message: "",
      clasificacion: [],
      categoria1: [],
      categoria2: [],
      categoriaArte: [],
      unidades: [
        "CEDU",
        "IMAC",
        "ICED",
        "FACULTAD DE DERECHO Y CIENCIAS POLÍTICAS",
        "FACULTAD DE CIENCIAS EXACTAS",
        "ESCUELA DE LENGUAS",
        "FACULTAD DE ODONTOLOGÍA",
        "FACULTAD DE CIENCIAS QUÍMICAS DGO.",
        "FACULTAD DE CIENCIAS, CULTURA FÍSICA",
        "ESCUELA SUPERIOR DE MÚSICA",
        "ESCUELA DE PINTURA, ESCULTURA Y ARTE",
        "FACULTAD DE PSICOLOGÍA Y TERAPIA COM",
        "FACULTAD DE CIENCIAS FORESTALES",
        "FACULTAD DE ENFERMERÍA Y OBSTETRICIA",
        "FACULTAD DE MEDICINA VETERINARIA Y ZOOT",
        "FACULTAD DE CIENCIAS DE LA SALUD",
        "FACULTAD DE CIENCIAS BIOLÓGICAS",
        "FACULTAD DE INGENIERÍA, CIENCIAS Y ARQUI",
        "FACULTAD DE AGRICULTURA Y ZOOTECNIA",
        "FACULTAD DE TRABAJO SOCIAL (*)",
        "FACULTAD DE MEDICINA Y NUTRICIÓN",
        "MUSEO REGIONAL",
        "FACULTAD DE CIENCIAS QUIMICAS DE GOMEZ PALACIO (*)",
        "FACULTAD DE CIENCIAS QUÍMICAS",
        "DIRECCIÓN DE DIFUSIÓN CULTURAL",
        "FACULTAD DE TRABAJO SOCIAL",
        "FACULTAD DE ECONOMÍA, CONTADURÍA Y ADM",
        "RADIO UNIVERSIDAD",
        "DIRECCIÓN DE EXTENSIÓN UNIVERSITARIA",
        "TV UJED",
        "DIRECCIÓN DE PLAN Y DESARROLLO ACAD",
        "COORDINACION INSTITUCIONAL FI",
        "UNIVERSIDAD JUÁREZ DEL ESTADO DE DURANGO",
        "COORDINACIÓN DE VINCULACIÓN EMPRES",
      ],
      sede: [
        "CEDU",
        "IMAC",
        "ICED",
        "FACULTAD DE DERECHO Y CIENCIAS POLÍTICAS",
        "FACULTAD DE CIENCIAS EXACTAS",
        "ESCUELA DE LENGUAS",
        "FACULTAD DE ODONTOLOGÍA",
        "FACULTAD DE CIENCIAS QUÍMICAS DGO.",
        "FACULTAD DE CIENCIAS, CULTURA FÍSICA",
        "ESCUELA SUPERIOR DE MÚSICA",
        "ESCUELA DE PINTURA, ESCULTURA Y ARTE",
        "FACULTAD DE PSICOLOGÍA Y TERAPIA COM",
        "FACULTAD DE CIENCIAS FORESTALES",
        "FACULTAD DE ENFERMERÍA Y OBSTETRICIA",
        "FACULTAD DE MEDICINA VETERINARIA Y ZOOT",
        "FACULTAD DE CIENCIAS DE LA SALUD",
        "FACULTAD DE CIENCIAS BIOLÓGICAS",
        "FACULTAD DE INGENIERÍA, CIENCIAS Y ARQUI",
        "FACULTAD DE AGRICULTURA Y ZOOTECNIA",
        "FACULTAD DE TRABAJO SOCIAL (*)",
        "FACULTAD DE MEDICINA Y NUTRICIÓN",
        "MUSEO REGIONAL",
        "FACULTAD DE CIENCIAS QUIMICAS DE GOMEZ PALACIO (*)",
        "FACULTAD DE CIENCIAS QUÍMICAS",
        "DIRECCIÓN DE DIFUSIÓN CULTURAL",
        "FACULTAD DE TRABAJO SOCIAL",
        "FACULTAD DE ECONOMÍA, CONTADURÍA Y ADM",
        "RADIO UNIVERSIDAD",
        "DIRECCIÓN DE EXTENSIÓN UNIVERSITARIA",
        "TV UJED",
        "DIRECCIÓN DE PLAN Y DESARROLLO ACAD",
        "COORDINACION INSTITUCIONAL FI",
        "UNIVERSIDAD JUÁREZ DEL ESTADO DE DURANGO",
        "COORDINACIÓN DE VINCULACIÓN EMPRES",
        " ",
        "Bellas Artes UJED",
        "Bellas Artes UJED Lerdo",
        "Biblioteca Central Universitaria",
        "Bicentenario",
        "BIOPARQUE, DURANGO",
        "Bioparque estrella, Mty., NL.",
        "Bolsón de Mapimí",
        "Bosque Venustiano Carranza. Torreón, Coah.",
        "Calle 5 de Febrero Esquina con Bruno Martínez, Zona Centro",
        "Campus Gómez Palacio",
        "Cancha de Santa Lucía",
        "Cancha de usos múltiples, FCF",
        "Cancha Frente a Facultad de Ciencias Químicas",
        'Cancha "Robelto Silva", Carretera a Mazatlán km 1.5',
        "Cancún, Quintana Roo",
        "Carretera Durango Mazatlan y Calle Opalo",
        "Casa Cuervo, Guadalajara, Jalisco",
        "Casa de Cultura CITIBANAMEX",
        "Casa de la Cultura de Cd. Lerdo,Durango",
        "Casa de la Cultura de Ciudad Lerdo Durango.  Av. Francisco I. Madero 52 Nte. Col. Centro CP 35150, Lerdo, Durango ",
        "Casa de la cultura de Gómez Palacio, Campestre GP",
        "Casa de la Cultura Durango, Calle Negrete 900 poniente",
        "Casa de las Banquetas Altas,Gómez Palacio Dgo.",
        "Casa Municipal del Arte y la Cultura, Hacienda de los Laureles112, Fracc. Hacienda de Tapias ",
        "Casa Nava avenida, Madero esquina con Ocampo., Ciudad Lerdo, Dgo.",
        "Casino Murano, Hotel las Rosas, Gómez Palacio, Dgo.",
        "Catedral Basílica Menor, Ave. 20 de Noviembre y Constitución",
        "CBTA 3",
        "CBTIS 110",
        "CBTIS 89",
        "CCH",
        "Cd. de Mexico",
        "Cdu (Promocion Deportiva)",
        "CENTRAL UJED",
        "Centro Cultural BANAMEX , 5 de Febrero Esq. con Francisco I. Madero",
        "Centro Cultural y de Convenciones Bicentenario",
        "Centro de Convenciones Bicentenario",
        "Centro de Convenciones, Gómez Palacio ",
        "Centro de Convenciones, Posada del Río. Gómez Palacio, Dgo.",
        "Centro de Integración Laboral, Fracc. Huizache",
        "CENTRO DE INV. Y DE ESTUDIOS AVANZADOS CINVESTAV ",
        "centro de la ciudad de durango ",
        "Centro Escolar Revolución, Sección A Gómez Farías entre Luna y Urrea, Barrio de Tierra Blanca",
        "Centro Especializado de Reintegración y Tratamiento para menores infractores (CERMI)",
        "Centro Monterrey, Nuevo León",
        "Centro Recreativo Tapias ",
        "Centro Regional de Educación para la Conservación (CRECO)",
        "Cerro de Los Remedios, Durango,Dgo.",
        "CIAC (Aquiles Serdán y Bruno Martínez)",
        "CIIDIR IPN,Calle Sigma 119 Fracc. 20 de Noviembre II",
        "Cine CITICINEMAS, Real del Mezquital 101 ",
        "Cinemex",
        "Cineteca Municipal Silvestre Revueltas. Juárez 217 Nte., Zona Centro",
        "CIUDAD DE MEXICO",
        "Ciudad del anciano",
        "CIUDAD UNIVERSITARIA, CDMX",
        "Club de Leones de Durango ",
        "COLEGIO DE BACHILLERES DEL ESTADO DE DURANGO",
        "Colegio De Ciencias Y Humanidades",
        "Colegio de Ginecología",
      ],
    };
  },
  methods: {
    getEvento(id) {
      EventosDataService.get(id)
        .then((response) => {
          this.currentEvento = response.data;
          this.getCategorias1(this.currentEvento.categorias.id);
          this.getCategorias2(this.currentEvento.subCategoria1.id);
          if(this.currentEvento.subCategoriaArte){
            this.getCategoriasArte(this.currentEvento.subCategoria2.id);
          }
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    validate() {
      this.valid = this.$refs.form.validate();
    },
    getClasificacion() {
      EventosDataService.getClasificacion()
        .then((response) => {
          this.clasificacion = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getCategorias1(clasf_id, limpiar) {
      if (limpiar == true){
        this.currentEvento.subCategoria1 = ''; 
        this.currentEvento.subCategoria2 = ''; 
        this.currentEvento.subCategoriaArte = ''; 
      }
      EventosDataService.getCategorias1(clasf_id)
        .then((response) => {
          this.categoria1 = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getCategorias2(cat_1, limpiar) {
      if (limpiar == true){
        this.currentEvento.subCategoria2 = ''; 
        this.currentEvento.subCategoriaArte = ''; 
      }
      EventosDataService.getCategorias2(cat_1)
        .then((response) => {
          this.categoria2 = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getCategoriasArte(cat, limpiar) {
      if (limpiar == true){
        this.currentEvento.subCategoriaArte = ''; 
      }
      EventosDataService.getCategoriasArte(cat)
        .then((response) => {
          this.categoriaArte = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    imprimirVal(value) {
      console.log(value);
    },
    updateEvento() {
      var data = {
        tituloEvento: this.currentEvento.tituloEvento,
        unidadResponsable: this.currentEvento.unidadResponsable,
        descripcionEvento: this.currentEvento.descripcionEvento,
        eventoDedicadoA: this.currentEvento.eventoDedicadoA,
        fechaEvento: this.currentEvento.fechaEvento,
        inicioEvento: this.currentEvento.inicioEvento,
        finEvento: this.currentEvento.finEvento,
        sede: this.currentEvento.sede,
        cupo: this.currentEvento.cupo,
        descripcion: this.currentEvento.descripcion,
        creditos: this.currentEvento.creditos,
        categorias: this.currentEvento.categorias.id,
      };
      
      if (this.currentEvento.subCategoria1 != ""){
        data.subCategoria1 = this.currentEvento.subCategoria1.id;
      }
      else {
        data.subCategoria1 = '';
      }
      if (this.currentEvento.subCategoria2 != ""){
        data.subCategoria2 = this.currentEvento.subCategoria2.id;
      }
      else {
        data.subCategoria2 = '';
      }
      if (this.currentEvento.subCategoriaArte != ""){
        data.subCategoriaArte = this.currentEvento.subCategoriaArte.id;
      }
      else {
        data.subCategoriaArte = '';
      }


      if (this.valid == true) {
        EventosDataService.update(this.currentEvento.id, data)
          .then((response) => {
            console.log(response.data);
            swal("El evento se actualizo correctamente!", "", "success");
          })
          .catch((e) => {
            console.log(e);
            swal(
              "No se pudo actualizar el evento correctamente (asegurese de llenar los campos correctamente)",
              "",
              "error"
            );
          });
      } else {
        console.log("Evento no Validado " + false);
      }
    },

    deleteEvento() {
      EventosDataService.delete(this.currentEvento.id)
        .then((response) => {
          console.log(response.data);
          swal("El evento se elimino correctamente!", "", "success");
          this.$router.push({ name: "eventos" });
        })
        .catch((e) => {
          console.log(e);
          swal("Ocurrio un error al eliminar el evento", "", "error");
        });
    },
  },
  mounted() {
    this.message = "";
    this.getEvento(this.$route.params.id);
    this.getClasificacion();
    console.log(this.$route.params.id);
  },
};
</script>

<style>
.edit-form {
  /* max-width: 800px;
  margin: auto; */
}
</style>