<template>
  <div class="submit-form">
    <v-card>
      <v-card-title> Registro de evento </v-card-title>
      <div v-if="!submitted">
        <v-container style="padding: 0px 40px 40px 40px">
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-container>
              <v-row>
                <v-col cols="12" md="6" sm="12" lg="6" xl="6">
                  <v-text-field
                    :rules="[(v) => !!v || 'Campo requerido']"
                    :counter="100"
                    label="Titulo de Evento"
                    id="tituloEvento"
                    v-model="eventos.tituloEvento"
                    name="tituloEvento"
                    required
                    outlined
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="6" sm="12" lg="6" xl="6">
                  <v-combobox
                    :rules="[(v) => !!v || 'Campo requerido']"
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

                <v-col cols="12" md="6" sm="12" lg="6" xl="6">
                  <v-textarea
                    v-model="eventos.descripcionEvento"
                    id="descripcionEvento"
                    name="descripcionEvento"
                    label="Descripción del evento"
                    :counter="200"
                    rows="2"
                    required
                    outlined
                    :rules="[(v) => !!v || 'Campo requerido']"
                  ></v-textarea>
                </v-col>

                <v-col cols="12" md="6" sm="12" lg="6" xl="6">
                  <v-text-field
                    id="eventoDedicadoA"
                    required
                    v-model="eventos.eventoDedicadoA"
                    name="eventoDedicadoA"
                    :rules="[(v) => !!v || 'Campo requerido']"
                    :counter="100"
                    label="Evento dedicado a"
                    outlined
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="4" sm="12" lg="4" xl="4">
                  <v-text-field
                    id="fechaEvento"
                    v-model="eventos.fechaEvento"
                    name="fechaEvento"
                    :rules="[(v) => !!v || 'Campo requerido']"
                    label="Fecha del evento"
                    required
                    outlined
                    type="date"
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="4" sm="6" lg="4" xl="4">
                  <v-text-field
                    id="inicioEvento"
                    required
                    v-model="eventos.inicioEvento"
                    name="inicioEvento"
                    :rules="[(v) => !!v || 'Campo requerido']"
                    label="Hora de inicio del evento"
                    outlined
                    type="time"
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="4" sm="6" lg="4" xl="4">
                  <v-text-field
                    id="finEvento"
                    required
                    v-model="eventos.finEvento"
                    name="finEvento"
                    :rules="[(v) => !!v || 'Campo requerido']"
                    label="Hora del final del evento"
                    outlined
                    type="time"
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="4" sm="6" lg="4" xl="4">
                  <v-combobox
                    v-model="eventos.sede"
                    id="sede"
                    required
                    name="sede"
                    :rules="[(v) => !!v || 'Campo requerido']"
                    :counter="100"
                    label="Sede del evento"
                    outlined
                    :items="sede"
                  ></v-combobox>
                </v-col>

                <v-col cols="12" md="4" sm="6" lg="4" xl="4">
                  <v-text-field
                    id="cupo"
                    required
                    v-model="eventos.cupo"
                    name="cupo"
                    type="number"
                    maxlength="4"
                    min="1"
                    max="1000"
                    placeholder="maximo mil personas"
                    oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
                    :rules="[(v) => !!v || 'Campo requerido']"
                    label="Cupo del evento"
                    outlined
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="4" sm="12" lg="4" xl="4">
                  <v-text-field
                    id="descripcion"
                    required
                    v-model="eventos.descripcion"
                    name="descripcion"
                    :rules="[(v) => !!v || 'Campo requerido']"
                    :counter="150"
                    label="Descripción del lugar"
                    outlined
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="6" sm="12" lg="6" xl="6">
                  <v-text-field
                    id="creditos"
                    required
                    v-model="eventos.creditos"
                    name="creditos"
                    type="number"
                    maxlength="4"
                    min="0"
                    max="10"
                    placeholder="maximo 10 creditos"
                    oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
                    :rules="[(v) => !!v || 'Campo requerido']"
                    label="Creditos otorgados en el evento"
                    outlined
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="6" sm="12" lg="6" xl="6">
                  <v-combobox
                    v-model="eventos.categorias"
                    id="categorias"
                    name="categorias"
                    :items="clasificacion"
                    label="Categoria del evento"
                    required
                    outlined
                    @change="getCategorias1($event.id)"
                    :rules="[(v) => !!v || 'Campo requerido']"
                  ></v-combobox>
                </v-col>

                <v-col v-if="eventos.categorias != ''" cols="12" md="6" sm="12" lg="6" xl="6">
                  <v-combobox
                    v-model="eventos.categorias_1"
                    :rules="[(v) => !!v || 'Campo requerido']"
                    :items="categoria1"
                    id="categorias_1"
                    name="categorias_1"
                    label="Categoria"
                    outlined
                    :counter="100"
                    required
                    @change="getCategorias2($event.id)"
                  ></v-combobox>
                </v-col>

                <v-col v-if="eventos.categorias.id != 1 && eventos.categorias_1 != '' && eventos.categorias_1.id != '18'" cols="12" md="6" sm="12" lg="6" xl="6">
                  <v-combobox
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
                  ></v-combobox>
                </v-col>



                <v-col v-else-if="eventos.categorias_1 != '' && eventos.categorias_1.id != '18'" cols="12" md="6" sm="12" lg="6" xl="6">
                  <v-combobox
                    v-model="eventos.categorias_2"
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

                <v-col v-if="eventos.categorias_2 != '' && eventos.categorias.id == 1 && eventos.categorias_2.id < 64 " cols="12" md="6" sm="12" lg="6" xl="6">
                  <v-combobox
                    v-model="eventos.categorias_arte"
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
                <button @click.prevent="saveEvento" class="btn btn-success">
                  Crear evento
                </button>
              </div>
            </v-row>
            <v-row> </v-row>
          </v-form>
        </v-container>
      </div>
      <div v-else>
        <v-container style="padding: 60px">
          <v-row>
            <button class="btn btn-success" @click="newEvento">
              Capturar otro evento
            </button>
          </v-row>
        </v-container>
      </div>
    </v-card>
  </div>
