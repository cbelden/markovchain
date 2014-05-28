from markovchain import MarkovChain

corpus = "this is a bunch of text used to make a markov chain. This is pretty neat."
chain = MarkovChain(corpus)

for term, consecutive_terms in chain:
    print term
    print consecutive_terms
    print ''
