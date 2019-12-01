# from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, "home.html")


def count(request):
    fulltext = request.GET["fulltext"]
    wordsList = fulltext.split()
    word_dictionary = {}

    for word in wordsList:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    # word_dictionary = sorted(word_dictionary.items(), key=lambda k: k[1], reverse=True)
    # what i found the way

    sorted_words = sorted(
        word_dictionary.items(), key=operator.itemgetter(1), reverse=True
    )
    # this is saying go ahead and look at the count which if we're going from zero based counting like

    print(word_dictionary)

    return render(
        request,
        "count.html",
        {
            "fulltext": fulltext,
            "wordsList": len(wordsList),
            "sorted_words": sorted_words,
        },
    )
