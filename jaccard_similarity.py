from __future__ import division
from __future__ import print_function
import argparse


def shingle(document, k):
    l = len(document)
    # print(l)
    result = set()
    for i in range(l-k+1):
        result.add(document[i:i+k])
    return result

def jacard_sim(set1, set2):

    return len(set1.intersection(set2))/len(set1.union(set2))

def main():
    document1 = "abcdefghijklmnopqrstuvwxyz"
    shng1 = shingle(document1,3)
    document2 = "bbcdefghijklmnopqrstuvwxyz"
    shng2 = shingle(document2,3)

    print(jacard_sim(shng1, shng2))


    

if __name__ == "__main__":
    main()
