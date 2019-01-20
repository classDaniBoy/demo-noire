# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define mc = Character("MAIN CHARACTER")
define a = Character("Alice")
define flash = Fade(0.1,0.0,0.5, color="#fff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    show alice happy
    a "Te voy a afanar las zapatillas."
    a "NO Te voy a afanar las zapatillas."

    "Ahora vamos a proceder todos los distintos sprites de Alice, solo para mostrar que masomenos puedo hacer cosas con este framework y probar alguna que otra distinta forma de transicionar"
    show alice doubt at left 
    "esta es Alice 'dudando' a la izquierda"
    show alice teasing at right with dissolve
    "esta es Alice 'teasing' a la derecha"
    show alice happy_blush  with flash
    "esta es Alice 'blushing' a la derecha"
    "Con eso finalizan los efectos que me se por ahora vi que se pueden hacer muchos más"
    show alice worried at center with flash
    "esta es Alice 'preocupada'"
    show alice embarassed
    "esta es Alice 'embarassed'"
    show alice default
    "esta es Alice 'default'"
    # This ends the game.

    return
