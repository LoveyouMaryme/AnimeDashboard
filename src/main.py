import os

from dotenv import find_dotenv, load_dotenv

from anime_dashboard.app.oauth_authorization import OAuthClientAuthorization
from anime_dashboard.infrastructure.fake_token_storage import FakeTokenStorage
from anime_dashboard.infrastructure.mal_oauth_client import MALOAuthClient
from anime_dashboard.presentation.flask.main import create_app

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

SCOPES = ["write:users"]
MAL_CLIENT_ID = os.getenv("MAL_CLIENT_ID")
MAL_CLIENT_SECRET = os.getenv("MAL_CLIENT_SECRET")

mal_oauth_client = MALOAuthClient(
    "http://localhost:8080/callback", MAL_CLIENT_ID, SCOPES[0], MAL_CLIENT_SECRET
)
storage = FakeTokenStorage()
oauth_processus = OAuthClientAuthorization(mal_oauth_client, storage)

app = create_app(oauth_processus)
if __name__ == "__main__":
    app.run(port=8080)
