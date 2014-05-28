from markovchain import MarkovChain

corpus = "this is a bunch of text used to make a markov chain. This is pretty neat."
chain = MarkovChain(corpus)

print chain.generate_phrase()
