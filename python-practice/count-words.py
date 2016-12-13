# From Udacity readiness assessment for machine learning nanodegree

"""Count words."""

"""Implement a function count_words() in Python that takes as input a string s 
and a number n, and returns the n most frequently-occuring words in s. The 
return value should be a list of tuples - the top n words paired with their 
respective counts [(<word>, <count>), (<word>, <count>), ...], sorted in 
descending count order."""

"""You can assume that all input will be in lowercase and that there will be no 
punctuations or other characters (only letters and single separating spaces). 
In case of a tie (equal count), order the tied words alphabetically."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    words = {}
    for word in s.split(' '):
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    rankedWords = []
    wordsLeft = {}
    for item in words:
        wordsLeft[item] = words[item]
    for word in words:
        maxOccurance = 0
        maxAlpha = None
        maxWord = ''
        for word2 in wordsLeft:
            if not maxAlpha:
                maxAlpha = word2
            if words[word2] > maxOccurance:
                maxOccurance = words[word2]
                maxWord = word2
            elif words[word2] == maxOccurance and word2 <= maxAlpha:
                maxAlpha = word2
                maxWord = word2
        rankedWords.append((maxWord, maxOccurance))
        del(wordsLeft[maxWord])
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = []
    for item in range(n):
        top_n.append(rankedWords[item])
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
