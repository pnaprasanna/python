import webbrowser
#webbrowser.open('https://engine.presearch.org/search?q=awsomeness')
#webbrowser.open('https://engine.presearch.org/search?q=this+day+that+age')

#https://pypi.org/project/Random-Word/
#pip3 install random-word pyyaml

from random_word import RandomWords
for i in range(3):
    random_words = RandomWords()
    x=random_words.get_random_word()
    webbrowser.open('https://engine.presearch.org/search?q=' + x) 
 
