<template>
  <v-container>
    <v-row>
      <v-bottom-navigation
        color="error"
        grow
      >
        <v-btn @click="retrieveEventos()">
          <span>Todos</span>
          <v-icon active>mdi-home</v-icon>
        </v-btn>

        <v-btn @click="FiltroCategorias('1')">
          <span>Arte</span>
          <v-icon>mdi-bank</v-icon>
        </v-btn>

        <v-btn @click="FiltroCategorias('2')">
          <span>Ciencia</span>
          <v-icon>mdi-head-lightbulb</v-icon>
        </v-btn>

        <v-btn @click="FiltroCategorias('3')">
          <span>Deporte</span>
          <v-icon>mdi-run-fast</v-icon>
        </v-btn>

        <v-btn @click="FiltroCategorias('4')">
          <span>Civismo</span>
          <v-icon>mdi-badge-account-horizontal</v-icon>
        </v-btn>

        <v-btn @click="FiltroCategorias('5')">
          <span>RSU</span>
          <v-icon>mdi-school</v-icon>
        </v-btn>

        <v-btn @click="FiltroCategorias('6')">
          <span>Emprendimiento</span>
          <v-icon>mdi-account-tie</v-icon>
        </v-btn>
      </v-bottom-navigation>
    </v-row>

    <v-row>
      <v-col>
        <v-data-table
          v-model="selected"
          :headers="headers"
          :items="eventos"
          :single-select="singleSelect"
          :search="search"
          item-key="id"
          show-select
          class="elevation-8 overflow-auto"
          height="520px"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>Eventos</v-toolbar-title>
              <v-spacer></v-spacer>
                <v-text-field
                  v-model="search"
                  append-icon="mdi-magnify"
                  label="Buscar"
                  single-line
                  hide-details
                ></v-text-field>
            </v-toolbar>
          </template>
          <template v-slot:no-data>
            Espere un momento!
          </template>
        </v-data-table>
        <!-- <v-row>
          <v-btn
            depressed
            elevation="2"
            @click="sendEvent(selected)"
          >Registro y Asistencia</v-btn>
        </v-row> -->
      </v-col>
      <v-col>
        <info-Evento :evento = "selected[0]"></info-Evento>
      </v-col>
    </v-row>
    
    
  </v-container>
</template>

<script>
import EventosDataService from "../../services/EventosDataService";
import infoEvento from "../Eventos/InfoEvento";

export default {
    name: "formacionIntegral",
    data() {
      return {
        eventos: [],
        singleSelect: true,
        selected: [
          {
            tituloEvento: '',
            unidadResponsable: '',
            descripcionEvento: '',
            eventoDedicadoA:'',
            fechaEvento:'',
            inicioEvento:'',
            finEvento:'',
            sede:'',
            cupo:'',
            descripcion:'',
            creditos:'',
            categorias:'',
          }
        ],
        singleExpand: true,
        expanded: [],
        search: '',
        headers: [
          { text: 'Titulo de evento', value: 'tituloEvento' },
          { text: 'Unidad responsable', value: 'unidadResponsable' },
          { text: 'Fecha de evento', sortable: true, value: 'fechaEvento' },
          { text: 'Cupo', value: 'cupo' },
          { text: 'Creditos', value: 'creditos' },
        ],
      };
    },
    components: {
      infoEvento
    },
    methods: {
      retrieveEventos() {
        EventosDataService.getAll()
          .then(response => {
            this.eventos = response.data;
            console.log(this.eventos);
          })
          .catch(e => {
            console.log(e);
          });
      },

      FiltroCategorias(categoria){
        EventosDataService.filtroCategoria(categoria)
          .then(response => {
            this.eventos = response.data;
          })
          .catch(e => {
            console.log(e);
          })
      },
    },
    mounted() {
      
    },
    created(){
      this.retrieveEventos();
      console.log(this.ejemplo)
    }
}
</script>

<style>

</style>