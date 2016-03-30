from sources.domain.skin.skin import Skin

class Roulette:

    m_bet = 0
    m_slots = 0
    m_skinsArray = []

    def __init__(self, bet, slots):
        self.m_bet = bet
        self.m_slots = slots
        self.initRoulette(bet, slots)

    def initRoulette(self, bet, slots):
        self.m_skinsArray = []
        for i in range (0,slots):
            self.m_skinsArray.append(Skin("200$","0.006", True, "M9 Bayonet Fade", "Knife"))

