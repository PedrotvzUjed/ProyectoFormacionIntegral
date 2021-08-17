<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Editar Evento</h2>
            </div>
        </div>

    <div class="row">
        <div class="col">   
             <div class="card">   
                  <div class="card-body">   
                    <form @submit="onSubmit">
                        <div class="form-group row">
                            <label for="title" class="col-sm-2 col-form-label">Titulo</label>
                           
                            <div class="col-sm-6">
                                <input type="text" placeholder="Titulo del evento" name="title" class="form-control" v-model.trim="form.title">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="description" class="col-sm-2 col-form-label">Descripción del evento</label>
                            <div class="col-sm-6">
                                <textarea name="description" class="form-control" placeholder="Descripción del evento" rows="4" v-model.trim="form.description"></textarea> 
                            </div>
                        </div>

                       


            <div class="rows">
                <div class="col text-left">
                    <b-button type="submit" variant="primary">Editar</b-button>
                    <b-button type="submit" class="btn-large-space" :to="{name:'/Listeventos'}">Cancelar</b-button>
                </div>    
            </div>
                        

                    </form>
                  </div>
        </div>
        </div>
    </div>

    </div>   
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            id: this.$route.params.id,
            form:{
                title:'',
                description:''
            }
        }
    },
    methods:{
        onSubmit(evt){
            evt.preventDefault()
              const path = 'http://localhost:8000/eventos/1/'
            axios.put(path, this.form).then((response) =>{
                this.form.title = response.data.tituloEvento
                this.form.description =response.data.descripcionEvento
            alert("Evento actualizado correctamente!")
            })
            .catch((error) => {
                console.log(error)
            })
        },
        getEvento(){
            const path = 'http://localhost:8000/eventos/1/'
            axios.get(path).then((response) =>{
                this.form.title = response.data.tituloEvento
                this.form.description =response.data.descripcionEvento
            })
            .catch((error) => {
                console.log(error)
            })
        }
    }, 
    created(){
        this.getEvento() 
    }
}
</script>

<style lang="css" scoped>

</style>