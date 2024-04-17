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
    def __init__(self, flybehavior, quackbehavior):
        self.flybehavior = flybehavior
        self.quackbehavior = quackbehavior

    def perform_fly(self):
        return self.flybehavior.fly()

    def perform_quack(self):
        return self.quackbehavior.quack()


class CanardVert(Canard):
    def __init__(self):
        super().__init__(flybehavior=Fly2Wings(), quackbehavior=Quack())

class CanardBleu(Canard):
    def __init__(self):
        super().__init__(flybehavior=FlyNone(), quackbehavior=Silent())


# Exemple d'utilisation
canard_vert = CanardVert()
print(canard_vert.perform_fly())    # Output: Je vole avec mes deux ailes
print(canard_vert.perform_quack())  # Output: Je fais coin coin

canard_bleu = CanardBleu()
print(canard_bleu.perform_fly())    # Output: Je ne peux pas voler
print(canard_bleu.perform_quack())  # Output: Je suis silencieux
