#!/usr/bin/env python3

#
# Burrows Wheeler Transform implemented in Python
# Currently, list.sort() is not the radix sort, so the algorithm order is O(n log n log n).
# This algorithm replaces items of arr to integers, so we can use the radix sort instead.
# In that case, the algorithm order becomes O(n log n).
#
from __future__ import print_function
from bwtlinear import decode_BWT
from bwtlinear import encode_BWT
import string
import codecs
SYMBOLTABLE = list(string.printable)
#SYMBOLTABLE = list(string.printable)
#SYMBOLTABLE = list(string.hexdigits)

# code from https://rosettacode.org/wiki/Move-to-front_algorithm#Python
def move2front_encode(strng, symboltable):
    sequence, pad = [], symboltable[::]
    for char in strng:
        indx = pad.index(char)
        sequence.append(indx)
        pad = [pad.pop(indx)] + pad
    return sequence
 
def move2front_decode(sequence, symboltable):
    chars, pad = [], symboltable[::]
    for indx in sequence:
        char = pad[indx]
        chars.append(char)
        pad = [pad.pop(indx)] + pad
    return ''.join(chars)
 
def Text2BWTMTF(original):
    encoded = encode_BWT(original+'$')
    #print("Data - {} BWT - {}".format(original,encoded))
    MTF_encoded = move2front_encode(encoded,SYMBOLTABLE)
    return MTF_encoded

def MTFBWT2Text(encoded):
    decoded = move2front_decode(encoded, SYMBOLTABLE)
    result = decode_BWT(decoded)
    return result[:-1]

"""
#original = "Burrows Wheeler Transform"
original = "banana".lower()
#original = "abracadabra"
bwt_ref, idx = bwt(original)
print(bwt_ref)
encoded = "".join(original[x] for x in bwt_ref)
print(encoded, idx)
ibwt_ref = ibwt(encoded, idx)
decoded = "".join(encoded[x] for x in ibwt_ref)
print(decoded)
listBWT = []
listBWT.append(encoded) 
listBWT.append("banana")
for s in listBWT:
    encode = move2front_encode(s, SYMBOLTABLE)
    print('%14r encodes to %r' % (s, encode), end=', ')
    decode = move2front_decode(encode, SYMBOLTABLE)
    print('which decodes back to %r' % decode)
    assert s == decode, 'Whoops!'
"""
listBWT = []#["abracadabra","banana", "saulosaulosaulo","salamandra","Rogerio"]
for word in listBWT:
    encoded = Text2BWTMTF(word)    
    decoded = MTFBWT2Text(encoded)
    print("Prototype - Encode {} to {} which was decoded to {}".format(word,encoded,decoded))


newfile = open("/Users/dossants/Desktop/Blockchain Slice/update/blockchain/blocks/Blkxxxx/SampleMTF.dat", 'w')
recoverFile = open("/Users/dossants/Desktop/Blockchain Slice/update/blockchain/blocks/Blkxxxx/ExpRecovered.dat",'w',encoding="Latin-1")
block = open("/Users/dossants/Desktop/Blockchain Slice/update/blockchain/blocks/Blkxxxx/ExpSample.dat",encoding="Latin-1").readlines()
count = 0 
for line in block:
    encoded = Text2BWTMTF(line.encode('utf-8').hex())    
    newfile.write(str(encoded))
    decoded = MTFBWT2Text(encoded)
    decoded = codecs.decode(decoded,"hex").decode("utf-8")
    recoverFile.write(str(decoded))
    #print("Prototype - Encode {} to {} which was decoded to {}".format(line,encoded,decoded))
    count +=1
    print(count)

newfile.close()
recoverFile.close()


    