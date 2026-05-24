from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def play(self, player):
        pass

    @abstractmethod
    def pause(self, player):
        pass

    @abstractmethod
    def stop(self, player):
        pass


class PlayingState(State):

    def play(self, player):
        print("Music is already playing")

    def pause(self, player):
        print("Music paused")
        player.state = PausedState()

    def stop(self, player):
        print("Music stopped")
        player.state = StoppedState()


class PausedState(State):

    def play(self, player):
        print("Music resumed")
        player.state = PlayingState()

    def pause(self, player):
        print("Music is already paused")

    def stop(self, player):
        print("Music stopped")
        player.state = StoppedState()


class StoppedState(State):

    def play(self, player):
        print("Music started")
        player.state = PlayingState()

    def pause(self, player):
        print("Cannot pause. Music is stopped")

    def stop(self, player):
        print("Music is already stopped")


class MusicPlayer:

    def __init__(self):
        self.state = StoppedState()

    def play(self):
        self.state.play(self)

    def pause(self):
        self.state.pause(self)

    def stop(self):
        self.state.stop(self)


if __name__ == "__main__":

    player = MusicPlayer()

    player.play()
    player.pause()
    player.play()
    player.stop()
    player.stop()
