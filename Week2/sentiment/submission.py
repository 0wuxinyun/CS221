#!/usr/bin/python

import random
import collections
import math
import sys
from util import *
import numpy as np

############################################################
# Problem 3: binary classification
############################################################

############################################################
# Problem 3a: feature extraction

def extractWordFeatures(x):
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    result=collections.defaultdict(int)
    for i in set(x.split()):
        result[i]=x.split().count(i)
    return result
# Improvement :
'''Faster: set first then count'''
    # END_YOUR_CODE

############################################################
# Problem 3b: stochastic gradient descent

def learnPredictor(trainExamples, testExamples, featureExtractor, numIters, eta):
    '''
    Given |trainExamples| and |testExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of iterations to
    train |numIters|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement stochastic gradient descent.

    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and testExamples
    to see how you're doing as you learn after each iteration.
    '''
    weights = collections.defaultdict(int)  # feature => weight
    # BEGIN_YOUR_CODE (our solution is 12 lines of code, but don't worry if you deviate from this)
    # get data x train:
    def loss(x,y,w):
        pre=0
        for feature,value in x.items():
            pre+=value*w[feature]
        return max(0,1-pre*y)
        
    def all_loss(x,y,w):
        result=0
        for i in range(len(x)):
            result+=loss(x[i],y[i],w)
        return result
    Xt=[]
    Y=[]
    Xtest=[]
    Yt=[]
    for i in trainExamples:
        Xt.append(featureExtractor(i[0]))
        Y.append(i[1])
    for i in testExamples:
        Xtest.append(featureExtractor(i[0]))
        Yt.append(i[1])

    for i in range(100):
        for num in range(len(Y)):
            lossv=loss(Xt[num],Y[num],weights)
            if lossv!=0:
                for feature,value in Xt[num].items():
                    gradient=-eta*Y[num]*value
                    weights[feature]-=gradient
        print('iteration {}: train Error = {}, test error = {}'.format(i,all_loss(Xt,Y,weights), all_loss(Xtest,Yt,weights)))
    return weights

############################################################
# Problem 3c: generate test case

def generateDataset(numExamples, weights):
    '''
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    '''
    random.seed(42)
    # Return a single example (phi(x), y).
    # phi(x) should be a dict whose keys are a subset of the keys in weights
    # and values can be anything (randomize!) with a nonzero score under the given weight vector.
    # y should be 1 or -1 as classified by the weight vector.
    def generateExample():
        # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
        phi=collections.defaultdict()
        pre=0
        for feature,value in weights.items():
            n=random.random()
            if n<0.4:
                phi[feature]=random.randrange(100)
                pre+=phi[feature]*value
                
        y=np.sign(pre)
        # END_YOUR_CODE
        return (phi, y)
# random.choice(list)
    return [generateExample() for _ in range(numExamples)]

############################################################
# Problem 3e: character features

def extractCharacterFeatures(n):
    '''
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces mapped to their n-gram counts.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    '''
    def extract(x):
        # BEGIN_YOUR_CODE (our solution is 6 lines of code, but don't worry if you deviate from this)
        inputs=list(x.replace(' ',''))
        result=collections.defaultdict(int)
        for i in range(n-1,len(inputs)):
            result[''.join(inputs[i-n+1:i+1])]+=1
# zip*           
        return dict(result)
        # END_YOUR_CODE
    return extract

############################################################
# Problem 4: k-means
############################################################


def kmeans(examples, K, maxIters):
    '''
    examples: list of examples, each example is a string-to-double dict representing a sparse vector.
    K: number of desired clusters. Assume that 0 < K <= |examples|.
    maxIters: maximum number of iterations to run (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
            final reconstruction loss)
    '''
    # BEGIN_YOUR_CODE (our solution is 25 lines of code, but don't worry if you deviate from this)
    # initialize K centers:
    
    centers=[]
    for i in range(K):
        center=collections.defaultdict(int)
        for d in examples[0].keys():
            center[d]=random.random()
        centers.append(center)
        
    def distance(center,point):
        result=0
        for d in center.keys():
            result+=(center[d]-point[d])**2
        return math.sqrt(result)
    
    # sign each point:
    def assignment(examples,centers,distance):
        assignments=[]
        for point in examples:
            dis=[]
            for center in centers:
                dis.append(distance(center,point))
            assignments.append(dis.index(min(dis)))
        return assignments
        
    # re-centers:
    def re_center(examples,K,assignments,centers):
        loss=0
        for i in range(K):
            sumall=[0]*len(examples[0])
            l=0
            for index in range(len(assignments)):
                if assignments[index]==i:
                    loss+=distance(centers[i],examples[index])
                    l+=1
                    m=0
                    for value in examples[index].values():
                        print(m,examples[index])
                        sumall[m]+=value
                        m+=1
            sumall=np.array(sumall)
            new=sumall/l
            m=0
            for key in centers[i].keys():
            
                centers[i][key]=new[m]
                m+=1
        return centers,loss


    # main:
    for i in range(maxIters):
        assignments=assignment(examples,centers,distance)
        centers,loss=re_center(examples,K,assignments,centers)
        
    
    return centers,assignments,loss

        
    # END_YOUR_CODE

'''
dictionary 1 :
    ki :[ assign points]

dictionary 1:
    ki :[coordinates]


'''
