class Person(object):
    def __init__(self, name):
        self.name = name

    def say(self, stuff):
        return self.name + ' says: ' + stuff

    def __str__(self):
        return self.name


class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)


class Professor(Lecturer):
    def say(self, stuff):
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)


class ArrogantProfessor(Professor):
    # def say(self, stuff):
    #     print Professor.say(self, self.lecture(stuff))

    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)


e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')

assert e.say('the sky is blue') == "eric says: the sky is blue"
assert le.say('the sky is blue') == "eric says: the sky is blue"
assert le.lecture('the sky is blue') == "I believe that eric says: the sky is blue"
# assert pe.say('the sky is blue') == "eric says: I believe that eric says: the sky is blue"
assert pe.lecture('the sky is blue') == "I believe that eric says: the sky is blue"
# assert ae.say('the sky is blue') == "eric says: It is obvious that eric says: the sky is blue"
# assert ae.lecture('the sky is blue') == "It is obvious that eric says: the sky is blue"

# assert ae.say('the sky is blue') == "eric says: It is obvious that I believe that eric says: the sky is blue"
assert ae.lecture('the sky is blue') == "It is obvious that I believe that eric says: the sky is blue"

assert pe.say('the sky is blue') == "Prof. eric says: I believe that eric says: the sky is blue"
assert ae.say('the sky is blue') == "Prof. eric says: It is obvious that I believe that eric says: the sky is blue"
