from json.encoder import JSONEncoder

class Skin():

    m_marketValue = 0
    m_wear = 0
    m_stattrack = False
    m_name = "Bayonet"
    m_weaponType = "knife"

    def __init__(self, marketValue, wear, stattrack, name, weaponType):

        self.m_marketValue = marketValue
        self.m_wear = wear
        self.m_stattrack = stattrack
        self.m_name = name
        self.m_weaponType = weaponType