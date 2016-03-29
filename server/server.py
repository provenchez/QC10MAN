from flask import Flask
server = Flask(__name__)

@server.route("/")
def main():
    return "flask app responding hello world !"

if __name__ == "__main__":