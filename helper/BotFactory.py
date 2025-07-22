from abc import ABC

from helper.strategy.botStrategy.EasyPlayingStrategy import EasyPlayingStrategy
from helper.strategy.botStrategy.HardPlayingStrategy import HardPlayingStrategy
from helper.strategy.botStrategy.MediumPlayingStrategy import MediumPlayingStrategy
from models.BotDifficulty import BotDifficulty


class BotFactory(ABC):

    @staticmethod
    def getBotStrategy(difficulty):
        if difficulty == BotDifficulty.EASY:
            return EasyPlayingStrategy()
        elif difficulty == BotDifficulty.MEDIUM:
            return MediumPlayingStrategy()
        elif difficulty == BotDifficulty.HARD:
            return HardPlayingStrategy()
        else:
            return EasyPlayingStrategy()
