# Multiple Inheritance Example

class Camera:
    def take_photo(self):
        print("Taking a photo 📸")


class MusicPlayer:
    def play_music(self):
        print("Playing music 🎵")


class SmartPhone(Camera, MusicPlayer):
    def phone_features(self):
        print("Making a call 📱 and sending messages ✉️")


# Object creation
device = SmartPhone()

device.take_photo()
device.play_music()
device.phone_features()
