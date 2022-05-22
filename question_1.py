"""https://stackoverflow.com/questions/72340418/cannot-generate-word-cloud-python

packages:
    https://github.com/amueller/word_cloud

word cloud:
    an image composed of words used in a particular text or subject, in which the
    size of each word indicates its frequency or importance.
"""
from collections import Counter

from wordcloud import WordCloud

import pandas as pd

import matplotlib.pyplot as plt


data = {
    "page_number": [1, 2],
    "top_words_only": [
        "people trees like instagram",
        "people yellow like flickrioapp people level water",
    ]
}

df = pd.DataFrame(data=data)

df.set_index("page_number", inplace=True)

print(df)

# option 1
# frequencies = dict([tuple(x) for x in df.top_words_only.str.split(
#     expand=True).stack().value_counts().reset_index().values])

# option 2
frequencies = Counter(w for x in df["top_words_only"] for w in x.split())

print(frequencies)

wordcloud = WordCloud()
wordcloud.generate_from_frequencies(frequencies)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
