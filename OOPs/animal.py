class Animal:
    alive = True

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Rabbit(Animal):
    def sleep(self):
        print("Sleeping as a Rabbit")

    def sleep(self, hr):
        print("Sleeping for ", hr)
    pass


class Fish(Animal):
    pass


rabbit = Rabbit()
rabbit.eat()
rabbit.sleep()
rabbit.sleep(12)
