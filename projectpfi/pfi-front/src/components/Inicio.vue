<template>
  <v-container>
      <v-card >
        <v-carousel
          height="350"
          hide-delimiter-background
          show-arrows-on-hover
        >
          <v-carousel-item
            v-for="(item,i) in items"
            :key="i"
            :src="item.src"
            transition="fade-transition"
          ></v-carousel-item>
        </v-carousel>
      </v-card>
      <v-card elevation="12">
        <v-card-title>Funciones</v-card-title>
        <v-card-text>
          <ul>
            <li>Este Programa de Formación Integral del estudiante, permitirá que los egresados de la UJED cuenten con las competencias, principios y valores, para ser mujeres y hombres íntegros, con valores y actitudes para la conformación de una sociedad unida y armónica, con ideales de justicia y sean mexicanos con gran responsabilidad civil y patriotismo.</li>
            <br>
            <li>Complementar la formación de nuestros estudiantes en atención, no sólo a sus necesidades como futuros profesionistas, sino también como personas cuyo desarrollo integral implica la consideración de dimensiones conceptuales, procedimentales y actitudinales que propicien la alineación profesional, humanista, ética y tecnológica (en lo instructivo): formar profesionales competitivos, seres humanos abiertos al equilibrio y armonía del lugar donde viven, del planeta que habitamos.</li>
          </ul>
        </v-card-text>
      </v-card>
      <!-- <v-container id="botones">
        <v-row>
          <v-col>
            <v-btn
              color="blue-grey"
              x-large
              block
              dark
              outlined
              @click="selected(1)"
            >
              Información General del PIFI
              <v-icon>mdi-information</v-icon>
            </v-btn>
          </v-col>
          <v-col>
            <v-btn
              color="blue-grey"
              x-large
              block
              dark
              outlined
              @click="selected(2)"
            >
              ProDES y ProGES
              <v-icon>mdi-domain</v-icon>
            </v-btn>
          </v-col>
          <v-spacer></v-spacer>
          <v-col>
            <v-btn
              color="blue-grey"
              x-large
              block
              dark
              outlined
              target="_blank"
              href="http://transparencia.ujed.mx"
            >
              Transparencia
              <v-icon>mdi-alpha-t-box</v-icon>
            </v-btn>
          </v-col>
          <v-col>
            <v-btn
              color="blue-grey"
              x-large
              block
              dark
              outlined
              @click="selected(4)"
            >
              Contacto
              <v-icon>mdi-account-box-outline</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-container> -->
      <v-card id="show" elevation="12">
        <v-row v-if="select == 1">
          <v-card-title>INFORMACIÖN GENERAL DEL PIFI</v-card-title>
          <v-card-text>
            <h5>PIFI</h5>
            <label>El Programa Integral de Fortalecimiento Institucional (PIFI) es una estrategia de la Secretaría de Educación (SEP) para lograr que las Instituciones de Educación Superior logren mejores niveles de calidad en sus programas educativos y servicios. A través de este programa, las instituciones reciben recursos para impulsar proyectos prioritarios.</label>
            <h5>Apoyos que otorga el PIFI</h5>
            <label>La SEP otorgará a las instituciones participantes apoyo técnico para la actualización de su PIFI. Además, en función de su disponibilidad presupuestal, la SEP asignará un monto no regularizable para la realización de proyectos cuyo objetivo sea: La mejora de la calidad de los programas educativos, incluidos los programas educativos de posgrado que recibieron una evaluación positiva en la Convocatoria del Programa Nacional de Posgrados de Calidad en la vertiente del Programa de Fomento a la Calidadperior logren mejores niveles de calidad en sus programas educativos y servicios. A través de este programa, las instituciones reciben recursos para impulsar proyectos prioritarios.
              La certificación de los procesos estratégicos de gestión, en el marco de los Programas de Fortalecimiento de las Dependencias de Educación Superior registradas en el PROMEP-SES, ProDES o ProFOE, y de la Gestión, ProGES, que hayan sido dictaminados favorablemente por los comités de evaluación que para tal efecto se conformen.</label>
            <h5>Monto máximo que se puede otorgar a una Institución a través del Programa</h5>
            <label>Se puede otorgar, dependiendo de la disponibilidad presupuestal, hasta un máximo de 90 millones de pesos, en una o varias ministraciones, por cada institución del Programa Integral de Fortalecimiento Institucional (PIFI).</label>
            <h5>Instituciónes que apoya el PIFI</h5>
            <label>Comprende únicamente a instituciones de educación superior públicas, relacionadas en el numeral 4.2 de las Reglas de Operación 2011.</label>
            <h5>Objetivos Generales de PIFI</h5>
            <ul>
              <li>Promover y contribuir a la mejora y al aseguramiento de una educación superior de calidad que forme profesionistas, especialistas y profesores-investigadores capaces de aplicar, innovar y transmitir conocimientos actuales, académicamente pertinentes y socialmente relevantes en las distintas áreas y disciplinas.</li>
              <li>Consolidar en las IES los procesos de planeación estratégica participativa que den lugar a esquemas de mejora continua y aseguramiento de la calidad de sus PE y de sus más importantes procesos de gestión.</li>
              <li>Fortalecer que la actividad educativa en las IES esté centrada en el aprendizaje efectivo de los estudiantes y en el desarrollo de su capacidad de aprender a lo largo de la vida.</li>
              <li>Consolidar los procesos de autoevaluación institucional, de evaluación externa y de mejora continua de la calidad, para:
                <ul>
                  <li>Conservar la acreditación de PE de TSU o Profesional Asociado y Licenciatura que haya sido otorgada por organismos especializados reconocidos por el COPAES y/o conservar la clasificación en el nivel 1 del Padrón de Programas Evaluados por los CIEES.</li>
                  <li>Mejorar y asegurar la calidad y permanencia de los PE de posgrado que lograron su ingreso al PNPC.</li>
                  <li>Certificar, por la Norma Internacional ISO-9000:2008, los procesos académico-administrativos.</li>
                  <li>Consolidar la rendición de cuentas a la sociedad sobre su funcionamiento.</li>
                </ul>
              </li>
            </ul>
            <h5>Propósitos del PIFI</h5>
            <label>El Programa tiene como propósito mejorar la oferta educativa y servicios que ofrecen las IES Públicas, a través de la formulación de Programas Integrales de Fortalecimiento Institucional (PIFI), que permitan, entre otros aspectos:</label>
            <ul>
              <li>Colaborar con la institución en el logro de la visión y las metas que se han fijado en el PIFI.</li>
              <li>Contribuir a elevar el nivel de consolidación de los Cuerpos Académicos (CA) adscritos a cada una de las DES de la institución registradas en el Programa de Mejoramiento del Profesorado (PROMEP-SES) y sus Líneas de Generación y Aplicación del Conocimiento (LGAC) que desarrollan, con el propósito de incidir en la mejora continua de la calidad de los PE.</li>
              <li>Atender las recomendaciones académicas que los CIEES han formulado a las IES para mejorar la calidad de los PE que ofrecen, que les permitan lograr la acreditación por organismos reconocidos por el COPAES y mejorar su gestión y administración en congruencia con las políticas públicas que para tal efecto establezca la SEP; así como las recomendaciones hechas por los Comités Externos de Evaluación a los programas de posgrado en el marco del PNPC SEP-CONACyT.</li>
              <li>Actualizar los planes y programas de estudio para que fomenten su pertinencia y su flexibilización curricular, incorporando el resultado de los estudios de seguimiento de egresados y empleadores.</li>
              <li>Impulsar y fortalecer la internacionalización de la educación superior, a través del establecimiento de redes internacionales de cooperación en las funciones sustantivas, el intercambio académico, la movilidad estudiantil y de académicos, el establecimiento de sistemas de acreditación de estudios, entre otros aspectos.</li>
              <li>Impulsar y fortalecer la innovación educativa para mejorar la calidad, incorporando enfoques y modelos educativos centrados en el aprendizaje, la actualización y flexibilidad curricular, entre otros aspectos.</li>
              <li>Impulsar la formación en valores como parte de la atención y formación integral del estudiante.</li>
              <li>Impulsar la educación ambiental para el desarrollo sustentable a través de la oferta educativa relacionada con el medio ambiente.</li>
              <li>Mejorar integralmente el proceso de enseñanza-aprendizaje.</li>
              <li>Mejorar los sistemas e instrumentos de las IES para la evaluación de los aprendizajes alcanzados por los estudiantes</li>
              <li>Fortalecer académicamente altos grados de formación académica, con programas cohesionados que eviten la fragmentación del saber y enfatizar los estudios de doctorado sobre todo en la modalidad directa.</li>
              <li>Fortalecer los programas institucionales de tutoría individual o en grupo de estudiantes, de seguimiento de egresados, de trayectoria, de retención, orientación educativa y titulación oportuna de estudios mediante una metodología apropiada, así como la prevención y atención de las adicciones, entre otros aspectos, que propicien una mejor atención y seguimiento de los alumnos por parte de las IES.</li>
              <li>Adecuar la normativa de la IES para su mejor funcionamiento.</li>
              <li>Desarrollar los sistemas integrales de información (del ejercicio y control presupuestal, control escolar y recursos humanos), que apoyen los procesos de planeación, autoevaluación, acreditación de programas y certificación de los procesos estratégicos de gestión institucionales.</li>
              <li>Ampliar y modernizar continuamente la infraestructura académica de laboratorios, aulas, talleres, plantas piloto, centros de lenguas extranjeras, cómputo y bibliotecas, para que los CA de las DES registradas en el PROMEP-SES y sus alumnos y alumnas cuenten con mejores condiciones para su trabajo académico, que permitan lograr la acreditación de los PE.</li>
              <li>Realizar reformas de carácter estructural en la IES que incidan en un mejor funcionamiento y viabilidad institucional.</li>
              <li>Apoyar objetivos de proyectos integrales por DES o por PE que fomenten la mejora de los PE de posgrado que estén registrados en el PNPC.</li>
              <li>Fomentar una política transversal de equidad de género entre personal administrativo, profesores y estudiantes.</li>
              <li>Fortalecer la vinculación de las IES con el entorno social.</li>
              <li>Impulsar el fortalecimiento junto con el CONACyT y las demás IES fundadoras, del Consorcio Nacional de Recursos de Información Científica y Tecnológica que busque optimizar recursos para que las IES participantes sean beneficiadas para acceder a bases de datos y revistas electrónicas, con el propósito de fomentar la cultura digital y tener acceso al conocimiento de vanguardia.</li>
            </ul>
          </v-card-text>
        </v-row>
        <v-row v-if="select == 2">
          <v-card-title>ORGANIZACIÓN DE LOS PRODES Y PROGES DE LA UJED</v-card-title>
          <v-card-text>
            <h5>ProDES</h5>
            <label>Son los Programas de Fortalecimiento de las Dependencias de Educación Superior (DES), documento en el que se señala el proceso de actualización de la planeación y la programación de las mismas, cuyo propósito es el de mejorar la oferta educativa y los servicios que ofrecen las DES,</label>
            <h5>ProGES</h5>
            <label>Es el Programa de Fortalecimiento de la Gestión Institucional (ProGES), documento en el que se consigna el resultado del proceso de actualización de la planeación y programación de la gestión, encaminado a mejorar la calidad de los servicios de la gestión Institucional para:</label>
            <ul>
              <li>Certificar los procesos estratégicos de gestión.</li>
              <li>Mejorar y aprovechar el SIIA para un correcto funcionamiento institucional.</li>
              <li>Aprovechar la capacidad física, creación de nuevos espacios y en su caso, para las obras que presentan retraso en su construcción.</li>
              <li>Resolver los problemas estructurales.</li>
              <li>Rendir cuentas.</li>
              <li>Aprovechar las plazas de PTC existentes y para la creación de nuevas plazas.</li>
              <li>Fomentar la perspectiva de género.</li>
              <li>Atender a las recomendaciones de los CIEES.</li>
            </ul>
          </v-card-text>
        </v-row>
        <v-row v-if="select == 4">
          <v-card-title>Contacto</v-card-title>
          <v-card-text>
            <v-row>
              <h5>Dirección:</h5>
              <p>Coordinación de Programa Integral de Fortalecimiento Institucional. Dirección de Planeación y Desarrollo Académico. Segunda planta Edificio Central. </p>
              <p>Constitución 404 sur, Zona Centro. C.P. 34000. Durango, Dgo. México.</p>
            </v-row>
            <v-row>
              <v-col>
                <h5>Teléfono:</h5>
                <p>+52 (618) 827-1248</p>
                <p>+52 (618) 812-0044 Ext. 133</p>
              </v-col>
              <v-col>
                <h5>Correo electronico:</h5>
                <label>xcruz@ujed.mx</label>
              </v-col>
            </v-row>
          </v-card-text>
        </v-row>
      </v-card>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        select: 0,
        items: [
          {
            src: 'https://www.elsoldedurango.com.mx/local/2fq0h9-ujed-durango/ALTERNATES/LANDSCAPE_1140/UJED%20Durango',
          },
          {
            src: 'https://www.elsoldedurango.com.mx/local/cd8owg-presentara-ujed-denuncia-ante-fiscalia-anticorrupcion-por-desvio-de-recursos.jpeg/ALTERNATES/LANDSCAPE_768/Presentar%C3%A1%20UJED%20denuncia%20ante%20Fiscal%C3%ADa%20Anticorrupci%C3%B3n%20por%20desv%C3%ADo%20de%20recursos.jpeg',
          },
          {
            src: 'https://www.elsoldedurango.com.mx/local/nza52q-estudiantes-ujed/ALTERNATES/LANDSCAPE_1140/Estudiantes%20UJED',
          },
          {
            src: 'https://www.elsoldedurango.com.mx/local/qt4jme-ujed.jpeg/ALTERNATES/LANDSCAPE_768/UJED.jpeg',
          },
        ],
      }
    },
    methods: {
      selected(num){
        this.select = num;
        setTimeout(this.scrollView, 100);  
        
      },
      scrollView(){
        const el = this.$el.querySelector("#show");
        if (el) {
          el.scrollIntoView();
        }
      }
    }
  }
</script>

<style scoped>
  .v-card__text {
    padding: 40px;
  }
  .v-card__text > label{
    margin-bottom: 25px;
  }
  .v-card__text > h5 {
    color: #a4010b;
  }
  .v-card__title {
    color: #a4010b;
    margin-left: 10px;
    margin-right: 10px;
  }
  .v-card{
    margin-bottom: 20px;
  }
  #botones{
    margin-bottom: 20px;
  }
</style>
