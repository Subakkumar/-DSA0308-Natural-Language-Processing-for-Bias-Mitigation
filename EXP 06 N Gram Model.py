import random

def create_bigram_model(text):
    words = text.split()
    bigrams = {}
    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        
        if current_word not in bigrams:
            bigrams[current_word] = []
        bigrams[current_word].append(next_word)
    
    return bigrams

def generate_text(bigram_model, num_words=50, start_word=None):
    if start_word is None:
        start_word = random.choice(list(bigram_model.keys()))
    
    text = [start_word]
    
    for _ in range(num_words - 1):
        current_word = text[-1]
        if current_word in bigram_model:
            next_word = random.choice(bigram_model[current_word])
            text.append(next_word)
        else:
            break
    
    return ' '.join(text)

# Example usage
text = "I have a cat. The cat is black. It is a lovely cat."
bigram_model = create_bigram_model(text)

generated_text = generate_text(bigram_model)
print(generated_text)
