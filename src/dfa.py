from typing import Set

class DFA:
    def __init__(self, text):#, nume):
        self.text = text
        v = text.split('\n')

        self.name = v[1]

        self.initial_state = (int(v[2]))

        fs = v[len(v) - 1].split(' ')
        self.final_states = [0] * len(fs)
        for x in range(0, len(fs)):
           self.final_states[x] = (int(fs[x]))

        v.pop(0)
        v.pop(0)
        v.pop(0)
        v.pop(len(v)-1)
       
        self.alphabet = [0] * len(v)
        keys = [0] * len(v)
        my_dict = {}
        for x in range(0, len(v)):
            line = v[x].split(',')
            aux = line[1].replace("'","")
            if(aux == "\\n"):
                aux = "\n"
            self.alphabet[x] = aux
            keys[x] = (int(line[0]), aux)
            my_dict[keys[x]] = int(line[2])
        self.alphabet = list(set(self.alphabet))
        self.delta = my_dict

    def config_func(self, i):
        if ( i[0], i[1][0] ) in self.delta and i[1] != "":
            return (self.delta[ ( i[0], i[1][0] ) ], i[1][1:])
        else:
            return -1

    def yes_or_no(self, w):
        i = (self.initial_state, w)
        for x in range(0, len(w)):
            t = self.config_func(i)
            if (t == -1):
                return False
            i = t
        if (i[1] == '') and (i[0] in self.final_states):
            return True
        else: return False
