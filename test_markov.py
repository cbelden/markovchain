import lyricscramble.lyricfactory as LF
import lyricscramble.lyric_chain as LC

if __name__ == '__main__':
    artist = "drake"
    # songs = ["started from the bottom", "underground kings", "the motion", "marvins room", "best i ever had", "shot for me"]
    songs = ["best i ever had", "shot for me"]
    factory = LF.lyricfactory()
    txt = ""
    for song in songs:
        txt += factory.findlyrics(artist, song)

    chain = LC.lyric_chain(txt)

    # for word in chain:
    #     print word
    #     print chain[word]
    phrase = chain.generate_phrase(10)
    print phrase + '\n'
