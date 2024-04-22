# MyuAppEconomicasAlumnos


# ScreenThree(MDScreen) --------------------------------------------------------------
# Chat Bot saludo
cadena = """
¡Hola! Soy Lexi
El Asistente Virtual de la Biblioteca. Puedes preguntarme sobre temas relacionados a las opciones del menú
"""
ChatBotMenu_hola = [cadena]

# Chat Bot munú principal
ChatBotMenu_menu = ["Menú Principal, contesto preguntas relacionadas a los temas mostrados en este menú",
                    "Institucional",     # def menu_pregunta01(self, instance)
                    "¿Qué se puede estudiar?",     # def menu_pregunta02(self, instance)
                    "¿Cómo ingreso a FCE?",     # def menu_pregunta03(self, instance)
                    "¿Querés hacer un trámite?",     # def menu_pregunta04(self, instance)
                    "Normas académicas",     # def menu_pregunta05(self, instance)
                    "Ubicar una oficina",     # def menu_pregunta06(self, instance)
                    "Dónde y cuándo curso",     # def menu_pregunta07(self, instance)
                    "Fechas de exámenes"     # def menu_pregunta08(self, instance)
]


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chat Bot pregunta 01, Institucional
ChatBotMenu_menu_preg01 = ["Institucional",
                           "Institucional",     # def menu_pregunta08_pregunta01(self, instance)
                           "Autoridades de la Facultad",     # def menu_pregunta08_pregunta02(self, instance)
                           "Secretarias",     # def menu_pregunta08_pregunta03(self, instance)
]

cadena = """
La Facultad de Ciencias Económicas es uno de los institutos fundadores de la Universidad Nacional de Cuyo.

Comenzó a funcionar el 16 de agosto de 1939 como Escuela de Ciencias Económicas, dependiente de la ex Facultad de Ciencias. Su primer Director fue el Ingeniero Edmundo G. Romero.

El 29 de noviembre de 1945, la Asamblea Universitaria inició el proceso de transformación de la Escuela de Ciencias Económicas en la Facultad de Ciencias Económicas. El proceso se completa el 10 de febrero de 1947 con la Ordenanza 197 del Rector interventor, Alfreo R. Egusquiza, a partir de dicho momento se da por inagurada la Facultad de Ciencias Económicas, tal como hoy se la conoce.

Se estableció que otorgaría los títulos de: Contador Público Nacional y Perito Partidor y el de Doctor en Ciencias Económicas, decisión que ratificó el Gobierno Nacional mediante Decreto 25621/46.

Académicamente creció muy rápido, y pocos años después de su iniciación ganó un alto prestigio nacional entre sus pares. Tiene además el orgullo de haber contado a lo largo de su historia con verdaderos maestros, excelentes investigadores, y con egresados de primer nivel, reconocidos y demandados nacional e internacionalmente desde organismos gubernamentales e instituciones bancarias, comerciales e industriales de alta jerarquía.

Por la acción de todos ellos se puede afirmar que la Facultad de Ciencias Económicas de la Universidad Nacional de Cuyo ha brindado a la Región y al País valiosos recursos humanos, y ha contribuido eficazmente con la Provincia de Mendoza mediante importantes investigaciones y múltiples tareas de extensión.

La Facultad tiene tres locaciones: la Central en el Centro Universitario del Gran Mendoza, la Sede Junín, en el Este provincial y una Delegación en la ciudad de San Rafael, al Sur de la provincia de Mendoza. En la sede central, la Facultad cuenta con un complejo edilicio de tres cuerpos: el edificio de Enseñanza, el de Gobierno y el de los Anfiteatros.

En marzo de 1996 la Delegación San Rafael inauguró sus nuevas instalaciones.
"""
ChatBotMenu_menu_preg01_preg01 = [cadena]

