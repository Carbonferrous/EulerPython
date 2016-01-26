import itertools
def testKey(cipher, a, b, c):
    return list(filter(None.__ne__, (i for j in itertools.zip_longest(list(map(lambda x: x^a,cipher[::3])), list(map(lambda x: x^b,cipher[1::3])), list(map(lambda x: x^c,cipher[2::3]))) for i in j)))
def listToString(cipher):
    return ''.join(map(chr,cipher))

encoded = list(map(int,open("p059_cipher.txt").read().split(',')))
for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            testCipher = testKey(encoded, a, b, c)
            CipherString = listToString(testCipher)
            if 'the' in CipherString and '`' not in CipherString and '~' not in CipherString:
                print(CipherString)
                print('Key: ', chr(a), chr(b), chr(c))
                print(sum(testCipher))
