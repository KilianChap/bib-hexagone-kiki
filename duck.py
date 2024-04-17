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

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        return "Je fais coin coin"

class Silent(QuackBehavior):
    def quack(self):
        return "Je suis silencieux"


class Canard(ABC):
    def __init__(self, nom, flybehavior, quackbehavior):
        self.nom = nom
        self.flybehavior = flybehavior
        self.quackbehavior = quackbehavior

    def perform_fly(self):
        return self.flybehavior.fly()

    def perform_quack(self):
        return self.quackbehavior.quack()


class CanardVert(Canard):
    def __init__(self):
        super().__init__(nom="Canard Vert", flybehavior=Fly2Wings(), quackbehavior=Quack())

class CanardBleu(Canard):
    def __init__(self):
        super().__init__(nom="Canard Bleu", flybehavior=FlyNone(), quackbehavior=Silent())


# Exemple d'utilisation
canard_Vert = CanardVert()
print(canard_Vert.nom)              # Output: Canard Vert
print(canard_Vert.perform_fly())    # Output: Je vole avec mes deux ailes
print(canard_Vert.perform_quack())  # Output: Je fais coin coin

canard_Bleu = CanardBleu()
print(canard_Bleu.nom)              # Output: Canard Bleu
print(canard_Bleu.perform_fly())    # Output: Je ne peux pas voler
print(canard_Bleu.perform_quack())  # Output: Je suis silencieux
