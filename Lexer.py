from dfa import DFA
from runlexer import lexer

def runlexer(lex, innp, out):
        lexf = open(lex, "r")
        inf = open(innp, "r")
        outf = open(out, "w")
        
	    word = "" + inf.read()
	    dfa_count = 1
	    strrr = ""
	    for x in lexf:
	        if (x == "\n"):
	            dfa_count += 1
            strrr = strrr + x
            aux = strrr.split("\n\n")

	    dfas = [0] * dfa_count
	    names = [0] * dfa_count

	    for x in range(0, dfa_count):
            dfas[x] = DFA(aux[x])
            names[x] = dfas[x].name

	    lex = lexer(dfas)
        outf.write(lex.parse(word))
        outf.close()
        lexf.close()
        inf.close()