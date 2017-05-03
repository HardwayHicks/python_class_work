class Song:
    """class to represent the song
    atributes:
        title (string): title of the song
        artist (string): name of the songs creators
        duration (int): the duration of the song in seconds, can be 0
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """ Class to represent an album, using its tracklist
    
    attributes:
        album_name
        year (int)
        artist: name fo the artists, if not specified will be various artists
        tracks (list[Song]) a list of songs on the album
        
    methods:
        add_song: used to add new song to the album's track list
        """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "various artists"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list
        Args:
            song(Song) the title of the song to add
            position (optional[int]) if specified will  add song to that position
            otherwise song will be added at the end of the list
            """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
        if position is None:
            self.tracks.append(song_found)
        else:
            self.tracks.insert(position, song_found)

class Artist:
    """ class to store artist details
    attributes:
        name
        albums (list[Album]) list of albums contained in this list
        
    methods:
        add_album: adds new album to artist's album list
        """

    def __init__(self, name):
        self.name = name
        self.albums =[]

    def add_album(self, album):
        """ add a new album to the list
        args:
            album(Album) object to add to the list
                if th album is already present it is not added a second time
                
            """
        self.albums.append(album)


    def add_song(self, name, year, title):
        """add a new song to the collection of albums
        
        this method will add the song to an album in the collection
        a new album will be created in the collection if it doesn't already exist
        
        Args:
            name: the name of th e album
            yeah (int): year the album was produced
            title: title of the song
            """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("found album " + name)

        album_found.add_song(title)



def find_object(field, object_list):
    """check the object_list to see if an object with 'name' attribute equal to 'field' exists"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # each row should have artist, album, year, song
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    """create a checkfile from the object data for comparison with the original file"""
    with open("checkflie.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                        file=checkfile)

if __name__ == '__main__':
    artists = load_data()
    print("there are {} artists".format(len(artists)))

    create_checkfile(artists)