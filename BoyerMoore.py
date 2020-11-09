from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer


def stemSentence(sentence):
        porter = PorterStemmer()
        porter.stem(sentence)
        token_words = word_tokenize(sentence)
        token_words
        stem_sentence = []
        for word in token_words:
                stem_sentence.append(porter.stem(word))
                stem_sentence.append(" ")
        # print("".join(stem_sentence)+'\n')
        return "".join(stem_sentence)



document1 = open(
        'File1.txt', 'r').readlines()
document2 = open(
        'File2.txt', 'r').readlines()
listee = (document1)
final1 = []
for i in listee:
        t = i.split('.')
        for i in t:
                final1.append(i)

for i in range(0, final1.count(' \n')):
        final1.remove(' \n')
for i in range(0, final1.count('\n')):
        final1.remove('\n')

listee = (document2)
final2 = []
for i in listee:
        t = i.split('.')
        for i in t:
                final2.append(i)

for i in range(0, final2.count(' \n')):
        final2.remove(' \n')
for i in range(0, final2.count('\n')):
        final2.remove('\n')


def remove_common_words_stemming(main, generic):
        finaler = []
        for i in main:
                # print(i)
                query = i
                stopwords = generic
                querywords = query.split()

                resultwords = [word for word in querywords if word.lower() not in stopwords]
                result = ' '.join(resultwords)
                finaler.append(stemSentence(result))
        # print(finaler)
        return finaler


# print(final)
common_word_list = ['do', 'she', 'they', 'we',
        'are', 'is', 'a', 'an', 'in', 'as', 'in', 'of']
document1 = remove_common_words_stemming(final1, common_word_list)
document2 = remove_common_words_stemming(final2, common_word_list)

def BoyerMooreHorspool(pattern, text):
    m = len(pattern)
    n = len(text)
    if m > n: return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1; i -= 1
        if j == -1: return i + 1
        k += skip[ord(text[k])]
    return -1
count=0
document2_joined= ".".join(document2)
for i in document1:
        checkvar=0
        checkvar=(BoyerMooreHorspool(i,document2_joined))
        if checkvar>-1:
                count=count+1
rate_plagarisim=(2*count)/(len(document1)+len(document2))

print('\nThe rate of plagarisim '+str(rate_plagarisim))
