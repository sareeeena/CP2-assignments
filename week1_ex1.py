class Song:
    def __init__(self, title ,artist,duration):
        self.title=title
        self.artist= artist
        self.duration= duration
    def display_info(self):
        print(f"Title: {self.title}, Artist: {self.artist}, Duration: {self.duration} min")  
    def get_duration_seconds(self):
        converted=self.duration * 60
        return converted 
song1= Song("Yesterday", "The Beatles", 2.5) 
song2=Song("BR", "Queen", 6.0)

song1.display_info()
song2.display_info()
d=song2.get_duration_seconds()
print(f"{int(d)}")