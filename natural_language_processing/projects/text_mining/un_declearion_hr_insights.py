import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Question 1
# Get the location of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create a path from the script folder as a root that references the file relative to the script location
relative_file_path = os.path.join(script_dir, 'datasets', 'un_declaration_hr_text_data.txt')

# Read the file contents
with open(relative_file_path, 'r') as file:
    text = file.read()

# Question 2
# Get list of stopwords
nltk.download('stopwords')
stopwords_list = set(stopwords.words('english'))

# Initialize an empty dictionary
word_frequencies = {}

# Process the text and count word frequencies
for word in text.split():
    if word.lower() not in stopwords_list:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(word_frequencies)

# Plot the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Question 3
# Count frequencies of the words
words = [word.lower() for word in text.split() if word.lower() not in stopwords_list]
word_freq = Counter(words)
top_words = dict(word_freq.most_common(25))

# Plot the frequency bar
plt.figure(figsize=(10, 6))
plt.bar(top_words.keys(), top_words.values())
plt.xticks(rotation=90)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 25 Frequent Terms (excluding stopwords)')
plt.show()