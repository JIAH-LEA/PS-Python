#Hackerrank
#String Reduction
#TimeComplexity O(n)

def getMinDeletions(s):
    return len(s)-len(set(s))
