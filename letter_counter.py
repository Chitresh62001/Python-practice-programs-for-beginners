# Program to find how many times each letter is repeated in a word
def count(word):
    syllables = []
    final = []
    word = word.lower()
    # (if the user only wants the repeated characters and their count)
    # (getting only the letters that are repeated and appending them in the syllables list)
    # for i in word:
    #    j = word.index(i)
    #    for k in range(int(len(word))):
    #        if j < len(word)-1:
    #            if (i == word[j+1]):
    #                syllables.append(i)
    #            j = j+1

    # (removing all the repeated entries in the syllables)
    # for element in syllables:
    #    if element not in final:
    #        final.append(element) #final consists of the repeated letters only one times

    # (Comparing each letter from final with the word and counting them)
    # for m in final:
    #    i = 0
    #    for l in word:
    #        if m == l:
    #            i = i+1
    #    print("The Letter", m, "is repeated", i, "times.")

    # (if the user wants to know how many times each character is repeated)
    for element in word:
        if element not in final:
            final.append(element)
    # (final consists of each letter in the word uniquely)
    # (Now comparing each letter from final with the word and counting them)
    for m in final:
        i = 0
        for l in word:
            if m == l:
                i = i + 1
        print("The Letter", m, "is repeated", i, "times.")


count("divinity")
