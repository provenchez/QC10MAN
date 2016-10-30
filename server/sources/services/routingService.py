from flask import Flask
from flask import jsonify
from sources.services.rouletteService import RouletteService
import json
import os

class RoutingService:

    m_server = Flask(__name__)
    m_rouletteService = ""


    def declareRoutes(self):
        @self.m_server.route("/")
        def index():
            return 	"Win	Loss	(+/-)
Devil	5	2	15
dav0ke	3	0	15
vez	4	2	10
infekt	2	0	10
sml	3	2	5
gmd	4	3	5
zid	2	1	5
provencher	1	1	0
knave	1	1	0
effys	1	1	0
PapaMax	1	2	-5
krz	0	1	-5
jay	2	4	-10
vtz	0	3	-15
tiz	1	4	-15
Subroza	2	5	-15"

        @self.m_server.route("/roulette")
        def roulette():
            roulette = self.m_rouletteService.getPopulatedRoulette(10)
            return json.dumps([skin.__dict__ for skin in roulette.m_skinsArray])

    def launchRoutingService(self):

        self._launchDomainServices()
        self.declareRoutes()
        port = int(os.environ.get('PORT', 5000))
        self.m_server.run(host='0.0.0.0', port=port)

    def _launchDomainServices(self):
        self.m_rouletteService = RouletteService()