cadena = """
Consejo Directivo
Presidente
Cont. Miguel González Gaviola

Consejeros Profesores
Prof. Graciela Silvia Salvo; Prof. Claudio Antonio Ruotolo; Prof. Verónica Linares; Prof. Guillermo Eduardo Migliozzi; Prof. Héctor Darío Taboas; Prof. María Eugenia Godoy.

Consejero Auxiliar de Docencia 
Mgter. Diego José Liseno.

Consejeros Egresados
Juan Francisco Giménez Rinaldi; Diego Andrés Mazo Zárate.

Consejeros Estudiantes  
Luciano Martín Carrada; María Milagros Aranciva Carceller; Carlos Gastón Ferreira Ascurra.

Consejera Personal de Apoyo Académico
Cintia Melina Goméz.
"""
ChatBotMenu_menu_preg01_preg02 = [cadena]

ChatBotMenu_menu_preg01_preg03 = [("Secretarias", " "),
                                  ("Secretaría Académica", "https://fce.uncuyo.edu.ar/paginas/index/secretara-acadmica"),
                                  ("Secretaría de Posgrado,\nInvestigación e Internacionalización", "https://fce.uncuyo.edu.ar/posgrado-investigacion"),
                                  ("Secretaría de Administración y Finanzas", "https://fce.uncuyo.edu.ar/paginas/index/secretara-administrativo-financiera"),
                                  ("Secretaría de Extensión y Vinculación", "https://fce.uncuyo.edu.ar/extension-y-relaciones-institucionales"),
                                  ("Secretaría de Bienestar", "https://fce.uncuyo.edu.ar/paginas/index/secretara-de-asuntos-estudiantiles"),
]


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chat Bot pregunta 02, ¿Qué se puede estudiar?
ChatBotMenu_menu_preg02 = ["Se pueden estudiar carreras de grado, de posgrado y cursos o diplomados. Elije la opción que te interese:",
                           "Carreras de grado",     # def menu_pregunta01_pregunta01(self, instance)
                           "Carreras de posgrado",      # def menu_pregunta01_pregunta02(self, instance)
                           "Cursos y diplomados",      # def menu_pregunta01_pregunta03(self, instance)
                           "Planes de Estudio"      # def menu_pregunta01_pregunta04(self, instance)
]

ChatBotMenu_menu_preg02_preg01 = [("Las carreras de grado vigentes", " "),
                                  ("Contador Público\nsede Mendoza y San Rafael", "https://fce.uncuyo.edu.ar/estudios/carrera/contador-publico-nacional68"),
                                  ("Licenciatura en Administración\nsede Mendoza", "https://fce.uncuyo.edu.ar/estudios/carrera/licenciatura-en-administracion"),
                                  ("Licenciatura en Logística\nsede Mendoza y Junín", "https://fce.uncuyo.edu.ar/estudios/carrera/licenciatura-en-logistica"),
                                  ("Ciclo de Licenciatura en Gestión de Negocios Regionales\nSede Alver y Junín", "https://fce.uncuyo.edu.ar/estudios/carrera/licenciatura-en-gestion-de-negocios-regionales"),
                                  ("Contador Público Nacional y Perito Partidor", "https://fce.uncuyo.edu.ar/estudios/carrera/contador-publico-nacional")  
]

ChatBotMenu_menu_preg02_preg02 = [("Los posgrados vigentes", " "),
                                  ("Doctorado en Ciencias Económicas", "https://fce.uncuyo.edu.ar/estudios/posgrado/194"),
                                  ("Maestría en Gerenciamiento de\nNegocios Agroindustriales", "https://fce.uncuyo.edu.ar/estudios/posgrado/153"),
                                  ("Maestría en Gestión Integrada de\nRecursos Hídricos", "https://fce.uncuyo.edu.ar/estudios/posgrado/175"),
                                  ("Maestría en Gestión Financiera del\nSector Público", "https://fce.uncuyo.edu.ar/estudios/posgrado/193"),
                                  ("Maestría en Responsabilidad Social y\nDesarrollo Sostenible", "https://fce.uncuyo.edu.ar/estudios/posgrado/203"),
                                  ("Maestría en Administración de\nServicios de Salud", "https://fce.uncuyo.edu.ar/estudios/posgrado/201"),
                                  ("Micro Maestría en\nGerencia Pública Avanzada", "https://fce.uncuyo.edu.ar/estudios/posgrado/224"),
                                  ("Micro Maestría en\nFinanzas Públicas Aplicadas", "https://fce.uncuyo.edu.ar/estudios/posgrado/225"),
                                  ("Maestría en Administración de\nNegocios", "https://fce.uncuyo.edu.ar/estudios/posgrado/147"),
                                  ("Especialización en Gestión y\nVinculación Tecnológica", "https://fce.uncuyo.edu.ar/estudios/posgrado/176"),
                                  ("Especialización en Tributación", "https://fce.uncuyo.edu.ar/estudios/posgrado/207"),
                                  ("Especialización en Sindicatura Concursal y\nEntes en Insolvencia", "https://fce.uncuyo.edu.ar/estudios/posgrado/212"),
                                  ("Especialización en Costos y\nGestión Empresarial", "https://fce.uncuyo.edu.ar/estudios/posgrado/122")
]

