from abc import ABC, abstractmethod

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class Fly2Wings(FlyBehavior):
    def fly(self):
        return "Je vole avec mes deux ailes"

class FlyNone(FlyBehavior):
    def fly(self):
        return "Je ne peux pas voler"


class Canard(ABC):
    def __init__(self, flybehavior):
        self.flybehavior = flybehavior

    def perform_fly(self):
        return self.flybehavior.fly()

class CanardVert(Canard):
    def __init__(self):
        super().__init__(flybehavior=Fly2Wings())

class CanardBleu(Canard):
    def __init__(self):
        super().__init__(flybehavior=FlyNone())


# Exemple d'utilisation
canard_vert = CanardVert()
print(canard_vert.perform_fly())  # Output: Je vole avec mes deux ailes

canard_bleu = CanardBleu()
print(canard_bleu.perform_fly())  # Output: Je ne peux pas voler
