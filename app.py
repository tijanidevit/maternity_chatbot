import spacy
from nltk.corpus import wordnet
from spacy.matcher import PhraseMatcher

# Load spaCy language model
nlp = spacy.load('en_core_web_sm')

print("Hello")

# Define common phrases and intents
phrases_to_intents = {
    "when can I feel the baby's movement": "movement",
    "how do I manage morning sickness": "morning_sickness",
    "what foods should I avoid during pregnancy": "diet",
    # Add more phrases and intents
}

# Create a PhraseMatcher
phrase_matcher = PhraseMatcher(nlp.vocab)
for phrase in phrases_to_intents.keys():
    phrase_matcher.add(phrase, None, nlp(phrase))

def get_intent(doc):
    matches = phrase_matcher(doc)
    if matches:
        match_id, start, end = matches[0]
        intent = phrases_to_intents[nlp.vocab.strings[match_id]]
        return intent
    return None

def generate_response(intent):
    if intent == "movement":
        return "You might start feeling the baby's movement around 18-25 weeks."
    elif intent == "morning_sickness":
        return "Managing morning sickness can involve eating small, frequent meals and staying hydrated."
    elif intent == "diet":
        return "It's recommended to avoid raw or undercooked seafood, unpasteurized dairy, and certain deli meats during pregnancy."
    # Add more intent-specific responses
    else:
        return "I'm sorry, I'm not sure how to help with that."

print("Maternity Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Maternity Chatbot: Goodbye!")
        break
    doc = nlp(user_input)
    intent = get_intent(doc)
    if intent:
        response = generate_response(intent)
    else:
        response = "I'm not sure what you're asking about."
    print("Maternity Chatbot:", response)
