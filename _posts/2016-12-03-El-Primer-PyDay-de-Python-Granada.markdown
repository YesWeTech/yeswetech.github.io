---
title:  "El primer PyDay de Python Granada"
subtitle: "Una tarde con la comunidad Python granadina"
date:   2016-12-3 19:50::00 +0530
categories: ["blog"]
author: "Marta Gómez Macías"
layout: post
image: assets/pyday/busquedaspython.jpg
---

Ayer, día 2 de Diciembre, se celebró el primer _PyDay_ de la asociación ___Python Granada___ para darse a conocer entre la comunidad local. Nosotras estuvimos allí y animamos por nuestras redes sociales a las chicas para que se acercasen. En general, hubo más público femenino de lo normal en este tipo de eventos, ¡lo cual nos encanta!

El grupo ___Python Granada___ organizó una serie de charlas sobre las que os vamos a hablar a continuación.

## Discovering Python Granada & PyConES16 Review

En primer lugar, [__Juan Antonio Fernández__](https://twitter.com/sinclair_88) presentó a la asociación ___Python Granada___. Inicialmente, explicó la historia de la asociación: fue fundada por [_Víctor Terrón_](https://twitter.com/pyctor) y [_Pablo Galindo_](https://github.com/pablogsal) porque les gustaba mucho _Python_ y querían conocer a la comunidad local que había en Granada. Ambos tuvieron que dejar la asociación debido a que se fueron de Granada pero un grupo de estudiantes de la UGR junto con varios profesionales del sector, decidieron volver a revivirla organizando este PyDay. 

Después, Juan Antonio explicó en primer lugar por qué es necesario aprender _Python_ hoy en día, la gran demanda laboral que tiene y la gran comunidad de usuarios que está empezando a tener. Para ello, nos mostró una gráfica en la que se veía como las búsquedas sobre _Python_ en _Stackoverflow_ iban aumentando con el paso del tiempo, mientras que las búsquedas de otros lenguajes como Java, iban disminuyendo.


![busquedaspython]({{ site.baseurl }}/assets/pyday/busquedaspython.jpg)

Por último, Juan Antonio concluyó su charla haciendo un pequeño resumen de la __PyConES__ celebrada este año en _Almería_. Resumió las distintas tecnologías basadas en Python sobre las que se hablaron en el evento: django, flask, pyqt, tensorflow, micropython, entre otras muchas. También mencionó los distintos paradigmas sobre los que se hablaron: deep learning, internet of things, algoritmos genéticos, aprendizaje automático, big data... Resaltando cómo se podía trabajar en todos ellos usando Python.

## Lo Bueno, Lo Feo y Lo Malo: Una Introducción a Python

Tras presentar a la asociación, fue el turno de [__Ángel Pablo Hinojosa__](https://twitter.com/psicobyte_) que hizo una pequeña introducción a _Python_ comparándolo con la película [_El bueno, el feo y el malo_](http://www.filmaffinity.com/es/film277815.html). En su charla, Ángel Pablo hizo un pequeño repaso desde los conceptos más básicos de Python: tipos de variables, listas y diccionarios; hasta los más complicados como clases y objetos, pasando por estructuras de control como bucles y condicionales.

![intropython]({{ site.baseurl }}/assets/pyday/intropython.jpg)

Para hacer la charla más amena, Ángel Pablo hizo un símil muy divertido entre la película y el lenguaje de programación, hablándonos de lo bueno, lo feo y lo malo de Python:

* Lo _bueno_ de Python es su facilidad para aprender y comprender código. Además de la gran comunidad que lo utiliza y de la gran cantidad de liberías que ya trae incorporadas.

* Lo _feo_ de Python(2) es la codificación de caracteres en _Unicode_.

* Lo _malo_ de Python es las dos versiones del lenguaje que conviven actualmente: Python2 y Python3. A pesar de que Python3 soluciona muchos de los problemas de Python2, muchos módulos no pueden ser ejecutados en Python3.

Si quieres ver las diapositivas de la presentación, las tienes disponibles en este [enlace](https://psicobyte.github.io/CharlaPyday2016).

## Cómo micropython cambió mi vida

Tras una breve introducción al lenguaje, [__Carlos Herraiz__](https://twitter.com/ciherraiz) nos contó cómo ejecutar _Python_ sobre un microcontrolador. En primer lugar, nos contó cómo había surgido _Micropython_ a través de un proyecto en kickstarter. Su creador desarrolló primero una placa que era capaz de ejecutar Python, pero debido a su alto precio, decidió diseñar Micropython para una placa más barata y usada: __ESP8266__. La gran ventaja de esta placa frente a otras como Arduino, a parte de su precio, es que incluye Wi-Fi; lo cual nos da muchísimo juego para crear dispositivos _Internet of Things_.

![micropython]({{ site.baseurl }}/assets/pyday/micropython.jpg)

Tras explicar la historia de Micropython y la placa que más se usa, Carlos hizo un ejemplo en vivo y en directo de varios scripts en Python que desarrolló en el chip. Demostró a los asistentes cómo este microchip puede ser un servidor Wi-Fi como un cliente de otro router. 

![ejemplodirecto]({{ site.baseurl }}/assets/pyday/ejemplodirecto.jpg)

Por último, Carlos concluyó explicando cómo Micropython le cambió la vida con dispositivos sencillos que lo avisaban por Twitter de tareas pendientes como, por ejemplo, regar las plantas cuando la tierra está seca, abrir la ventana cuando el nivel de humedad exceda un umbral, etc. 

El público discutió sobre la seguridad de estos dispositivos.

## Web Development With Python

Tras un breve descanso, le tocó el turno a la programación web. [__Jose Miguel López__](https://twitter.com/josemlp91) nos dio una charla sobre programación web con Python. Para introducir su charla empezó haciendo un pequeño repaso histórico de la programación web: desde el inicio de la web y el lenguaje _HTML_, pasando por lenguajes de programación que nos hacían más cómodo trabajar con HTML como _PHP_, hasta llegar a frameworks de programación que nos permiten crear aplicaciones webs como django o flask.

![web]({{ site.baseurl }}/assets/pyday/web.jpg)

Tras explicar algunos de los framework de programación web que podemos usar con Python, Jose Miguel nos demostró cómo se puede crear una aplicación web con flask en cinco minutos. Para ello, usó la web llamada [Python Anywhere](https://www.pythonanywhere.com/) para hacer un Hola Mundo.

![webdirecto]({{ site.baseurl }}/assets/pyday/webdirecto.jpg)

## Aprende a ser Dios con Algoritmos Genéticos. Paso 1: Introducción.

Tras aprender cómo se hacen aplicaciones web con Python, cambiamos el chip para hacer una pequeña introducción a los _algoritmos genéticos_ de la mano de [__Braulio Vargas__](https://twitter.com/brau_vl). En primer lugar, Braulio nos explicó que los algoritmos genéticos se basan en la _Teoría Neo-Darwiniana_ y además realizó una breve explicación de la misma de forma muy sencilla y cercana. Una vez explicadas las bases, pasó a explicar las distintas partes de un algoritmo genético: reproducción, herencia, mutación, competición y selección. 

![explicacion]({{ site.baseurl }}/assets/pyday/explicacion.jpg)

Braulio nos explicó cómo modelar la solución de nuestro algoritmo y algunos operadores de cruce y selección. Recalcó que en los algoritmos genéticos existe un compromiso entre la eficiciencia del algoritmo y la calidad de la solución que obtenemos y, además, explicó los distintos parámetros del algoritmo. También mencionó algunas aplicaciones reales que tiene.

Por último, Braulio nos proporcionó un enlace al taller de Algoritmos Genéticos hecho e impartido por [_AeroPython_](https://github.com/AeroPython/Taller-Algoritmos-Geneticos-PyConEs16) en la PyConES16 para aprender algoritmos genéticos con Python.

![tutoriales]({{ site.baseurl }}/assets/pyday/tutoriales.jpg)

Si quieres consultar las diapositivas de esta charla, están disponibles en este [enlace](https://brauliov.github.io/Aprende-a-ser-dios-con-algoritmos-geneticos/).

## Charla improvisada de Pablo Galindo

Como hemos dicho antes, [__Pablo Galindo__](https://github.com/pablogsal) fue uno de los fundadores de Python Granada y pudo asistir al evento. Los organizadores lo invitaron a dar una pequeña charla improvisada y aceptó el reto.

Así, Pablo nos contó algunas curiosidades sobre Python como el uso del operador `is`, o el truco de que una lista vacía (`[]`) se evalúa como `False`. También explicó el uso del operador `all` y vimos por qué una serie de expresiones se evaluaban como `True` o `False`. Todo esto de forma clara, rápida y muy dinámica.

![improvisada]({{ site.baseurl }}/assets/pyday/improvisada.jpg)

## Closing, seeds & PyBeers

Para cerrar el evento, [__Israel Blancas__](https://twitter.com/iblancasa) hizo una pequeña charla en un tono más relajado que el resto. En primer lugar, animó al público a participar en las distintas actividades de Python Granada y en su [grupo de telegram](https://telegram.me/pythongranada). Después, contó algunas curiosidades sobre Python e hizo algunos chistes con instrucciones del lenguaje. Por último, animó a los asistentes a presentarse a la [_Hash Code_](https://hashcode.withgoogle.com/), ya que Python Granada va a presentarse como grupo participante.

![closing]({{ site.baseurl }}/assets/pyday/closing.jpg)


## Conclusión

Tras el PyDay, algunos de los asistentes nos fuimos de cervezas :). Fue un evento muy divertido en el que se hablaron de cosas muy interesantes. La asistencia de chicas fue bastante alta, aunque no hubo ninguna ponente. 
