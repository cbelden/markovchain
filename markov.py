import lyricscramble.lyric_chain as LC


if __name__ == '__main__':
    f = open('./pimps_lyrics.txt', 'r')
    txt = f.read()
    f.close()

    mychain = LC.lyric_chain(txt)
    print mychain.generate_phrase(15)
