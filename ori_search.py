import itertools
import collections
import sys
#---------------------------------------------------------------
#creates the reverse comp. of a string of bases A, C, G, T
#---------------------------------------------------------------
def reverse(Pattern):
    d = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    return ''.join(d[x] for x in Pattern[::-1])
#---------------------------------------------------------------
#creates an array of skew for each nuc. pos. in dna string "g"
#---------------------------------------------------------------
def skew(g):
    map = {'A':0, 'T':0, 'C':-1, 'G':1}
    s = [0]
    for i, value in enumerate(g):
        s.append(s[i] + map[value])
    return s

#---------------------------------------------------------------
#returns array of positions of minimum skew in genome g
#---------------------------------------------------------------
def minskew(g):
    s = skew(g)
    m = min(s)
    return [ i for i, val in enumerate(s) if val == m ]


#---------------------------------------------------------------
#returns hamming distance of two strings of equal length
#hamming distance = number of differences at each index
#---------------------------------------------------------------
def hd(p,q):
    hd = 0
    for i,j in zip(p,q):
        if i != j:
            hd += 1
    return hd

#---------------------------------------------------------------
#generate a dictionary of all instances of each k-mer for
#a size k and a text t
#---------------------------------------------------------------
def kmers(t, k):
    d = {}
    for i in range(len(t) - k + 1):
        if t[i:i+k] in d:
            d[t[i:i+k]] += 1
        else:
            d[t[i:i+k]] = 1
    return d

#---------------------------------------------------------------
#returns array of approximate occurences of pattern in text
#where approximate is defined as a string that is only d
#differences separate from pattern
#---------------------------------------------------------------
def ApproximatePatternMatching(g, p, d):
    positions = []
    l = len(p)
    for i, val in enumerate(g):
        if i > len(g) - len(p):
            break
        dist = hd(p,g[i:i+l])
        if dist <= d:
            positions.append(i)
        elif dist - d > 1:
            i += dist - d
        else:
            pass
    return positions

def max_list(dict):
    max = 0
    list = []
    for d in dict:
        if dict[d] > max:
            max = dict[d]
            list.clear()
            list.append(d)
        elif dict[d] == max:
            list.append(d)
        else:
            pass
    return list

def make_sisters(text,d): #make sisters of text t with d mismatches
    list = ['A', 'C', 'G', 'T']
    sisters = []
    if d == 0:
        return sisters
    elif d == 1:
        for i in range(len(text)):
            for k in list:
                if text[i] != k:
                    sisters.append(text[0:i] + k + text[i+1:])
        return sisters
    elif d == len(text):
        l = []
        for i in text:
            l.append(make_sisters(i, 1))
        for i in itertools.product(*l):
            sisters.append("".join(i))
        return sisters
    else:
        for i in list:
            if i == text[0]:
                l = make_sisters(text[1:], d)
                for k in l:
                    sisters.append(i + k)
            else:
                l = make_sisters(text[1:], d-1)
                for k in l:
                    sisters.append(i + k)
        return sisters

def Mismatches(text, k, d):
    kmer_list = kmers(text,k)
    dict = kmer_list.copy()
    for i in kmer_list:
        temp = d
        while temp > 0:
            sisters = make_sisters(i, temp)
            for k in sisters:
                if k in dict:
                    dict[k] += kmer_list[i]
                else:
                    dict[k] = kmer_list[i]
            temp = temp - 1
    max_value = max(dict.values())
    max_mismatches = [keys for keys, vals, in dict.items() if vals == max_value]
    return max_mismatches

def MismatchesWithComplements(text, k, d):
    kmer_list = kmers(text,k)
    dict = kmer_list.copy()
    for i in kmer_list:
        temp = d
        while temp > 0:
            sisters = make_sisters(i, temp)
            for k in sisters:
                if k in dict:
                    dict[k] += kmer_list[i]
                else:
                    dict[k] = kmer_list[i]
            temp = temp - 1
    mwc = {}
    for i in dict:
        if reverse(i) in dict:
            mwc[i] = dict[i] + dict[reverse(i)]
        else:
            mwc[i] = dict[i]
    max_value = max(mwc.values())
    max_mismatches = [keys for keys, vals, in mwc.items() if vals == max_value]
    return max_mismatches
