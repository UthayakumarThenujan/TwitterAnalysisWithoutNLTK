from ntscraper import Nitter

import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

scraper = Nitter(0)

term = input("Enter the term: ")
mode = input("What mode do you want to filter (term, hashtag, user): ")
language = input("Enter the language (e.g., 'en' for English, 'es' for Spanish): ")
number = int(input("Number of tweets to scrape: "))
since = input("Since date (YYYY-MM-DD): ")
until = input("Until date (YYYY-MM-DD): ")


def get_tweets():
    tweets = scraper.get_tweets(
        '{}'.format(term),
        mode='{}'.format(mode),
        language='{}'.format(language),
        number=number,
        since='{}'.format(since),
        until='{}'.format(until),
    )

    final_tweets = []
    for x in tweets["tweets"]:
        data = [x["text"]]
        final_tweets.append(data)

    dat = pd.DataFrame(final_tweets, columns=["text"])
    return final_tweets


text = ""
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0, length):
    text = text_tweets[i][0] + " " + text
    print(text)

lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans("", "", string.punctuation))

tokenize_words = cleaned_text.split()

stop_words = [
    "i",
    "me",
    "my",
    "myself",
    "we",
    "our",
    "ours",
    "ourselves",
    "you",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "he",
    "him",
    "his",
    "himself",
    "she",
    "her",
    "hers",
    "herself",
    "it",
    "its",
    "itself",
    "they",
    "them",
    "their",
    "theirs",
    "themselves",
    "what",
    "which",
    "who",
    "whom",
    "this",
    "that",
    "these",
    "those",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "having",
    "do",
    "does",
    "did",
    "doing",
    "a",
    "an",
    "the",
    "and",
    "but",
    "if",
    "or",
    "because",
    "as",
    "until",
    "while",
    "of",
    "at",
    "by",
    "for",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "to",
    "from",
    "up",
    "down",
    "in",
    "out",
    "on",
    "off",
    "over",
    "under",
    "again",
    "further",
    "then",
    "once",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "s",
    "t",
    "can",
    "will",
    "just",
    "don",
    "should",
    "now",
]

final_words = []

for words in tokenize_words:
    if words not in stop_words:
        final_words.append(words)

print(final_words)
emotion_list = []
with open("E:\FastAPI\TwitterAnalysisWithoutNLTK\emotions.txt", "r") as file:
    for line in file:
        clear_line = line.replace("\n", "").replace(",", "").replace("'", "").strip()
        word, emotions = clear_line.split(":")

        if word in final_words:
            emotion_list.append(emotions)

w = Counter(emotion_list)

fig, axl = plt.subplots()
axl.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()
