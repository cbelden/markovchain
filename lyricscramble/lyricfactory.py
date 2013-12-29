import musixmatch.matcher as matcher
import musixmatch.util as util
import json
import string



class lyricfactory(object):
    """
    The lyricfactory calls on the MusixMatch API python wrapper
    and retrieves the lyrics for a given artist/song combo
    """
    def __init__(self):
        pass

    def findlyrics(self, artist, song):
        """
        input
            artist - name of the artist
            song - name of the song

        returns
            the lyrics for that song
        """
        resp = self.pinpointsong(artist, song)
        #share_url = resp['track_share_url']
        lyricinfo = resp.lyrics()
        txt = lyricinfo["lyrics_body"].encode("utf8")
        lyrics = txt.replace("******* This Lyrics is NOT for Commercial use *******", "").translate(string.maketrans("", ""), string.punctuation)

        return lyrics

    def pinpointsong(self, artist, song):
        """
        Uses the MusixMatch API to find the lyrics.
        """
        # construct API call
        params = {}
        params['q_artist'] = artist
        params['q_track'] = song

        print "...searcing for lyrics"

        # send api call
        try:
            resp = matcher.track(**params)
        except util.MusixMatchAPIError, e:
            print "...could not perform a lyric search."
            print e.args
            return None

        print "...found lyrics"
        return resp
