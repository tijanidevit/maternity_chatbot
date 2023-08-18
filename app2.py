import spacy
from spacy.matcher import PhraseMatcher
from spacy.matcher import Matcher
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

# Load spaCy language model
nlp = spacy.load('en_core_web_sm')

print("Hello There")

# Define common intents and patterns
# intents = {
#     "movement": ["feel", "baby's", "movement"],
#     "morning_sickness": ["manage", "morning", "sickness"],
#     "diet": ["foods", "avoid", "pregnancy"]
#     # Add more intents and patterns
# }




def get_intent(doc):
    matches = intent_matcher(doc)
    if matches:
        intent_id, start, end = matches[0]
        return nlp.vocab.strings[intent_id]
    return None

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

intents = {
    "movement": [
        ["feel", "baby's", "movement"],
        ["when", "baby", "start", "move"],
        get_synonyms("movement")
    ],
    "morning_sickness": [
        ["manage", "morning", "sickness"],
        ["how", "deal", "nausea", "pregnancy"],
        get_synonyms("morning_sickness")
    ],
    "diet": [
        ["foods", "avoid", "pregnancy"],
        ["what", "eat", "stay", "healthy", "pregnant"],
        get_synonyms("diet")
    ]
    # Add more intents and patterns
}


# Create a Matcher for intent patterns
intent_matcher = Matcher(nlp.vocab)
for intent, patterns_list in intents.items():
    for pattern in patterns_list:
        pattern_list = [{"LOWER": token.lower()} for token in pattern]
        intent_matcher.add(intent, [pattern])

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
