# Alternate way of finding duplicate letters in a word (ONLY THE FIRST FOR IS DIFFERENT REST IS SAME AS LETTER_COUNTER)
def count(word):
    l1 = []
    l2 = []
    l3 = []
    word = word.lower()

    # if the user onlys wants the repeated characters
    # (getting only the letters that are repeated and appending them in the syllables list)
    for i in word:
        l3.append(i)
        for j in l3[l3.index(i)+1:len(l3)]:
            if (i == j):
                l1.append(i)
                # removing cause it will always take the index of first letter repeated
                l3.remove(i)

    # (removing all the repeated entries in the syllables)
    for m in l1:
        if m not in l2:
            l2.append(m)  # l2 consists of the repeated letters only one times

    # (Comparing each letter from l2 with the word and counting them)
    for k in l2:
        i = 0
        for letter4 in word:
            if k == letter4:
                i = i + 1
        print("The Letter", k, "is repeated", i, "times.")


count("divinity")
