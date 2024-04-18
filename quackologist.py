class Duck:
    def fly(self):
        pass

    def quack(self):
        pass

class Goose:
    def honk(self):
        pass

class FlyWithWings:
    def fly(self):
        print("Je vole avec mes ailes !")

class FlyNoWay:
    def fly(self):
        print("Je ne peux pas voler.")

class Quack:
    def quack(self):
        print("Cancan !")

class Squeak:
    def quack(self):
        print("Couic !")

class Honk:
    def honk(self):
        print("Honnk !")

class QuackCounter(Duck):
    def __init__(self, duck):
        self.duck = duck
        self.quack_count = 0
        self.quackologist = Quackologist()  # Création d'une instance de quackologiste

    def quack(self):
        self.duck.quack()
        self.quack_count += 1
        print("Nombre de cancanements :", self.quack_count)
        # Notifier le quackologiste
        self.quackologist.update(self.duck)

class Quackologist:
    def update(self, duck):
        print("Le quackologiste a observé un canard cancaner !")

class DuckSimulator:
    def simulate(self, duck):
        duck.fly()
        duck.fly()
        duck.quack()
        duck.fly()
        duck.fly()
        duck.fly()
        duck.quack()
        duck.quack()
        duck.quack()

class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()

class RedheadDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()

class RubberDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()

class GooseAdapter(Duck):
    def __init__(self, goose):
        self.goose = goose
        self.honk_behavior = Honk()

    def fly(self):
        print("Je suis un faux canard, je ne peux pas voler.")

    def quack(self):
        self.honk_behavior.honk()

if __name__ == "__main__":
    simulator = DuckSimulator()

    mallard_duck = MallardDuck()
    redhead_duck = RedheadDuck()
    rubber_duck = RubberDuck()
    goose = GooseAdapter(Goose())

    # Ajout du compteur de cancanements aux canards
    mallard_duck = QuackCounter(mallard_duck)
    redhead_duck = QuackCounter(redhead_duck)
    rubber_duck = QuackCounter(rubber_duck)

    print("Mallard Duck Simulation:")
    simulator.simulate(mallard_duck)

    print("\nRedhead Duck Simulation:")
    simulator.simulate(redhead_duck)

    print("\nRubber Duck Simulation:")
    simulator.simulate(rubber_duck)

    print("\nGoose Simulation:")
    simulator.simulate(goose)
