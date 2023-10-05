# Clase que representa un juego de bolos
class Game:
    # Constructor que inicializa la lista de frames
    def __init__(self):
        self.frames = []

    # Método que calcula el puntaje total del juego
    def score(self):
        total = 0
        for frame in self.frames:
            total += frame.score()
        return total


# Clase que representa un frame o turno de bolos
class Frame:
    # Constructor que inicializa la lista de rolls
    def __init__(self):
        self.rolls = []

    # Método que agrega un roll a la lista de rolls
    def add_roll(self, pins):
        self.rolls.append(Roll(pins))

    # Método que calcula el puntaje del frame
    def score(self):
        total = 0
        for roll in self.rolls:
            total += roll.score()
        # Si el frame es un spare, se suma el puntaje del primer roll del siguiente frame
        if self.is_spare():
            next_frame = self.frames[self.frames.index(self) + 1]
            total += next_frame.rolls[0].score()
        return total

    # Método que determina si el frame es un spare
    def is_spare(self):
        return len(self.rolls) == 2 and self.score() == 10


# Clase que representa un roll o lanzamiento de bolos
class Roll:
    # Constructor que inicializa el número de pines derribados
    def __init__(self, pins):   
        self.pins = pins

    # Método que devuelve el puntaje del roll
    def score(self):
        return self.pins