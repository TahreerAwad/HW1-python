import os
from os import listdir

irrelevant_word = ["\n", ".", ",", "? ", "! ", "the ", "a ", "for ", "by ", "and ", "to ", "in ",
                   "with ", "is ", "of ", "this ", "was ", "all "]

#for irwd in irrelevant_word:
#    article_data[article_num - 1] = article_data[article_num - 1].replace(irwd, " ")
#    word_list = article_data[article_num - 1].split(" ")
#    word_histogram = {}
#    for word in word_list:
#        if word not in word_histogram.keys():
#            word_histogram[word] = 1
#        else:
#            word_histogram[word] = word_histogram[word] + 1
#word_histogram.pop("")
# load all articles
articles = []
path = os.getcwd()
files = os.listdir(path)
for name in files:
    if ".txt" in name:
       print(name)
for file in files:
    file_path = os.path.join(path, file)
    f = open(path, "r")
    print(f.read())
    #with open(file_path, "r") as source:
      #  content = source.read()
    for word in irrelevant_word:
        if word.lower() in f.lower():
            f = f.replace(word, "")

        articles.append(f)

input_word = input(" Write some words to search into articles: ")

results = []

for [index, article] in enumerate(articles):
    results.append({"index": index, "count": article.count(input_word)})

top_three_article = sorted(results, key=lambda w: w["count"], reverse=True)[:3]

results_indexes = [a["index"] for a in top_three_article]

for index in results_indexes:
    print(f"{index} - {articles[index][:50]}...")