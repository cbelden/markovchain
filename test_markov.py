import lyricscramble.lyricfactory as LF
import lyricscramble.lyric_chain as LC
import lyricscramble.utils as utils

if __name__ == '__main__':
    # Get txt from MusixMatch to use for markov chain
    request_info = utils.RetreiveRequestInfo()
    l_factory = LF.lyricfactory()
    txt = l_factory.request_lyrics(request_info["songs"])

    # Use txt to generate markov chain
    chain = LC.lyric_chain(txt)

    # Let user generate phrases
    phrase_length = 15

    while 1:
        print chain.generate_phrase(phrase_length)
        raw = raw_input()

        if raw != '':
            print "Quitting.."
            break
