from random import choice

nGramSize = 3
markovSize = int(450 / nGramSize)
with open('source.txt', 'r', encoding='UTF-8') as source:
    with open('output.txt', 'w', encoding='UTF-8') as thingy:
        thingy.write('')

    text = source.read()

    tmpGram = []
    Grams = {}

    for i, char in enumerate(text):       # puts every nGramSize sequential characters into a list.
        for j in range(nGramSize):
            try:
                tmpGram.append(text[i+j])
            except IndexError:
                tmpGram = []
        Grams[''.join(tmpGram)] = []
        tmpGram.clear()

    textList = list(text)
    for Gram in Grams:
        for i, char in enumerate(textList):
            checkGram = []
            for j in range(nGramSize):      # we need to find every instance of the n-gram in the text, so we search through it
                try:
                    checkGram.append(textList[i+j])
                except IndexError:
                    checkGram = []
            if Gram == ''.join(checkGram):      # if the current bit of text we are searching is the n-gram, find the next n-gram after it and add it to the dictionary
                nextGram = []
                for k in range(nGramSize):
                    try:
                        nextGram.append(textList[i+k+nGramSize])
                    except IndexError:
                        nextGram = []
                nextGram = ''.join(nextGram)
                Grams[Gram].append(nextGram)

    try:        # just choose a random n-gram to start us off
        nextItem = (choice(list(Grams)))
    except KeyError:
        nextItem = []

    while markovSize > 0:
        nextItem = (choice(Grams[nextItem]))        # then take that n-gram, choose a random n-gram that can possibly come after it, then write it to output.
        with open('output.txt', 'a', encoding='UTF-8') as file:
            file.write(nextItem)

        markovSize -= 1
