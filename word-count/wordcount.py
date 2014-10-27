import re

def word_count(words):
    words = words.split()
	 
    list_words = {}
	
    for words in words:
        if words in list_words:
            list_words[words] += 1
        else:
		    list_words[words] = 1
   
    print list_words
	
    return list_words
				
    
   
	

