# UTFSM Survival Guide

Bienvenidos al source code de la guia de supervivencia de la USM!!!

Este repositorio es un fork del repositorio original del [CEEING](https://github.com/CEEINF-UTFSM/utfsm-survival-guide), que como está caído de hace un tiempo, además de que no hay actualizaciones desde la pandemia, decidimos volverlo a subir a internet para que la comunidad tenga acceso.

A su vez el repositorio original surge a partir de una recopilación de comentarios sobre la carrera que se puede encontrar [aquí](https://docs.google.com/document/d/1ZORkRBDfVD3lYEzETasc74sJj7cdgy6oqHFKpqUJSgc/edit).

Tenemos la intención de actualizarlo y agregarle algunas cosita. Cualquier comentario o sugerencia la pueden hacer en este repositorio en la pestaña de issues, esperamos que les sea de su agrado.

## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
    - [Archivos](#Archivos)
- [Como editar cosas pequeñas](#como-editar-cosas-pequenas)
    - [Formato de Páginas](#formato-de-paginas)
- [Como hacer cambios grandes y probarlos localmente](#como-hacer-cambios-grandes-y-probarlos-localmente)
    - [Añadir una página nueva](#anadir-una-pagina-nueva)
    - [Añadir una sección nueva](#anadir-una-seccion-nueva)
- [Agradecimientos](#agradecimientos)
    - [Créditos](#creditos)

## Estructura del Proyecto

Primero que todo, todas las páginas visibles del proyecto están escritas usando el formato [Markdown](https://es.wikipedia.org/wiki/Markdown) (el mejor formato de archivos de todos los tiempos, change my mind), pueden encontrar una guía de sintaxis en [markdownguide.org](https://www.markdownguide.org/), pero es bastante simple, es una simplificación del html, y si quieren hacer cosas más complejas de todas formas le pueden meter etiquetas del html.

Luego se ocupa [Jekyll](https://jekyllrb.com/) para transformar estos archivos en markdown a archivos html que el navegador pueda procesar. Además esta página es hosteada por [github pages](https://pages.github.com/) y la subsecuente información es un resumen de la documentación de esa wea que me tuve que leer.

Muy importante, en el proyecto hay 2 ramas, master es la rama principal y es la que se muestra al público, mientras que baby-master (c2 talf reference) es la rama de prueba donde se hacen los cambios antes de mandarlos a master, **todo cambió que se quiera hacer directamente a master será rechazado**.

### Archivos

Aquí una lista de los archivos que considero más importantese para el proyecto.

- `_data/`
    - `sidebars/`
        - `main_sidebar.yml`, esté es la tabla de contenidos donde se encuentran los semestres.
    - `topnav.yml`, aquí se encuentra el navbar de arriba en la página.
- `css/`, estilos de la página
- `images/`, todas las imágenes ocupadas
- `pages/`, aquí estan todos los archivos markdown de cada subpágina.
- `_config.yml`, configuración del jekyll (no tocar)
- `404.md`, página fallback
- `index.md`, página de introducción

## Como editar cosas pequeñas

Si quieres añadir un comentario a un curso, cambiar una descripción, poner una imagén, hacer algo pequeño, no necesitas setear nada previamente, solo tienes que editar los archivos que desees.

Para este caso los archivos disponibles para edición básica son:

- `images/`, por si quieres agregar una imagen es aquí
- `pages/`, aquí se encuentran todos los archivos markdown de las subpáginas
- `index.md`, página de inicio

### Formato de Páginas

Toda página debe seguir un formato predefinido para que funcióne bien, que se resume en:

``` md
---
title: nombre de la página en el tab del navegador
keywords: palabras clave que ayudan a la búsqueda
last_update: ultima actualización del archivo (por favor mantener actualizado)
summary: "resumen de la página que aparecera al inicio"
sidebar: main_sidebar
permalink: link que aparecera agregado al url de la página
folder: carpeta dentro de /pages, donde se encuentra el archivo markdown
---

todo el contenido de la página en formato markdown

{% include links.html %}
```

Puede ver un archivo dentro de `pages/` para ver mejor la estructura.

## Como hacer cambios grandes y probarlos localmente

Esto ya es un poco más complicado y requiere usar la consola junto con WSL o linux.

### Setup y servidor local

1. Clonar el repositorio con `git clone https://github.com/Zer0-Creativity/utfsm-survival-guide.git`.
2. Instalar [ruby](https://www.ruby-lang.org/es/), [bundler](https://bundler.io/) y [jekyll](https://jekyllrb.com/).
3. Dentro del repositorio ejecutar `bundle install`, si no funciona a la primera ocupe `sudo bundle install`.
4. Para activar un servidor local donde ver los cambios, ejecutar `bundle exec jekyll serve`

Luego el terminal te dará un link donde podrás ver la página y tus cambios en tiempo real y hacer la edición mucho más facil y dinámica.

### Añadir una página nueva

1. Cree un archivo `.md` dentro de `/pages` dentro de la carpeta correspondiente con el formato descrito en [Formato de Páginas](#formato-de-paginas).
2. Para agregar la nueva página al menú de la izquierda vaya al archivo `_data/sidebars/main_sidebar.yml`.
3. Dentro del archivo se encontrara un listado en forma de árbol del menú con el siguiente formato:

``` md
- title: nombre de la página en el menú
  url: url especificada en permalink en su archivo .md
  output: web, pdf
```

4. Añada su nueva página en la sección correspondiente y estará listo.

### Añadir una sección nueva

1. Cree una carpeta nueva dentro de `/pages` con el nombre de la sección nueva, aquí irán todas las páginas dentro de la sección.
2. Vaya a `_data/sidebars/main_sidebar.yml` para agregar la nueva sección al menú.
3. Dentro del archivo se encontrara un listado en forma de árbol del menú con el siguiente formato:

``` md
- title: nombre de la página en el menú
  url: url especificada en permalink en su archivo .md
  output: web, pdf
  subfolderitems: lista de páginas con el formato especificado en la sección anterior
```

4. Agregue su nueva sección en la posición deseada y estará listo.

## Agradecimientos

Aquí un pequeño comentario para agradecer a todas las personas que han participado de algúna u otra forma en este proyecto, desde el creador del manual original, hasta los alumnos que lo mantuvieron hasta antes de la pandemia, ahora es el turno de la siguiente generación de mantener este proyecto y luego pasar a la siguiente, y así para que este manual siga ayudando estando para futuros informaticos sansanos.

Ahora una pequeña mención a los contribuidores del proyecto a lo largo de su existencia:

### Créditos

**Contribuidores Originales**

- [BayronValenzuela](https://github.com/BayronValenzuela)
- [Mxi-C0de](https://github.com/Mxi-C0de)
- [Yhatoh](https://github.com/Yhatoh)
- [VadokDev](https://github.com/VadokDev)
- [HectorxH](https://github.com/HectorxH)
- [sofiwiwiwi](https://github.com/sofiwiwiwi)
- [pyeom](https://github.com/pyeom)
- [YorkoDev](https://github.com/YorkoDev)
- [AxlKings](https://github.com/AxlKings)
- [keleron](https://github.com/keleron)
- [Pantuflaa](https://github.com/Pantuflaa)
- [NeuronaSaturada](https://github.com/NeuronaSaturada)

**Tema Actual**

- [LuckJMG](https://github.com/LuckJMG)
- [siroale](https://github.com/siroale)
- [MoonTurtlee](https://github.com/MoonTurtlee)

