<template>
  <v-container>
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
          { text: 'Id', align: 'start', sortable: true, value: 'id'},
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
/*       sendEvent(evento) {
        console.log(evento)
        this.$router.push("/fi-registro/"+evento.id);
      } */
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