ChatBotMenu_menu_preg02_preg03 = [("Las diplomaturas y cursos vigentes", " "),
                                  ("Diplomaturas y cursos", "https://fce.uncuyo.edu.ar/cursos")
]

ChatBotMenu_menu_preg02_preg04 = [("Planes de Estudio", " "),
                                  ("Contador Público Nacional y\nPerito Partidor\nPlan 1998", "https://fce.uncuyo.edu.ar/upload/oc00-006-plan-estudios-cpn-y-pp.pdf"),
                                  ("Contador Público\nPlan 2019", "https://fce.uncuyo.edu.ar/upload/ocs00662018-ratifica-cp19.pdf"),
                                  ("Licenciatura en Administración\nPlan 1998", "https://fce.uncuyo.edu.ar/upload/ocs00172000-licenciatura-en-administracion.pdf"),
                                  ("Licenciatura en Administración\nPlan 2019", "https://fce.uncuyo.edu.ar/upload/oc17-0005-aprobar-plan-de-estudios-licenciatura-en-administracion1.pdf"),
                                  ("Licenciatura en Economía\nPlan 1998", "https://fce.uncuyo.edu.ar/upload/ocs00332002-licenciatura-en-economia.pdf"),
                                  ("Licenciatura en Economía\nPlan 2019", "https://fce.uncuyo.edu.ar/upload/oc17-0006-aprobar-plan-de-estudios-licenciatura-en-economia1.pdf"),
                                  ("Licenciatura en Logística\nPlan 2017", "https://fce.uncuyo.edu.ar/upload/ocs00032016-logistica-plan-de-estudios.pdf")
]


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chat Bot pregunta 03, ¿Cómo ingreso a FCE?
ChatBotMenu_menu_preg03 = ["Las inscripciones para el ingreso 2024 ya se encuentra cerrada."]


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chat Bot pregunta 04, ¿Querés hacer un trámite?
ChatBotMenu_menu_preg04 = ["Trámites Frecuentes",
                           "Cambio de Carrera",      # def menu_pregunta03_pregunta01(self, instance)
                           "Cambio de Plan de Estudio",      # def menu_pregunta03_pregunta02(self, instance)
                           "Certificado Analítico Parcial",       # def menu_pregunta03_pregunta03(self, instance)
                           "Certificado de Alumno Regular",       # def menu_pregunta03_pregunta04(self, instance)
                           "Certificado de asistencia a exámen",       # def menu_pregunta03_pregunta05(self, instance)
                           "Pedir correo institucional",      # def menu_pregunta03_pregunta06(self, instance)
                           "Medio boleto universitario"       # def menu_pregunta03_pregunta07(self, instance)
]
cadena = """
Para cambiarte de carrera es conveniente que consultes a Dirección de Alumnos.

Te puedes comunicar con ellos:
   - Por teléfono al 449-4065
   - Por mail a diralum@fce.uncu.edu.ar
"""
ChatBotMenu_menu_preg04_preg01 = [cadena]

cadena = """
Para cambiarte de plan de estudio es conveniente que consultes a Dirección de Alumnos.

Te puedes comunicar con ellos:
   - Por teléfono al 449-4065
   - Por mail a diralum@fce.uncu.edu.ar
"""
ChatBotMenu_menu_preg04_preg02 = [cadena]

