from flask import Flask
server = Flask(__name__)

@server.route("/")
def main():
    return "flask app responding hello world !"

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
    server.run(host='0.0.0.0', port=port)