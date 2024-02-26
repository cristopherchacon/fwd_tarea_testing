# Tarea sobre testing (pruebas) en Python

## Requerimientos

Se procederá a crear un juego con los siguientes requerimientos de usuario:

1. Solicita al jugador que ingrese su nombre. Usa su nombre para imprimir un saludo.
2. Genera una selección aleatoria entre piedra, papel o tijera y guárdalo como el número objetivo que el jugador debe adivinar.
3. Lleva un registro de cuántas partidas ha ganado cada jugador. Hazle saber cuantos turnos quedan puede ser el mejor de 5 partidas.
4. Solicita al jugador que elija entre las opciones de piedra, papel o tijera.
5. Compare ambas jugadas e imprima un mensaje segun el ganador, cuando gane el jugador entonces "El jugador1 ha ganado" y cuando gane la computadora "La computadora ha ganado".
7. Si el jugador o la computadora completan 3 partidas ganadas el juego termina ahi y se determina el ganador final.

## Resultado Esperado

1. Cuando se ejecuta el script con el comando `python game.py`, este deberia permitir jugar a un jugador y la computadora.
2. Cuando se ejecutan los tests con el comando `pytest game_test.py`, todos deberian estar en verde; Inicialmente hay dos tests en verde y 4 en rojo.


## Tips para Resolverlo

- Crear un número aleatorio en Python
  
  Puedes generar una selección aleatoria en Python con el paquete de la libreria standard llamado random. Este tiene una funcion llamada `choice` que te puede ser util.

- If statement

  En Python, puedes usar una declaración if para ejecutar código si una condición es verdadera. Por ejemplo:
```python
if condición
  # Ejecuta algún código
```

- Estructura de control while:
  
  Un bucle while en Python ejecuta un bloque de código mientras una condición sea verdadera. Por ejemplo:
```python
while condición
  # Ejecuta algún código
```

## Tests
Se recomienda este recurso para iniciar a leer acerca de los tests:

Getting started with pytest (beginner - intermediate) anthony explains
https://www.youtube.com/watch?v=mzlH8lp4ISA&ab_channel=anthonywritescode

## Material addicional

Automated Testing in Python with pytest, tox, and GitHub Actions
https://www.youtube.com/watch?v=DhUpxWjOhME&ab_channel=mCoding

## Docker

Si se usa Docker, se puede correr los siguientes comandos para ejecutar los tests:

docker build -t my-pytest-image .
docker run --rm my-pytest-image

Para ingresar al contenedor:

docker run -it my-pytest-image bash
