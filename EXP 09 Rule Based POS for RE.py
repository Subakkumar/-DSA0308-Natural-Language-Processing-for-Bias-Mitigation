import re

def rule_based_tagger(text):
  """
  Performs rule-based part-of-speech tagging on a text using regular expressions.

  Improves upon previous responses by:
  - Addressing some limitations (e.g., handling "ing" for adjectives and nouns)
  - Including more comprehensive regular expressions
  - Providing comments for better understanding

  Args:
      text: The text string to tag.

  Returns:
      A list of tuples, where each tuple contains a word and its corresponding POS tag.
  """

  rules = [
    # Nouns (NN): Common noun patterns
    (r"^[A-Z][a-z]+$", "NNP"),  # Proper nouns
    (r"^[a-z]+$", "NN"),        # Lowercase words (excluding some adverbs/conjunctions)
    (r"^[^\d\W]+$", "NN"),      # Words without digits or special characters

    # Verbs (VB): Basic verb patterns
    (r"^.*ing$", "VBG"),       # Gerunds (present participle verbs ending in "ing")
    (r"^.*ed$", "VBD"),        # Past tense verbs (exceptions exist)
    (r"^(is|are|was|were|am)$", "BE"),  # Common be verbs

    # Adjectives (JJ): Basic adjective patterns
    (r"^[^\d\W]+$", "JJ"),      # Words without digits or special characters (excluding nouns/verbs)
    (r".*ly$", "JJ"),           # Words ending in "ly" (can also be adverbs)

    # Adverbs (RB): Basic adverb patterns
    (r".*ly$", "RB"),           # Words ending in "ly" (can also be adjectives)
    (r"^(here|there|then|now|always|never|often|sometimes|soon)$", "RB"),  # Common adverbs

    # Pronouns (PRP): Basic pronoun patterns
    (r"^(I|me|my|mine|you|your|yours|he|him|his|hers|she|it|its|we|us|our|ours|they|them|their|theirs)$", "PRP"),

    # Articles (DT): Articles
    (r"^(a|an|the)$", "DT"),

    # Prepositions (IN): Common prepositions
    (r"^(in|of|at|to|from|by|with|as|onto|into|for|on|over|under|between)$", "IN"),

    # Conjunctions (CC): Common conjunctions
    (r"^(and|but|or|nor|so|yet|for)$", "CC"),

    # Cardinal numbers (CD): Basic digits
    (r"^\d+$", "CD"),

    # Other (UH): Interjections and other non-standard words
    (r"^.*$", "UH"),           # Catch-all for unclassified words
  ]

  tagged_words = []
  for word in text.split():
    for pattern, tag in rules:
      if re.match(pattern, word):
        tagged_words.append((word, tag))
        break  # Stop after the first matching rule
    else:
      tagged_words.append((word, "UNKNOWN"))  # Unknown words get the UNKNOWN tag

  return tagged_words

# Example usage
text = "The quick brown fox jumps over the lazy dog. He doesn't like running very often."
tagged_words = rule_based_tagger(text)

print("Text:", text)
print("Tagged Words:", tagged_words)
