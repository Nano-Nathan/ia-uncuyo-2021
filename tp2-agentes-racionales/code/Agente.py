import random
class Agent:
    def __init__(self, env): #recibe como parámetro un objeto de la clase Environment
        #Define el tamaño del tablero
        self.maxX = env.sizeX - 1;
        self.maxY = env.sizeY - 1;
        #Define una posicion aleatoria
        self.currentX = random.randrange(env.sizeX);
        self.currentY = random.randrange(env.sizeY);
        #Avisa al tablero donde se va a encontrar
        env.move(self.currentX, self.currentY);
        #Guarda el entorno
        self.env = env;
        #Ayuda a pensar al agente
        self.isOrigin = False;
        self.moveToRight = True;
        self.endJob = False;
        #Registro de movimientos.
        self.record = [];

    #Acciones del agente
    def up(self):
        #Se mueve
        self.currentY -= 1;
        #Guarda el movimiento en el registro
        self.__save('up');
        #Envia la nueva posicion 
        self.__sendPosition();
    def down(self):
        #Se mueve
        self.currentY += 1;
        #Guarda el movimiento en el registro
        self.__save('down');
        #Envia la nueva posicion 
        self.__sendPosition();
    def left(self):
        #Se mueve
        self.currentX -= 1;
        #Guarda el movimiento en el registro
        self.__save('left');
        #Envia la nueva posicion 
        self.__sendPosition();
    def right(self):
        #Se mueve
        self.currentX += 1;
        #Guarda el movimiento en el registro
        self.__save('right');
        #Envia la nueva posicion 
        self.__sendPosition();
    def clean(self):
        #Guarda el movimiento en el registro
        self.__save('clean');
        self.env.clean();
    def idle(self):
        #Guarda el movimiento en el registro
        self.__save('idle');
        return;
    def __sendPosition (self): 
        self.env.move(self.currentX, self.currentY)
    def __save (self, action):
        if(len(self.record) > 0 and self.record[-1][1] == action):
            self.record[-1][0] += 1;
        else: 
            self.record.append([1, action]);

    def getRecord (self):
        return self.record;

    def perspective(self): #sensa el entorno
        return self.env.isDirty()

    def think(self, isDirty): # implementa las acciones a seguir por el agente
        if(isDirty):
            return self.clean;
        elif(self.endJob):
            return self.idle;
        else: 
            # Se moverá hacia la posción (0,0) y luego limpiará fila por fila
            # hasta llegar al último casillero

            #Si está o ya pasó por la posicion (0,0)
            if(self.isOrigin):
                #Si se debe mover a la derecha
                if(self.moveToRight):
                    if(self.currentX < self.maxX):
                        return self.right;
                    else:
                        self.moveToRight = False;
                        if(self.currentY < self.maxY):
                            return self.down;
                        else:
                            self.endJob = True;
                            return self.idle;
                else:
                    if(self.currentX > 0):
                        return self.left;
                    else:
                        self.moveToRight = True;
                        if(self.currentY < self.maxY):
                            return self.down;
                        else: 
                            self.endJob = True;
                            return self.idle;
            else:
                #Se mueve a la izquierda y luego arriba
                if(self.currentX > 0):
                    return self.left;
                else:
                    if(self.currentY > 0):
                        return self.up;
                    else:
                        #Llego a la posición inicial, comienza el recorrido
                        self.isOrigin = True;
                        return self.right;

    def doAction(self): #Realiza la accion
        #Obtiene si el lugar está sucio o no
        bIsDirty = self.perspective();
        #Piensa que accion llevar a cabo, dependiendo del entorno
        action = self.think(bIsDirty);
        #Realiza la accion
        action();
    
    def doActionRandom(self):
        if(self.perspective()):
            self.clean();
        else:
            action = random.randrange(4);
            if(action == 0): #Left
                if(self.currentX > 0):
                    self.left();
                else:
                    self.idle();
            elif (action == 1): #Right
                if(self.currentX < self.maxX):
                    self.right();
                else:
                    self.idle();
            elif(action == 2): #Up
                if(self.currentY > 0):
                    self.up();
                else:
                    self.idle();
            elif (action == 3): #Down
                if(self.currentY < self.maxY):
                    self.down();
                else:
                    self.idle();
                    