cadena = """
Actualmente solo se puede obtener por el sistema SIU GURANÍ un analítico que se emite con código QR para la validación del mismo. Seguí los siguientes pasos.

Ingresa a guaraní > Trámites > Solicitudes y constancias > Nueva solicitud >hay que rellenar tres campos:
   1. Seleccioná: Analítico descarga con/sin aplazos
   2. Presentar a: 'a quien corresponda'
   3. Observaciones: (coloca un punto), Aceptar

Te va a salir un cartel en verde que dice que se realizó con éxito.

Luego volvés a ingresar a: Trámites > Solicitudes y constancias y vas ver un listado de los pedidos, al final se va a encontrar tu pedido y al final de esa fila está un ícono de pdf, clickeas sobre él y lo vas a poder descargar.
"""
ChatBotMenu_menu_preg04_preg03 = [cadena]

cadena = """
Ahora te explico cómo pedirlo desde SIU GUARANÍ.

Ingresa a guaraní > trámites > Solicitudes y constancias > Nueva solicitud > hay que rellenar tres campos:
   1. Selecciona 'Constancia de alumno regular'
   2. Presentar a: 'a quien corresponda'
   3. Observaciones: (coloca un punto), Aceptar

Te va a salir un cartel en verde que dice que se realizó con éxito

Luego volvés a ingresar a trámites> Solicitudes y constancias y vas ver un listado de los pedidos, al final se va a encontrar tu pedido y al final de esa fila hay un ícono de pdf, clickeas sobre él y lo vas a poder descargar.
"""
ChatBotMenu_menu_preg04_preg04 = [cadena]

ChatBotMenu_menu_preg04_preg05 = [("Puedes gestionar tu Certificado de Asistencia a Examen, desde el Blog de Clases y Exámenes. Desde ahí puedes pedirlo y descargarlo. Te dejo el link a dicha entrada del Blog en el botón de abajo:", " "),
                                  ("Certificado de asistencia a exámen", "https://clasesyexamenes.blogspot.com/p/certificados.html")
]

ChatBotMenu_menu_preg04_preg06 = [("Para pedir el mail institucional ingresá tu solicitud en el siguiente formulario. En el transcurso de 24 hs recibirás un correo con las instrucciones para ingresar a la cuenta.", " "),
                                  ("Formulario Mail Institucional", "https://docs.google.com/forms/d/e/1FAIpQLSckXphFcNoPsRw8mGdW3lWWrj7drXMPafxfdc1vu2dxQsOgsA/viewform")
]

ChatBotMenu_menu_preg04_preg07 = [("Para obtener el medio boleto universitario completa el primer formulario para cargar tu solicitud en nuestros sistemas. Y dentro de las 96 horas de solicitado, descarga el certificado desde el segundo link.", " "),
                                  ("Solicitar el Medio Boleto", "https://docs.google.com/forms/d/e/1FAIpQLSc3KcpkTkZ-kWzNqChjnSbTHPK2T3P-8HYDBQFbY9UhGKLubA/viewform"),
                                  ("Descarcar certificado", "http://www.vym.mendoza.gov.ar/web/certificados/descargarCertificado.jsp")
]


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chat Bot pregunta 05, Normas académicas
ChatBotMenu_menu_preg05 = ["Te puede interesar",
                           "Que es RAM",     # def menu_pregunta04_pregunta01(self, instance)
                           "Alumno universitario",      # def menu_pregunta04_pregunta02(self, instance)
                           "Alumno activo",      # def menu_pregunta04_pregunta03(self, instance)
                           "Alumno pasivo",      # def menu_pregunta04_pregunta04(self, instance)
                           "Año académico"      # def menu_pregunta04_pregunta05(self, instance)
]

ChatBotMenu_menu_preg05_preg01 = ["El Rendimiento Académico Negativo (RAN) se produce cuando el alumno no ha logrado el rendimiento académico mínimo. Si esto sucede, la reinscripción tiene ese carácter y ese año deberá aprobar dos materias para no repetir el RAN."
]

ChatBotMenu_menu_preg05_preg02 = ["Un alumno universitario es aquel que se inscribe para cursar una carrera de grado o de pregrado y ha cumplido con las condiciones de admisibilidad."
]

ChatBotMenu_menu_preg05_preg03 = ["Un alumno activo es aquel que se reinscribe cada año en la respectiva carrera."
]

