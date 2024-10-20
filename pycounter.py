import matplotlib.pyplot as plt
from collections import Counter
import re

input_file_path = 'lahuta_e_malcise.txt'

albanian_alphabet = 'a b c ç d dh e ë f g gj h i j k l ll m n nj o p q r rr s sh t th u v x xh y z zh'.split()

letter_counter = Counter({letter: 0 for letter in albanian_alphabet})

with open(input_file_path, 'r', buffering=8192) as infile:
    for line in infile:
        cleaned_line = re.sub(r'[^a-zçë]', '', line.lower())
        letter_counter.update(cleaned_line)

filtered_counter = {letter: letter_counter[letter] for letter in albanian_alphabet}

plt.figure(figsize=(15, 8))
plt.bar(filtered_counter.keys(), filtered_counter.values(), color='blue')
plt.xlabel('Shkronjat')
plt.ylabel('Numri i paraqitjeve')
plt.title('Frekuenca e shkronjave shqipe ne tekst')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('albanian_letter_frequency.png')
plt.show()