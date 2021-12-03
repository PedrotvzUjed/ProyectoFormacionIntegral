<template>
  <!-- <div class="list row">
    <div class="col-md-8">
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Buscar por titulo del evento"
          v-model="tituloEvento"/>
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button"
            @click="searchtituloEvento"
          >
            Buscar
          </button>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <h4>Lista de Eventos</h4>
      <ul class="list-group">
        <li class="list-group-item"
          :class="{ active: index == currentIndex }"
          v-for="(eventos, index) in eventos"
          :key="index"
          @click="setActiveEvento(eventos, index)"
        >
          {{ eventos.tituloEvento }}
        </li>
      </ul>

      <button class="m-3 btn btn-sm btn-danger" @click="removeAllEventos">
        Eliminar todos los eventos
      </button>
    </div>
    <div class="col-md-6">
      <div v-if="currentEvento">
        <h4>Evento</h4>
        <div>
          <label><strong>Titulo del evento: </strong></label> {{ currentEvento.tituloEvento }}
        </div>
        <div>
          <label><strong>Unidad Responsable del evento: </strong></label> {{ currentEvento.unidadResponsable }}
        </div>
        <div> 
         <label><strong>Descripcion del evento: </strong></label> 
       {{ currentEvento.descripcionEvento }}
        </div>
        <div>
          <label><strong>Evento dedicado a: </strong></label> {{ currentEvento.eventoDedicadoA }}
        </div>
         <div>
          <label><strong>Fecha del evento: </strong></label> {{ currentEvento.fechaEvento }}
        </div>
         <div>
          <label><strong>Hora de inicio del evento: </strong></label> {{ currentEvento.inicioEvento }}
        </div>
        <div>
          <label><strong>Hora del final del evento: </strong></label> {{ currentEvento.finEvento }}
        </div>
        <div>
          <label><strong>Sede del evento: </strong></label> {{ currentEvento.sede }}
        </div>
          <div>
          <label><strong>Cupo del evento: </strong></label> {{ currentEvento.cupo }}
        </div>
         <div>
          <label><strong>Descripción: </strong></label> {{ currentEvento.descripcion }}
        </div>


        


        <button type="button" class="btn btn-primary">
        <router-link :to="'/eventos/' + currentEvento.id" class="badge badge-warning">Editar informacion del evento</router-link></button>
      </div>
      <div v-else>
        <br />
        <p>Por favor selecciona un Evento para ver mas información del mismo</p>
      </div>
    </div>
  </div> -->
  <v-container>
    <v-row>
      <v-col>
        <v-data-table
          v-model="selected"
          :headers="headers"
          :items="eventos"
          :single-select="singleSelect"
          :search="search"
          @change="retrieveEventos"
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
        <v-card v-if="selected[0].tituloEvento != ''"
        elevation="8"
      >
        <v-img
          height="150"
          src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
        ></v-img>

        <v-card-title>{{ selected[0].tituloEvento }}</v-card-title>

        <v-card-text>
          <v-row>
            <label><strong>Descripcion del evento:</strong></label>
            <v-spacer></v-spacer>
            <label>{{ selected[0].descripcionEvento }}</label>
          </v-row>
          <v-row>
            <label><strong>Unidad Responsable del evento: </strong></label>
            <v-spacer></v-spacer>
            <label>{{ selected[0].unidadResponsable }}</label>
          </v-row>
          <v-row>
            <label><strong>Evento dedicado a: </strong></label>
            <v-spacer></v-spacer>
            <label>{{ selected[0].eventoDedicadoA }}</label>
          </v-row>
          <v-row>
            <v-col>
              <label><strong>Fecha del evento:</strong></label>
            </v-col>
            <v-col>
              <label> {{ selected[0].fechaEvento }}</label>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <label><strong>Hora de inicio del evento: </strong>{{ selected[0].inicioEvento }}</label>
            </v-col>
            <v-col>
              <label><strong>Hora del final del evento: </strong> {{ selected[0].finEvento }} </label>
            </v-col>
          </v-row>
          <v-row>
            <label><strong>Sede del evento:</strong></label>
            <v-spacer></v-spacer>
            <label>{{ selected[0].sede }}</label>
          </v-row>
          <v-row>
            <v-col>
              <label><strong>Cupo del evento:</strong></label>
            </v-col>
            <v-col>
              <label> {{ selected[0].cupo }}</label>
            </v-col>
          </v-row>

          <v-row>
            <label><strong>Descripción: </strong></label>
            <v-spacer></v-spacer>
            <label>{{ selected[0].descripcion }}</label>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            depressed
            color="blue-grey darken-1"
            class="white--text"
            @click="sendEvent(selected[0])"
          >
            Editar
          </v-btn>
          <v-btn
            depressed
            color="error"
            class="white--text"
            @click="deleteEvent(selected[0])"
          >
            Eliminar
          </v-btn>
        </v-card-actions>
      </v-card>

      <v-card class="align-center" elevation="8" v-else>
        <v-card-text>
          <v-row>
            <h4>Favor de seleccionar un evento para mas detalles</h4>
          </v-row>
          <v-row class="center">
            <v-btn
              loading
              text
              x-large
            ></v-btn>
          </v-row>
          
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            depressed
            disabled
            color="warning"
          >
            Editar
          </v-btn>
          <v-btn
            depressed
            disabled
            color="error"
          >
            Eliminar
          </v-btn>
        </v-card-actions>
      </v-card>
      </v-col>
    </v-row>
    
    
  </v-container>
</template>

<script>
import EventosDataService from "../../services/EventosDataService";
import swal from 'sweetalert'	

export default {
  name: "eventos-list",
  data() {
    return {
      eventos: [],
      currentEvento: null,
      currentIndex: -1,
      tituloEvento: "",
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
  methods: {
    retrieveEventos() {
      EventosDataService.getAll()
        .then(response => {
          this.eventos = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    deleteEvent(evento){
      swal({
        title: "Estas seguro de querer eliminar el evento?",
        text: "Esta acción no se puede deshacer",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          EventosDataService.delete(evento.id)
            .then(response => {
              console.log(response);
              this.retrieveEventos();
              this.selected[0].tituloEvento = '';
            })
            .catch(e => {
              console.log(e);
            })
          swal("Eliminaste el evento!", {
            icon: "success",
          });
        } else {
          swal("Parece que te arrepentiste!");
        }
      });
    },

    sendEvent(evento) {
      console.log(evento)
      this.$router.push("/fi-registro/"+evento.id);
    },

    refreshList() {
      this.retrieveEventos();
      this.currentEvento = null;
      this.currentIndex = -1;
    },

    setActiveEvento(evento, index) {
      this.currentEvento = evento;
      this.currentIndex = evento ? index : -1;
    },

    removeAllEventos() {
      EventosDataService.deleteAll()
        .then(response => {
          console.log(response.data);
          this.refreshList();
        })
        .catch(e => {
          console.log(e);
        });
    },
    
    searchtituloEvento() {
      EventosDataService.findByTitle(this.tituloEvento)
        .then(response => {
          this.eventos = response.data;
          this.setActiveEvento(null);
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.retrieveEventos();
  }
};
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>