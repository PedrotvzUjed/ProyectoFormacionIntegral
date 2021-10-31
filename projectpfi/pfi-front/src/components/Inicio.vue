<template>
  <v-container>
      <v-card>
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
      <v-card>
        <v-card-title>Funciones</v-card-title>
        <v-card-text>
          <ul>
            <li>La función de la coordinación de esta área en forma sistemática, asesora, orienta, revisa, integra, organiza y valida cada uno de los momentos que implica la operación del programa PIFI.</li>
            <li>Organizar y coordinar operativamente el Programa Integral de Fortalecimiento Integral.</li>
            <li>Coordinar y supervisar la reprogramación de Proyectos PIFI, con el fin de cumplir con la planeación y los compromisos establecidos en cada uno de los documentos tanto de ProDes como ProGES.</li>
            <li>Asesorar a las Unidades Académicas y áreas de Administración central sobre las reglas de operación financiera que deben seguir para el desarrollo de sus proyectos, así como asesorarlos en la elaboración y actualización del PIFI.</li>
            <li>Gestionar ante las autoridades de la SES (Subsecretaria de Educación Superior)la transferencia de partidas, así como la liberación de convenios firmados por la Universidad con la secretaria y cumplir satisfactoriamente con los mismos.</li>
            <li>Presentación del Plan de Trabajo e Informe Anual, así como proporcionar la información necesaria cuando se lleva a cabo las auditorias académicas federales, estatales e institucionales.</li>
          </ul>
        </v-card-text>
      </v-card>
      <v-card>
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
              <v-icon>mdi-domain</v-icon>
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
              <v-icon>mdi-domain</v-icon>
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
              <v-icon>mdi-domain</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-card>
      <v-card id="show">
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
              <v-col>
                <h5>Dirección:</h5>
                <p>Coordinación de Programa Integral de Fortalecimiento Institucional .</p>
                <p>Dirección de Planeación y Desarrollo Académico.</p>
                <p>Segunda planta Edificio Central.</p>
                <p>Constitución 404 sur, Zona Centro.</p>
                <p>C.P. 34000. Durango, Dgo. México.</p>
              </v-col>
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
            src: 'data:image/png;base64,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',
          },
          {
            src: 'https://www.elsoldedurango.com.mx/local/2fq0h9-ujed-durango/ALTERNATES/LANDSCAPE_1140/UJED%20Durango',
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

<style>

</style>