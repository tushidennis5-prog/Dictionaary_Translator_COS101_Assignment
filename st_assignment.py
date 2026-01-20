import streamlit as st

st.title("English to French Dictionary")


french_dict = {
    "hello": "Bonjour",
    "come": "Viens",
    "go": "Aller",
    "thank you": "Merci",
    "water": "Eau",
    "food": "Nourriture",
    "mother": "Mère",
    "father": "Père",
    "sister": "Sœur",
    "brother": "Frère",
    "girl": "Fille",
    "boy": "Garçon",
    "house": "Maison",
    "book": "Livre",
    "school": "École",
    "child": "Enfant",
    "man": "Homme",
    "woman": "Femme",
    "sun": "Soleil",
    "moon": "Lune",
    "star": "Étoile",
    "love": "Amour",
    "car": "Voiture",
    "clothe": "Vêtement",
    "phone": "Téléphone",
    "god": "Dieu",
    "friend": "Ami",
    "name": "Nom",
    "market": "Marché",
    "good morning": "Bonjour",
    "good afternoon": "Bon après-midi",
    "good evening": "Bonsoir",
    "good night": "Bonne nuit",
}


choice = st.selectbox("Select Language", ["French"])


# We use .lower() to make sure it matches our dictionary keys
your_word = st.text_input("Enter English word:").lower().strip()

if st.button("Search"):
    if choice == "French":
        # Using .get() is safer than square brackets as it prevents crashes if word is missing
        result = french_dict.get(your_word)
        
        if result:
            st.success(f"**French:** {result}")
        else:
            st.error("Word not found in dictionary.")