</template>

<script>
import swal from "sweetalert";
import EventosDataService from "../../services/EventosDataService";

export default {
  name: "add-evento",

  data() {
    return {
      eventos: {
        tituloEvento: "",
        unidadResponsable: "",
        descripcionEvento: "",
        eventoDedicadoA: "",
        fechaEvento: "",
        inicioEvento: "",
        finEvento: "",
        sede: "",
        cupo: "",
        descripcion: "",
        creditos: "",
        categorias: "",
        categorias_1: "",
        categorias_2: "",
        categorias_arte: "",
      },
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
      clasificacion: [],
      categoria1: [],
      categoria2: [],
      categoriaArte: [],
      submitted: false,
      valid: true,
      colors: [
        "blue",
        "indigo",
        "deep-purple",
        "cyan",
        "green",
        "orange",
        "grey darken-1",
      ],
    };
  },
  created() {
    this.getClasificacion();
  },

  methods: {
    getClasificacion() {
      EventosDataService.getClasificacion()
        .then((response) => {
          this.clasificacion = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getCategorias1(clasf_id) {
      EventosDataService.getCategorias1(clasf_id)
        .then((response) => {
          this.eventos.categorias_1 = '';
          this.eventos.categorias_2 = '';
          this.eventos.categorias_arte = '';
          this.categoria1 = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getCategorias2(cat_1) {
      EventosDataService.getCategorias2(cat_1)
        .then((response) => {
          this.eventos.categorias_2 = "";
          this.categoria2 = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getCategoriasArte(cat) {
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
    validate() {
      this.valid = this.$refs.form.validate();
    },
    saveEvento() {
      this.validate();
      if (this.valid == true) {
        this.createEvento();
      } else {
        console.log("Evento no Validado " + false);
      }
    },

    newEvento() {
      location.reload();      
    },
    createEvento() {
      var data = {
        tituloEvento: this.eventos.tituloEvento,
        unidadResponsable: this.eventos.unidadResponsable,
        descripcionEvento: this.eventos.descripcionEvento,
        eventoDedicadoA: this.eventos.eventoDedicadoA,
        fechaEvento: this.eventos.fechaEvento,
        inicioEvento: this.eventos.inicioEvento,
        finEvento: this.eventos.finEvento,
        sede: this.eventos.sede,
        cupo: this.eventos.cupo,
        descripcion: this.eventos.descripcion,
        creditos: this.eventos.creditos,
        categorias: this.eventos.categorias.id,
      };
      if (this.eventos.categorias_1 != ''){
        data.subCategoria1 = this.eventos.categorias_1.id;
      }
      if (this.eventos.categorias_2 != ''){
        data.subCategoria2 = this.eventos.categorias_2.id;
      }
      if (this.eventos.categorias_arte != ''){
        data.subCategoriaArte = this.eventos.categorias_arte.id;
      }

      EventosDataService.create(data)
        .then((response) => {
          this.submitted = true;
          swal("El evento se ha registrado correctamente!!", "", "success");
          this.createCalendario(response.data);
        })
        .catch((e) => {
          console.log(e);
          swal(
            "No se pudo registrar el evento. Verifique que lleno correctamente todos los campos.",
            "",
            "error"
          );
        });
    },

    createCalendario(dataEvento) {
      var campos = {
        name: dataEvento.tituloEvento,
        color: this.colors[this.rnd(0, this.colors.length - 1)],
        start: dataEvento.fechaEvento + " " + dataEvento.inicioEvento,
        end: dataEvento.fechaEvento + " " + dataEvento.finEvento,
        details: dataEvento.descripcionEvento,
        evento: dataEvento.id,
      };
      EventosDataService.createCalendario(campos)
        .then((response) => {
          console.log(response.data);
          this.submitted = true;
          swal("El evento se registro y agrego al calendario!!", "", "success");
        })
        .catch((e) => {
          console.log(e);
          swal("No se pudo agregar al calendario", "", "error");
        });
    },
    rnd(a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a;
    },
  },
};
</script>

<style>
</style>