import pyglet

def play_sound(sound_file):
    # Load the sound file
    sound_effect = pyglet.resource.media(sound_file)
    sound_effect.play()

# Example usage:
# Provide the full or relative path to the sound file
#print("playing sound...")
#play_sound("soundtrack/nice_shot.mp3")
#play_sound("soundtrack/Euphoric20Pixels20ext20v2.1.mp3")
#print("sound has now sounded")
