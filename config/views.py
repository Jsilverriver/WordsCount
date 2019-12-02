from django.shortcuts import render
import operator


def homepage(request):
    return render(request, "home.html")


def count(request):
    fulltext = request.GET["fulltext"]

    number_of_words = fulltext.split()
    # = ['a', 'b', 'c']

    words_dictionary = {}

    for word in number_of_words:
        if word in words_dictionary:
            words_dictionary[word] += 1
        else:
            words_dictionary[word] = 1

    # sorted_words = sorted(words_dictionary.items(), key=lambda k: k[1], reverse=True)
    # what i found the way

    sorted_words = sorted(
        words_dictionary.items(), key=operator.itemgetter(1), reverse=True
    )

    return render(
        request,
        "count.html",
        {
            "fulltext": fulltext,
            "number_of_words": len(number_of_words),
            "sorted_words": sorted_words,
        },
    )


def about(request):
    return render(request, "about.html")
