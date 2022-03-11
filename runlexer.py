from typing import Counter
from dfa import DFA

class lexer:
    def __init__(self, dfas):
        self.dfas = dfas

    def longest_prefix(self, word):
        pref_curr = ""
        found = [0] * len(self.dfas)
        for x in word:
            pref_curr += x
            for i in range (0, len(self.dfas)):
                if ( self.dfas[i].yes_or_no("" + pref_curr) == True ):
                    found[i] = len(pref_curr)
        
        r = max(found)
        index = found.index(r)
        return (index, word[0:found[index]])
            
    def parse(self, word):
        answer = ""
        while word != '':
            t = ''
            if(self.longest_prefix(word)[1] == "\n"):
                t = t + "\\n"
            else:
                t = self.longest_prefix(word)[1]
            answer = answer + self.dfas[self.longest_prefix(word)[0]].name + ' ' + t + '\n'
            word = word[ len(self.longest_prefix(word)[1]):]
        return answer