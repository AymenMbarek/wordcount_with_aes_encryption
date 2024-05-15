from collections import defaultdict

def map_function(text):
    words = text.split()
    mapped = [(word, 1) for word in words]
    return mapped

def reduce_function(mapped_data):
    reduced = defaultdict(int)
    for word, count in mapped_data:
        reduced[word] += count
    return dict(reduced)

def word_count(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    mapped_data = map_function(text)
    reduced_data = reduce_function(mapped_data)
    
    return reduced_data

file_path = 'textfile.txt'  # Remplace par le chemin de ton fichier
word_counts = word_count(file_path)
print("Nombre de mots (par mot) :")
for word, count in word_counts.items():
    print(f"{word}: {count}")
