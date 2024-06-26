import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text using SpaCy
    doc = nlp(text)
    
    # Iterate over the entities recognized by SpaCy
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    
    return entities

# Example text
text = "Apple is going to build a new factory in California and plans to hire 1000 people."

# Perform Named Entity Recognition
entities = perform_ner(text)

# Print the recognized entities and their labels
for entity, label in entities:
    print(f"Entity: {entity}, Label: {label}")
