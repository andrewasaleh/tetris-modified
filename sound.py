import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.wav")
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.wav")
        self.music_playing = False  # Keep track of whether music is playing

    def play_rotate_sound(self):
        self.rotate_sound.play()

    def play_clear_sound(self):
        self.clear_sound.play()

    def play_music(self, loop=-1):
        pygame.mixer.music.load("Sounds/music.wav")
        pygame.mixer.music.play(loop)
        self.music_playing = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.music_playing = False

# Initialize SoundManager
sound_manager = SoundManager()

# When the game starts
sound_manager.play_music()

# When the game ends
sound_manager.stop_music()
