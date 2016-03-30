from sources.domain.roulette.roulette import Roulette

class RouletteService:

    m_slots = 15

    def getPopulatedRoulette(self, bet):
       return Roulette(bet, self.m_slots)