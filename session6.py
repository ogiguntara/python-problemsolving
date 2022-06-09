#!python3
import string

def sortString(a):
    print(a)
    #normalize string
    new_string=a.translate(str.maketrans('','',string.punctuation))#remove punctuation
    print(new_string)
    #pecahkan kata dari kalimat
    words = new_string.split(' ')#split by space
    print(words)
    print('total words : ',len(words))

    #mengurutkan kata-kata
    words.sort()
    print(words)
    print('\nHasil urutan sesuai abjad: ')
    for word in words:
        print(word)

def luas_segitiga(alas,tinggi):
    return (alas*tinggi)/2
