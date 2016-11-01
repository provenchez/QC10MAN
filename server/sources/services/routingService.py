from flask import Flask
import json
import os

class RoutingService:

    m_server = Flask(__name__)

    def declareRoutes(self):
        @self.m_server.route("/")
        def index():
            return 	"Vez est gay"

        @self.m_server.route('/index')
        def index():
            return "Hello, World!"

    def launchRoutingService(self):
        self._launchDomainServices()
        self.declareRoutes()
        port = int(os.environ.get('PORT', 5000))
        self.m_server.run(host='0.0.0.0', port=port, debug=True)

