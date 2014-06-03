from markovchain import MarkovChain

corpus = "this is a bunch of text used to make a markov chain. This is pretty neat."
chain = MarkovChain(corpus)

for i in range(10):
    print chain.generate_phrase(min_words=5, max_size=140)
