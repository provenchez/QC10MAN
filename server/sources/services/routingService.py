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
            return 	"Win	Loss	(+/-)"

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
