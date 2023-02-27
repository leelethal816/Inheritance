# This program demonstrates polymorphism.

import f_animals as animals


def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = animals.Mammal("regular animal")
    dog = animals.Dog()
    cat = animals.Cat()
    animal_list = [mammal, dog, cat]

    # Display information about each one.
    print("Here are some animals and")
    print("the sounds they make.")
    print("--------------------------")
    for each in animal_list:
        animal_passing(each)
        print()


def animal_passing(animal):
    if isinstance(animal, animals.Mammal):
        animal.show_species()
        animal.make_sound()
    else:
        print(f"{animal} is not a mammal object")


# Call the main function.
main()
