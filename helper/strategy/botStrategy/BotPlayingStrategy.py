from abc import ABC, abstractmethod

class BotPlayingStrategy(ABC):

    @abstractmethod
    def decide_cell(self, board):
        raise NotImplementedError
