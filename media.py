# Import webbrowser module
import webbrowser


class Movie():
    # Constructor for the movie class to create instances of Movie.
    def __init__(self, title, synopsis, poster_image, trailer_youtube,
                 release_date, starring):
        self.title = title
        self.synopsis = synopsis
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.starring = starring
