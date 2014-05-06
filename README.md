<h3>Calvin Belden</h3>
<h3>12/11/13</h3>

<p>The following project creates a bigram language model based off of song lyrics
specified by the user. The user specifies song/artist combos in a configuration file,
lyric_scramble retrieves the song lyrics and then probabalistically generates phrases
based off of the frequencies of each bigram.</p>

<p>MusixMatch is a service that provides lyric data, and I have used their API to
request this information.  I've used the Python Wrapper 2 to access this API
programmatically.  Unfortunately, this service does not return complete lyric
information.</p>

<ul>
<li>Here is a link to the GitHub for the Python wrapper: https://github.com/utstikkar/pyMusiXmatch</li>
<li>Here is a link to the MusixMatch API documentation: https://developer.musixmatch.com/documentation</li>
</ul>

<p>To use this program, you will need to set up an account with MusixMatch and set the
MUSIXMATCH_API_KEY environment variable to the API key associated with your account.</p>

<p>Currently, test_markov.py shows an example program using the lyricscramble module.</p>

<p>NOTE TO SELF: The current project is SUPER buggy.  Lyric text is currently not parsed
correctly; should implement a better solution soon.  I'm still deciding how to treat punctuation.
I am leaning towards stripping all punctuation.  I am sure there are other errors too. Will be
implementing unit tests.</p>


<ul>Cal's TODO:
<li>correctly name the program, vars, functions: what I have actually created is a bigram
language model based on a corpus composed of lyrics specified by the user. I then generate
phrases based on this lanugage model.</li>
<li>correct text parsing</li>
<li>improve output to screen - make more readable</li>
<li>implement unit tests</li>
</ul>
