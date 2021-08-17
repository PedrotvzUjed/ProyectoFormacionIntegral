<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado de eventos</h2>
                <div class="col-md-12">
                    <b-table stripped hover :items = "eventos" :fields = "fields">
                        <template v-slot:cell(action)="data">
                            <b-button size="sm" variant="primary" to="{name:'EditEventos', params: {id:data.item.id}}">Editar</b-button>
                            <b-button size="sm" variant="danger">Eliminar</b-button>
                        </template>
                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    
    data(){
        return{
            fields: [
                {key: 'tituloEvento', label: 'Titulo'},
                {key: 'unidadResponsable',label: 'unidad responsable del evento'},
                {key: 'action', label: ''},
                {key: 'creditos', label:'Creditos'}
            ],
            eventos: []
        }
    },
    methods:{
        getEventos(){
            const path = 'http://localhost:8000/eventos/'
            axios.get(path).then((response)=> {
                this.eventos = response.data
            })
            .catch((error) => {
                console.log(error)
            }) 
            }

    },
    created(){
        this.getEventos()
    }
}
</script>

<style lang="css" scoped>
</style>