from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader

class MusicPlayer(BoxLayout):
    def __init__(self, **kwargs):
        super(MusicPlayer, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Load the MP3 file (Make sure sample.mp3 is in the same folder)
        self.sound = SoundLoader.load('sample.mp3')

        # Track Info Label
        self.track_label = Label(text="Playing: sample.mp3", font_size='20sp')
        self.add_widget(self.track_label)

        # Play Button
        self.play_button = Button(text="PLAY", size_hint=(1, 0.3))
        self.play_button.bind(on_press=self.play_music)
        self.add_widget(self.play_button)

        # Stop Button
        self.stop_button = Button(text="STOP", size_hint=(1, 0.3))
        self.stop_button.bind(on_press=self.stop_music)
        self.add_widget(self.stop_button)

    def play_music(self, instance):
        if self.sound:
            self.sound.play()
            self.track_label.text = "Music is Playing..."

    def stop_music(self, instance):
        if self.sound:
            self.sound.stop()
            self.track_label.text = "Music Stopped"

class SimpleTrackApp(App):
    def build(self):
        self.title = "Custom Music Player"
        return MusicPlayer()

if __name__ == '__main__':
    SimpleTrackApp().run()
