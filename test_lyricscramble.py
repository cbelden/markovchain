import lyricscramble.lyricfactory as LF
import lyricscramble.language_model as LM
import lyricscramble.utils as scramble_utils

if __name__ == '__main__':
    # Get request info from config file
    request_info = scramble_utils.RetreiveRequestInfo()

    # Retrieve the song lyrics specified in the user config file
    l_factory = LF.lyricfactory()
    lyrics = l_factory.retrieveLyrics()

    # Use lyric txt to generate language model
    m_chain = LM.language_model(lyrics)

    while 1:
        print m_chain.generate_string()
        raw = raw_input()

        if raw != '':
            print "Quitting.."
            break
