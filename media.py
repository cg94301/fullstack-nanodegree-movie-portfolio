import webbrowser

class Movie():
    def __init__(self, title, storyline, poster, youtube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
