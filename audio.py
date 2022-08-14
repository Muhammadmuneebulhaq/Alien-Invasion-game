from pygame import mixer

welcome_note = 'Gallery\\'

def playaudio(filename):
    mixer.init()
    mixer.music.load(filename)
    mixer.music.set_volume(0.7)
    mixer.music.play(1)