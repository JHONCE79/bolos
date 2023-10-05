from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self):
        self.frames = []

    @abstractmethod
    def score(self):
        pass

class Frame:
    def __init__(self):
        self.rolls = []

    def add_roll(self, pins):
        self.rolls.append(Roll(pins))

    def score(self):
        total = 0
        for roll in self.rolls:
            total += roll.score()

        if self.is_spare():
            next_frame = self.frames[self.frames.index(self) + 1]
            total += next_frame.rolls[0].score()
        return total

    def is_spare(self):
        return len(self.rolls) == 2 and self.score() == 10


class Roll:
    def __init__(self, pins):
        self.pins = pins

    def score(self):
        return self.pins