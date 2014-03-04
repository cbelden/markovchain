import musixmatch.matcher as matcher
import musixmatch.util as util
import json


class lyricfactory(object):
    """
    The lyricfactory calls on the MusixMatch API python wrapper
    and retrieves the lyrics for a given artist/song combo
    """
    def __init__(self):
        pass

    def retrieveLyrics(self):
        user_request = self.readUserRequestInfo()
        return self.request_lyrics(user_request["songs"])

    def readUserRequestInfo(self):
        """
        Reads in the song request information from the json config file: lyric_scramble/settings/config.json
        """
        json_fp = open('settings/config.json', 'r')
        data = json.load(json_fp)
        json_fp.close()

        return data

    def request_lyrics(self, request_info):
        """
        input
            request_info data from the config.json file

        returns
            the concatenated text from the lyrics returned for each song
        """
        txt = ""
        for artist in request_info:
            for song in request_info[artist]:
                txt += self.findlyrics(artist, song)

        return txt

    def findlyrics(self, artist, song):
        """
        input
            artist - name of the artist
            song - name of the song

        returns
            the lyrics for that song
        """
        api_resp = self.pinpoint_song(artist, song)

        if not api_resp:
            return ''

        lyricinfo = api_resp.lyrics()
        txt = lyricinfo["lyrics_body"].encode("utf8")
        txt = txt.replace("******* This Lyrics is NOT for Commercial use *******", "")

        return txt

    def pinpoint_song(self, artist, song):
        """
        Uses the MusixMatch API to find the lyrics.
        """
        # construct API call
        params = {}
        params['q_artist'] = artist
        params['q_track'] = song

        print "Searching for \"%s\" lyrics by '%s'..." % (song, artist)

        # send api call
        try:
            resp = matcher.track(**params)
        except util.MusixMatchAPIError, e:
            print "...could not perform a lyric search."
            print e.args[0]
            return None

        print "\t*Found the lyrics"

        return resp
