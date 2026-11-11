import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, request, session

from anime_dashboard.app.oauth_authorization import OAuthClientAuthorization


def create_app(oauth_authorization: OAuthClientAuthorization):
    app = Flask(__name__)

    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")

    @app.route("/")
    def login() -> str:
        url, client_state, verifier = oauth_authorization.start()
        session["client_state"] = client_state
        session["verifier"] = verifier
        return redirect(url)

    @app.route("/callback", methods=["GET"])
    def api_callback() -> str:
        authorization_code = request.args.get("code")
        server_state = request.args.get("state")

        check = oauth_authorization.complete(
            server_state,
            session["client_state"],
            authorization_code,
            session["verifier"],
        )

        return check

    @app.route("/tokens", methods=["POST"])
    def store_access_refesh_codes() -> str:
        pass

    return app
