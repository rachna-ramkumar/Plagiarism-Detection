
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

print(document1)
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
common_word_list = ['do', 'she', 'they', 'we',',',
        'are', 'is', 'a', 'an', 'in', 'as', 'in', 'of']
document1 = remove_common_words_stemming(final1, common_word_list)
document2 = remove_common_words_stemming(final2, common_word_list)
print(document1)

#print(document1)

# tokenizing -> stop word removal -> stemming is finished

# we need to do a hashing
d=128
def search(pat, txt, q):

        M = len(pat)  # dno of letter in input alphabet
        N = len(txt)
        i = 0
        j = 0
        p = 0  # hash value for pattern
        t = 0  # hash value for txt
        h = 1
        count = 0

        # The value of h would be "pow(d, M-1)% q"
        for i in range(M-1):
                h = (h * d) % q

        # Calculate the hash value of pattern and first window
        # of text
        if(N>M):
                for i in range(M-1):
                
                        p = (d * p + ord(pat[i])) % q
                        t = (d * t + ord(txt[i])) % q
                        #print("\nPASSSS "+str([i])+' '+str(txt[i]))
        else:
                exit

        
                

        # Slide the pattern over text one by one
        for i in range(N-M + 1):
                # Check the hash values of current window of text and
                # pattern if the hash values match then only check
                # for characters on by one
                if p == t:
                        # Check for characters one by one
                        for j in range(M):
                                if txt[i + j] != pat[j]:
                                        break

                        j += 1
                        # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
                        if j == M:
                                count = count+1
                                print("Pattern found at index " + str(i))

                # Calculate hash value for next window of text: Remove
                # leading digit, add trailing digit
                if i < N-M:
                        t = (d*(t-ord(txt[i])*h) + ord(txt[i + M])) % q

                        # We might get negative values of t, converting it to
                        # positive
                        if t < 0:
                                t = t + q
        return count

q = 101
match_no=0

for i in document2:
        for j in document1:
                print(str('\n doc 1 string ->')+j +'``***``'+i+str('<---pattern\n'))
                test=search(j,i,q)
                if test>0:
                        match_no=match_no+1

rate_plagarisim=(2*match_no)/(len(document1)+len(document2))

print('\nThe rate of plagarisim '+str(rate_plagarisim))
