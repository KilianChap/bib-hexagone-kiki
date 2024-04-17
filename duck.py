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


class CanardNoir(Canard):
    def __init__(self):
        super().__init__(nom="Canard Noir", flybehavior=Fly2Wings(), quackbehavior=Quack())

class CanardBlanc(Canard):
    def __init__(self):
        super().__init__(nom="Canard Blanc", flybehavior=FlyNone(), quackbehavior=Silent())


# Exemple d'utilisation
canard_Noir = CanardNoir()
print(canard_Noir.nom)              # Output: Canard Noir
print(canard_Noir.perform_fly())    # Output: Je vole avec mes deux ailes
print(canard_Noir.perform_quack())  # Output: Je fais coin coin

canard_Blanc = CanardBlanc()
print(canard_Blanc.nom)              # Output: Canard Blanc
print(canard_Blanc.perform_fly())    # Output: Je ne peux pas voler
print(canard_Blanc.perform_quack())  # Output: Je suis silencieux
