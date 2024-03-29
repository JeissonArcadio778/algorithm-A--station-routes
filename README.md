# Proyecto de Búsqueda A* en Python

Este proyecto implementa el algoritmo de búsqueda A* en Python para encontrar la ruta más corta entre dos puntos en un mapa de nodos conectados. El algoritmo A* es una técnica de búsqueda informada que utiliza una combinación de coste real para llegar a un nodo y una heurística que estima el coste para llegar al nodo final desde el nodo actual.

# Descripción

El algoritmo A* se utiliza ampliamente en la planificación de rutas y en juegos para encontrar el camino más eficiente entre dos puntos. En este proyecto, se implementa una versión simplificada del algoritmo para demostrar su funcionamiento en un conjunto de datos de nodos conectados con costes asociados.

## Estructura del Proyecto

El proyecto consta de los siguientes archivos:

- knowledge_base.py: Contiene la base de conocimiento con las conexiones entre los nodos y sus respectivos costes.
- index.py: Implementa el algoritmo de búsqueda A* y contiene la lógica principal del programa.
- README.md: Proporciona una descripción del proyecto y las instrucciones para su ejecución.

### Requisitos

Para ejecutar este proyecto, necesitarás tener instalado Python 3 en tu sistema. No se requieren bibliotecas externas adicionales.

## Ejecución

Para ejecutar el programa y encontrar la ruta más corta entre dos puntos, sigue estos pasos:

- Abre una terminal o línea de comandos.
- Navega hasta el directorio donde se encuentran los archivos del proyecto.
- Ejecuta el script a_star.py con el comando python a_star.py.

El programa imprimirá la mejor ruta encontrada entre el punto de partida y el destino definidos en el script.

## Personalización

Puedes modificar la base de conocimiento en knowledge_base.py para experimentar con diferentes mapas de nodos y conexiones. También puedes ajustar los puntos de partida y destino en el script a_star.py para probar diferentes rutas.

## Contribuciones

Las contribuciones al proyecto son bienvenidas. Si tienes ideas para mejorar el algoritmo o la implementación, no dudes en crear un pull request o abrir un issue.

## Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo LICENSE para obtener más detalles.