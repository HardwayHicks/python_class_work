class Song:
    """class to represent the song
    atributes:
        title (string): title of the song
        artist (Artist): an artist object representing the songs creators
        duration (int): the duration of the song in seconds, can be 0
    """

    def __init__(self, title, artist, duration=0):
        """ song init method
        
    Args:
        title (string): initializes the title attribute
        artist (Artist): an artist object representing the songs creators
        duration (optional) [int]: initial value of the duration
            duration will default to 0 if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration

