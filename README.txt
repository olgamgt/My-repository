 IMPORTANTE: El caso base es que con el mapa 1 el robot se desplace desde un punto inicial a otro final, con cualquiera de los algoritmos


Se han implementado tres maneras distintas para que el simulador se mueva de un punto inicial a otro final, se han utilizado tres algoritmos de planificación de robots: A*, bfs y dfs. De esta manera, el robot se asegura alcanzar la meta y en algunos casos de la manera óptima. Para ello se cuenta con un fichero (busqueda.py) en que se recoge el código referente a estos algoritmos. Se ha creado una clase y diferentes métodos los cuales se invocarán desde el fichero raiz pygame-loop.py.

Para comprobar que el funcionamiento del simulador es correcto se seguirán los siguientes pasos:

	1) Se ejecuta python ./gym-csv-loop.py assets/map3.csv 2 2 10 1 estrella, de tal manera que los parámetros que se pasan son los siguientes:

		- assets/map1.csv
		- X inicial
		- Y inicial
		- X final
		- Y final
		- Metodo de planificacion: estrella, dfs, bfs

	IMPORTANTE: tener cuidado con las posiciones inicial y final para que no se salgan de las dimensiones del mapa y no se correspondan con las paredes

Extras:

	Se han creado tres mapas de las mismas dimensiones pero con distintas configuraciones:
	 	- Mapa 2: se incluye un obstaculo unido en mitad del mapa que dificulta llegar a la meta de manera trivial
		- Mapa 3: se incluyen diferentes obstaculos en medio del mapa
		- Mapa 4: simula una especie de laberinto, donde el robot tendra que seguir el camino hasta la meta
	Ademas, se han utilizado mapas de mayor dimension con diferentes configuraciones, que son:
		- Mapa 5 
		- Mapa 6
		- Mapa 7
	Videos: se han hecho tres videos con diferentes mapas para probar el funcionamiento de cada algoritmo
		- Video 1: map1_bfs --> Caso base utilizando el algoritmo bfs 
		- Video 2: map3_estrella
		- Video 3: map5_dfs
		- Video 4: map7_bfs
		- Video 5: map7_estrella 


Contenido de la carpeta:
 - Carpeta assets: cada uno de los mapas .csv
 - Carpeta videos: los videos correspondiente a cada simulacion realizada
