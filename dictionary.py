import json
from difflib import get_close_matches
data=json.load(open('original.json'))

def define_meaning(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print(f'Did you mean this {get_close_matches(word,data.keys())[0]}')
        n=input('press y for yes or n for no:-')
        if n=='y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return 'You press wrong keys or may be its not in our database'
    else:
        return 'You press wrong keys or may be its not in our database'
    
word=input('Enter a word:-')
result=define_meaning(word)
if( type(result)== list):
    count=0
    for l in result:
        count+=1
        print(count,')',l)
else:
    print(result)