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


def get_prefix_table(needle):
    prefix_set = set()
    n = len(needle)
    prefix_table = [0]*n
    delimeter = 1
    while(delimeter<n):
        prefix_set.add(needle[:delimeter])
        j = 1
        while(j<delimeter+1):
            if needle[j:delimeter+1] in prefix_set:
                prefix_table[delimeter] = delimeter - j + 1
                break
            j += 1
        delimeter += 1
    return prefix_table

def strstr(haystack, needle):
    # m: denoting the position within S where the prospective match for W begins
    # i: denoting the index of the currently considered character in W.
    haystack_len = len(haystack)
    needle_len = len(needle)
    if (needle_len > haystack_len) or (not haystack_len) or (not needle_len):
        return -1
    prefix_table = get_prefix_table(needle)
    m = i = 0
    while((i<needle_len) and (m<haystack_len)):
        if haystack[m] == needle[i]:
            i += 1
            m += 1
        else:
            if i != 0:
                i = prefix_table[i-1]
            else:
                m += 1
    if i==needle_len and haystack[m-1] == needle[i-1]:
        return m - needle_len
    else:
        return -1
#doc 1 is pattern and doc 2 is to be searched
count=0
document2_joined= ".".join(document2)

for i in document1:
        checkvar=0
        checkvar=(strstr(document2_joined,i))
        if checkvar>0:
                count=count+1

print("the matches are "+str(count))
print("\n The rate of plagarisim is "+ str((2*count)/(len(document1)+len(document2))))
