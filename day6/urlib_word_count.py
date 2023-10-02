import urllib

def has_three_double(word):
    """ Returns True if the word contains three consecutive pairs of
    double letters and False otherwise.         
    """
    for l in range(len(word)-5):
        if word[l] == word[l+1] and \
           word[l+2]==word[l+3] and \
           word[l+4]==word[l+5]:
            return True
    return False

# Comments that fit in a single line can be put in this format.
# Anything after a single pound sign is ignored.

# The main body of the program starts here

word_url = 'http://www.greenteapress.com/thinkpython/code/words.txt'
word_file = urllib.urlopen(word_url)

count = 0
for word in word_file:
    word = word.strip().strip('\n')
    if has_three_double(word):
        print (word)
        count = count + 1
        
if count == 0:
    print ('No words found')
elif count == 1:
    print ("1 word found")
else:
    print (count, 'words were found')