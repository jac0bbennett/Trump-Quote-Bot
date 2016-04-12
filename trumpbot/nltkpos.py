#!/usr/bin/python
import nltk
file = open(r"tweets.txt", "r", encoding="utf-8-sig")

wordpos = {}

POS = nltk.pos_tag(file.read().encode("ascii", errors="ignore").decode("ascii").split())

for word in POS:
    if word[0].startswith('http') or word[0].startswith('@') or word[0].startswith('"') or word[0].startswith('.'):
        pass
    else:
        try:
            wordpos[word[1]].append(word[0])
        except KeyError:
            wordpos[word[1]] = [word[0]]
        
f = open( 'words.py', 'w' )
f.write( 'wordpos = ' + repr(wordpos))
f.close()