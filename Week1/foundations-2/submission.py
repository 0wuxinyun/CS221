import collections
import math

############################################################
# Problem 3a
# use of max for compare strings arpherically
def findAlphabeticallyLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """

    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)    
    return max([i for i in text.split()])
    # END_YOUR_CODE

############################################################
# Problem 3b

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return math.sqrt(sum([(loc1[i]-loc2[i])**2 for i in range(len(loc1))]))
# Can use Zip methods to simplify it 
    # END_YOUR_CODE

############################################################
# Problem 3c

def mutateSentences(sentence):
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be similar to the original sentence if
      - it as the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence
        (the words within each pair should appear in the same order in the output sentence
         as they did in the orignal sentence.)
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more than
        once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (reordered versions of this list are allowed)
    """
    # BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)
    # recursion:

    def eachone(now,pairs):
        if (len(now)==len(pairs)+1):
            return now
        else:
            for pair in pairs:
                if pair[0]==now[-1]:
                    return eachone(now+[pair[1]],pairs)
    # list method return NONE 

    words=sentence.lower().split(' ')
    l=len(words)
        # pair :
    pairs=[]
    for i in range(l-1):
        pairs.append([words[i],words[i+1]])
    result=[]
    result.append(sentence.lower())
    for pair in pairs:
        now=eachone(pair,pairs)
        if now is not None:
            result.append(' '.join(now))
    return list(set(result))

        
    # END_YOUR_CODE

############################################################
# Problem 3d

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    suming=0
    for k,v in v1.items():
        if k in v2:
            suming+=v*v2[k]
    return suming
    # END_YOUR_CODE

############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    for k,v in v1.items():
        if k in v2:
            v1[k]+=scale*v2[k]
    for k,v in v2.items():
        if k not in v1:
            v1[k]=scale*v2[k]
    return v1
    # END_YOUR_CODE

############################################################
# Problem 3f

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    d=collections.defaultdict(int)
    for i in text.split(" "):
        d[i]+=1
    result=[]
    for k,v in d.items():
        if v==1:
            result.append(k)
    return set(result)
        
    # END_YOUR_CODE

############################################################
# Problem 3g

def computeLongestPalindromeLength(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    # BEGIN_YOUR_CODE (our solution is 19 lines of code, but don't worry if you deviate from this)
    cache={}
    def recurrence(text,i):
        if (text,i) in cache:
            result = cache[(text,i)]
        
        elif len(text[:i+1])==0:
            if text==0:               
                result = 0
            else:
                result = len(text)
        elif text==text[::-1]:
            result =0
        else:
            delnow=1+recurrence(text[:i]+text[i+1:],i-1)
            not_delnow=recurrence(text,i-1)
            result = min(delnow,not_delnow)
        cache[(text,i)]=result
        return result
    return len(text)-recurrence(text,len(text))
    # END_YOUR_CODE
