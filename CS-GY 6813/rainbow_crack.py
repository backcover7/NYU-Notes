#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib

dictPath = "D:/tmp/l.txt"
hashPath = "D:/tmp/linkedin.txt"
rainbowFile = "D:/tmp/rb.txt"
result = 'D:/tmp/result.txt'


def hashType(val):
    with open(hashPath,'r') as test:
        val = test.readline()
        hashLen = len(val)
        if hashLen == 33: return 'md5'
        elif hashLen == 41: return 'sha1'
        elif hashLen == 65: return 'sha256'

def generateRainbow():
    rb = open(rainbowFile, 'a+')
    with open(dictPath, 'r') as dict:
        dictVal = dict.readline().strip('\n')
        while dictVal:
            if hashType(dictVal) == 'md5':
                hashResult = hashlib.md5(dictVal).hexdigest()
                rb.write(hashResult + '/' + dictVal + '\n')
            elif hashType(dictVal) == 'sha1':
                hashResult = hashlib.sha1(dictVal).hexdigest()
                rb.write(hashResult + '/' + dictVal + '\n')
            elif hashType(dictVal) == 'sha256':
                #salt
                for salt in range(0, 100):
                    hashResult = hashlib.sha256(str(salt) + dictVal).hexdigest()
                    rb.write(hashResult + '/' + dictVal + '\n')
            dictVal = dict.readline().strip('\n')
    rb.close()

def toDict():
    with open(rainbowFile, 'r') as rb:
        rbDict = {}
        line = rb.readline()
        len = line.index('/')
        if hashType(len) == 'md5':
            while line:
                rbDict[line[0:32]] = line[33:-1]
                line = rb.readline()
        elif hashType(len) == 'sha1':
            while line:
                rbDict[line[0:40]] = line[41:-1]
                line = rb.readline()
        elif hashType(len) == 'sha256':
            while line:
                rbDict[line[0:64]] = line[65:-1]
                line = rb.readline()
        return rbDict

generateRainbow()
dt = toDict()
with open(hashPath, 'r') as target:
    crack = target.readline().strip('\n')
    while crack:
        with open(result, 'a+') as rt:
            if(dt.has_key(crack)):
                rt.write(crack + ' : ' + dt.get(crack) + '\n')
            else:
                rt.write(crack + ' : ' + 'NOT FOUND' + '\n')
            crack = target.readline().strip('\n')
