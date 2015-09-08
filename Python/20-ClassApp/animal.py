class Animal:
    def __init__(self, weight, age):
        self.weight = weight
        self.age = age

    def eat(self, moreWeight, lessWeight):
        weight = self.weight + moreWeight - lessWeight
        print "weight:", weight
        return weight
