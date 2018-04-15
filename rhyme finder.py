def find_rhyming_words(wordToRhyme: str, length=5)->None:
    '''Given a word, return top <length> rhyming words'''
    
    def _print(wordToRhyme: str, length: int, index_dic: 'dict[int:str[]]')->None:
        '''Print rhyming words, if any'''
        print('Words rhyming with {}:'.format(wordToRhyme.capitalize()))
        wordsFound=1
        while index_dic and wordsFound<length+1:
            mostMatching = index_dic.pop(min(index_dic))
            # because the indicies are negative,
            # the min index is the most matching characters
            while wordsFound<length+1 and mostMatching:
                shortestWord = min(mostMatching, key=lambda x: len(x))
                print('     '+shortestWord.capitalize())
                mostMatching.pop(mostMatching.index(shortestWord))
                wordsFound+=1
                    
        if wordsFound==1:
            print('No rhyming words found with {}.'.format(wordToRhyme.capitalize()))

    if wordToRhyme == 'quit':
        quit()
        
    with open("words", "r") as word:
        word_set = set(word.read().split())
        
    if not (wordToRhyme.lower() in word_set or wordToRhyme.capitalize() in word_set):
        print("Word {} not in our dictionary".format(wordToRhyme))
        return
    
    word_set = word_set - set((wordToRhyme.casefold(),wordToRhyme.capitalize()))
    index_dic = {-1:[word for word in word_set if word[-1]==wordToRhyme[-1]]}
    # hardcode the first index
    # because the following loop will iterate through the previous indices
    for reverseIndex in range(2,len(wordToRhyme)+1):
        index_dic[-reverseIndex]=[]
        for word in index_dic[-reverseIndex+1]:
            if len(word)>reverseIndex and word[-reverseIndex]==wordToRhyme[-reverseIndex]:
                # the length of the word must be larger than reverseIndex
                # or word[-reverseIndex] will raise error
                index_dic[-reverseIndex].append(word)
                index_dic[-reverseIndex+1].pop(index_dic[-reverseIndex+1].index(word))
        if len(index_dic[-reverseIndex])==0:
            break
    _print(wordToRhyme, length, index_dic)

def generator(length: int)->None:
    '''prompt user to enter words to rhyme, and call find_rhyming_words on their input'''
    yield find_rhyming_words(input('Type a word to rhyme: '),length)
    while True:
        yield find_rhyming_words(input('Type a word to rhyme again: '),length)

if __name__ == "__main__":
    print('Type "quit" to quit\n')
    length = input('Type number of rhyming words to print: ')
    while not length.isnumeric():
        print("Error: please type in number")
        length = input('Type number of rhyming words to print: ')
    length = int(length)
    for i in generator(length):
        generator(length)
        print()
    
    
            
                    

    
    


            
