#markovchain

##About
The markovchain module implements a Markov Chain (using a bigram) for text corpuses. I really just made this for my lyricscramble package, which has some unique requirements (for generating tweets).

##Installing

    pip install git+git://github.com/cbelden/markovchain.git@master

##Use

    corpus = 'This is a sample text corpus.'
    chain = MarkovChain(corpus)
    chain.generate_phrase()
