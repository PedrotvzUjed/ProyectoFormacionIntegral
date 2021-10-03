<template>
  <div class="list row">
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
  </div>
</template>

<script>
import EventosDataService from "../../services/EventosDataService";

export default {
  name: "eventos-list",
  data() {
    return {
      eventos: [],
      currentEvento: null,
      currentIndex: -1,
      tituloEvento: ""
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