ChatBotMenu_menu_preg05_preg04 = ["Un alumno pasivo es aquel que no se reinscribe en un año académico. Sigue siendo alumno pero no puede ejercer actividad académica en ese año (no puede cursar ni rendir exámenes finales)."
]

ChatBotMenu_menu_preg05_preg05 = ["Un año académico es el período comprendido entre el 1 de abril y el 31 de marzo del año siguiente."
]


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chat Bot pregunta 06, Ubicar una oficina
ChatBotMenu_menu_preg06 = ["Ubicar una oficina",
                           "Clases y Exámenes",     # def menu_pregunta05_pregunta01(self, instance)
                           "Secretaría de Asuntos Estudiantiles",     # def menu_pregunta05_pregunta02(self, instance)
                           "SAPOE",     # def menu_pregunta05_pregunta03(self, instance)
                           "Dirección de Alumnos",     # def menu_pregunta05_pregunta04(self, instance)
                           "Biblioteca",     # def menu_pregunta05_pregunta05(self, instance)
]

ChatBotMenu_menu_preg06_preg01 = [("La Oficina de Clases y Exámenes está en planta baja del edificio de aulas. Atienden de corrido de 8hs a 20hs. Te puedes comunicar con ellos: Mail: click@fce.uncu.edu.ar o Teléfono: 449-4066", ""),
                                  ("Clases y Exámenes", "http://actividad-academica.fce.uncu.edu.ar/clayexa/clayexa.php")
]

ChatBotMenu_menu_preg06_preg02 = [("El Centro de Estudiantes (CECE) es el espacio que tenemos los y las estudiantes para poder expresarnos, participar, construir y hacer valer nuestros derechos en la comunidad educativa. Bajo la conducción actual de la Franja Morada. Nos ofrece variada de información y cursos desde sus diferentes medios de comunicación.", ""),
                                  ("Página de CECE", "https://beacons.ai/franja_morada_fce"),
                                  ("Espacio de CECE en Econet", "https://moodle.fce.uncu.edu.ar/moodle/login/index.php"),
                                  ("Instagram CECE", "https://moodle.fce.uncu.edu.ar/moodle/login/index.php"),
]

cadena = """
El SAPOE es el Servicio de Apoyo Pedagógico y Orientación al Estudiante (SAPOE) creado por la Universidad Nacional de Cuyo por medio de la Ordenanza Nª 44/1986 C.S.

Contacto y ubicación:
   - 3° Piso del Edificio de Alumnos - Facultad de Ciencias Económicas
   - TELÉFONO: 4135000 Interno 2424
   - Correo: sapoe@fce.uncu.edu.ar
   - San Rafael: sapoesr@fce.uncu.edu.ar
   - Sede Junín: sapoejunin@fce.uncu.edu.ar
"""
ChatBotMenu_menu_preg06_preg03 = [cadena]

cadena = """
Dirección de Alumnos es el encargado del registro y documentación del alumno desde su ingreso hasta su egreso.

Asimismo interviene en el control, verificación de solicitudes para cursado de materias, exámenes, etc., además de otras tareas relacionadas con la atención a alumnos.

Contacto:
   - Mail: diralum@fce.uncu.edu.ar
   - Teléfono: 4494065
   - Lunes a Viernes de 8 a 13
   - Lunes a Jueves 16:30 a 19
   - Viernes de 15 a 16:30
"""
ChatBotMenu_menu_preg06_preg04 = [cadena]

cadena = """
Biblioteca Manuel Belgrano

Contacto:
   - Mail: biblioteca@fce.uncu.edu.ar
   - Teléfono: 449-4009, Interno: 2423
   - Abierta de lunes a viernes de 8 a 14 hs. y de 15 a 19 hs.
"""
ChatBotMenu_menu_preg06_preg05 = [cadena]


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chat Bot pregunta 07, Dónde y cuando curso
ChatBotMenu_menu_preg07 = ["Podrás consultar las aulas de cursado en las pantallas de click.",
]


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chat Bot pregunta 08, Fechas de exámenes
ChatBotMenu_menu_preg08 = [("Puedes acceder a las fechas de exámenes parciales y finales a través de la siguiente página:", ""),
                           ("Información Académica", "https://fce.uncuyo.edu.ar/infoacademica")
]
