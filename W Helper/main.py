import pandas as pd
import numpy as np
import investigate as iv

full_df = pd.read_csv('wordle.csv')
words_df=full_df['word']
chararr_words = list(words_df.map(lambda x : [list(char) for char in list(x)]))
abundancearr=list(full_df['occurrence'])

w = [['c','r','a','t','e'],
    ['p','a','u','s','e'],
    ['w','a','l','l','s'],
    ['f','i','n','e','d']]

s = [[1,1,2,1,2],
    [1,2,1,1,2],
    [1,2,1,1,1],
    [1,1,1,2,1]]

print (iv.top_5_guesses(chararr_words,abundancearr,w,s))

x=0