"Hello":"",
    "Come":"Bonjour",
    "go":"",
    "Thank you":"Merci",
    "Water":"Eau",
    "Food":"Nourriture",
    "Mother":"Mère",
    "Father":"Père",
    "sister":"Sœur",
    "brother":"Frère",
    "girl":"Fille"
    "boy":"Garçon",
    "House":"Maison",
    "Book":"Livre",
    "School":"Ecole",
    "Child":"Enfant",
    "Man":"Homme",
    "Woman":"Femme",
    "Sun":"Soleil",
    "Moon":"Lune",
    "Star":"Etoile",
    "Love":"Amour",
    "car":"Voiture"
    "clothe":"Vêtement",
    "phone":"Téléphone"
    "God":"Dieu",
    "Friend":"Ami",
    "Name":"Nom",
    "Market":"Marché"
    "good morning":"Bonjour",
    "good afternoon":"Bon après-midi",
    "good evening":"Bonsoir",
    "good night":"Bonne nuit",
}

while True:
    word = input("Enter an English word to translate to French (or type 'exit' to quit): ").strip()

    if word == "":
        print("Please enter an English word to translate to French.")
        continue

    if word.lower() == "exit":
        print("Goodbye!")
        break

    translation = dictionary.get(word)

    if translation:
        print(f"The French translation of '{word}' is '{translation}'.")
    else:
        print("Word not found in the dictionary.")