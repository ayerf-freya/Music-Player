from textual.app import App
from textual.widgets import Label
from main import sp


class MusicPlayer(App):
      def compose(self):
          now_playing = sp.currently_playing()
          track_name = now_playing["item"]["name"]
          artist_name = ", ".join([a["name"] for a in now_playing["item"]["artists"]])
          album_name = now_playing["item"]["album"]["name"]
          duration_ms = now_playing["item"]["duration_ms"]
          progress_ms = now_playing["progress_ms"]
          yield Label(track_name)
          yield Label(artist_name)
          yield Label(album_name)
          yield Label(str(duration_ms // 1000))
          yield Label(str(progress_ms // 1000))

if __name__ == "__main__":
    app = MusicPlayer()
    app.run()


