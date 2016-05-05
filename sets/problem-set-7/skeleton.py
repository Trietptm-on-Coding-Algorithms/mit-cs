import random


class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """

    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = tuple([location[0] * 1.0, location[1] * 1.0])

    def get_number_of_species(self, animal):
        return self.species_types.get(animal, 0)

    def get_location(self):
        return self.location

    def get_species_count(self):
        return self.species_types.copy()

    def get_name(self):
        return self.name

    def adopt_pet(self, species):
        count = self.get_number_of_species(species)

        if count > 0:
            count -= 1
            if count > 0:
                self.species_types[species] = count
            else:
                del (self.species_types[species])

    def __str__(self):
        return self.name


class Adopter:
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """

    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        return self.name

    def get_desired_species(self):
        return self.desired_species

    def get_score(self, adoption_center):
        adoptable = adoption_center.get_number_of_species(self.desired_species)

        score = 1.0 * adoptable

        return score


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """

    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        score = Adopter.get_score(self, adoption_center)

        num_other = 0
        for other in self.considered_species:
            num_other += adoption_center.get_number_of_species(other)

        score += (0.3 * num_other)

        return score


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """

    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        score = Adopter.get_score(self, adoption_center)

        num_feared = adoption_center.get_number_of_species(self.feared_species)

        score -= (0.3 * num_feared)

        if score < 0:
            score = 0.0

        return score


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """

    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        num_other = 0
        for other in self.allergic_species:
            num_other += adoption_center.get_number_of_species(other)

        if num_other > 0:
            score = 0.0
        else:
            score = Adopter.get_score(self, adoption_center)

        return score


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter.
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary.
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """

    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        lowest_effectiveness = 1.0

        # print self.medicine_effectiveness

        for allergy in self.allergic_species:
            count = adoption_center.get_number_of_species(allergy)

            if count > 0:
                if allergy in self.medicine_effectiveness:
                    if self.medicine_effectiveness[allergy] < lowest_effectiveness:
                        lowest_effectiveness = self.medicine_effectiveness[allergy]
                else:
                    lowest_effectiveness = 0

        score = lowest_effectiveness * Adopter.get_score(self, adoption_center)

        return score


class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """

    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location

    def get_score(self, adoption_center):

        distance = self.get_linear_distance(adoption_center)
        num_desired = adoption_center.get_number_of_species(self.desired_species)

        if distance < 1:
            return 1.0 * num_desired
        elif distance >= 1 and distance < 3:
            return random.uniform(0.7, 0.9) * num_desired
        elif distance >= 3 and distance < 5:
            return random.uniform(0.5, 0.7) * num_desired
        elif distance >= 5:
            return random.uniform(0.1, 0.5) * num_desired

    def get_linear_distance(self, to_location):
        from math import sqrt

        adoption_location = to_location.get_location()

        x1 = self.location[0]
        y1 = self.location[1]
        x2 = adoption_location[0]
        y2 = adoption_location[1]

        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    scores = []

    for center in list_of_adoption_centers:
        score = adopter.get_score(center)
        scores.append([score, center])

    scores.sort(key=lambda x: x[1].get_name())  # sort by name
    scores.sort(key=lambda x: x[0], reverse=True)  # now sort by score

    finals = []
    for score in scores:
        finals.append(score[1])

    return finals


def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """

    scores = []

    for adopter in list_of_adopters:
        score = adopter.get_score(adoption_center)
        scores.append([score, adopter])

    scores.sort(key=lambda x: x[1].get_name())  # sort by name
    scores.sort(key=lambda x: x[0], reverse=True)  # now sort by score

    # print scores

    finals = []
    candidates = 0
    for score in scores:
        candidates += 1
        if candidates <= n:
            finals.append(score[1])

    return finals


adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four", "Cat", "Dog")
adopter5 = SluggishAdopter("Five", "Cat", (1, 2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog")

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1, 1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3, 5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2, 10))

# how to test get_adopters_for_advertisement
res = get_adopters_for_advertisement(ac2, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)

for r in res:
    print r.get_name()


    # adopter4 = FearfulAdopter("Four","Cat","Dog")
    # adopter5 = SluggishAdopter("Five","Cat", (1,2))
    # adopter6 = AllergicAdopter("Six", "Lizard", "Cat")
    #
    # ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
    # ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
    # ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
    # ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
    # ac5 = AdoptionCenter("Place5a", {"Cat": 45, "Lizard": 2}, (8,-2))
    # ac55 = AdoptionCenter("Place5c", {"Cat": 45, "Lizard": 2}, (8,-2))
    # ac555 = AdoptionCenter("Place5b", {"Cat": 45, "Lizard": 2}, (8,-2))
    # ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))
    #
    # # how to test get_ordered_adoption_center_list
    # res = get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac55, ac555, ac6])
    #
    # for r in res:
    #     print r.get_name()

    # you can print the name and score of each item in the list returned
