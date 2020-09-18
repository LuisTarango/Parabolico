from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y): #Instrucciones que lanza el proyectil cuando se hace click en direccion a los parametros dados
    "Respond to screen tap."
    if not inside(ball):            #Verifica que no exista otro proyectil en la zona de juego
        ball.x = -199               #Da la posiscion inical del proyectil para x
        ball.y = -199               #Da la posiscion inical del proyectil para y
        speed.x = (x + 200) / 17    #Da la velocidad inical del proyectil para x
        speed.y = (y + 200) / 17    #Da la velocidad inical del proyectil para y

def inside(xy): #Revisa si el parametro dado se encuentra dentro del area de juego
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200  #Revsa los rangos x y y esten dentro de la zona de juego y se regresa el resultado

def draw(): #Se encarga de dibujar y asinar color y tamano al proyectil y a los objetivos
    "Draw ball and targets."
    clear()

    for target in targets:      #Dibuja los objetivos de color azul y diametro de 20
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):            #Se dibuja el proyectil de color rojo y diametro de 6
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move(): #Hace que el proyectil se mueva de manera parabolica y que los objetivos se muevan horizontalmente por la zona de jugo
    "Move ball and targets."
    if randrange(40) == 0:          #Tiene la posiblidad de crear un nuevo objetivo si la condicion randomizada es verdadera
        y = randrange(-150, 150)    #Se randomiza una altura para que aparezca el objetivo
        target = vector(200, y)
        targets.append(target)

    for target in targets: #Dicta la magnitud del paso de los objetivos mayor magnitud mayor velocidad
        target.x -= 2.5

    if inside(ball):    #Le da al proyectil su caracteristico movimiento parabolico
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()   #Crea una copia de la lista de objetivos
    targets.clear()         #Limpia la lista de objetivos

    for target in dupe: #Revisa constantemente que el objetivo no haya sido golpeado por el proyectil, en caso de que si, este desaparece
        if abs(target - ball) > 13: #(El 13 se debe al radio del objetivo, si, el proyectil entra en este ango se marca como golpe)
            targets.append(target) #Si no es golpeado el proyectil, este continua, en caso de ser golpeado, no se agregara a la lista

    draw()

    for target in targets:  #Se asegura que el objetivo se encuentre en los limites de la zona de juego, y en caso de que salga lo regresa a su x inicial con misma altura
        if not inside(target):
            target.x=200;

    ontimer(move, 50)   #Hace que el juego progrese cadad cierto tiempo

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)  #Se registran las coordenadas del click
move()
done()
