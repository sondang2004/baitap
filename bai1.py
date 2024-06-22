def mad_libs():
    # Story template with placeholders for user input
    story = """
    Once upon a time, there was a {adjective} {animal} who loved to {verb} {adverb}.
    One day, while {verb_ing} {place}, {name} found a {adjective} {object}.
    It was the most {adjective} {object} {name} had ever seen!
    """

    # Prompt the user to enter words for each placeholder
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    place = input("Enter a place: ")
    name = input("Enter a name: ")
    object_name = input("Enter an object: ")

    # Fill in the story with user input
    filled_story = story.format(adjective=adjective, animal=animal, verb=verb,
                                adverb=adverb, verb_ing=verb_ing, place=place,
                                name=name, object=object_name)

    # Print the completed Mad Libs story
    print("\nYour Mad Libs Story:\n")
    print(filled_story)

# Run the Mad Libs game
mad_libs()
