import os
import secrets
from urllib.parse import urlencode

from dotenv import find_dotenv, load_dotenv

from anime_dashboard.infrastructure.oauth_token import OAuthTokens


class MALOAuthClient:
    """"""

    """"""

    def __init__(
        self, redirect_uri: str, token_endpoint: str, client_id: str, scope: str
    ):
        self.redirect_uri = redirect_uri
        self.token_endpoint = (token_endpoint,)
        self.client_id = client_id
        self.scope = scope

    def initialize(self) -> str:
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)

        os.getenv("MAL_CLIENT_SECRET")

        state = secrets.token_urlsafe(32)
        code_verifier = secrets.token_urlsafe(32)
        code_challenge = code_verifier
        authorization_endpoint = "https://myanimelist.net/v1/oauth2/authorize"
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": self.scope,
            "code_challenge": code_challenge,
            "code_challenge_method": "plain",
            "state": state,
        }

        url_params = urlencode(params)
        url_request = authorization_endpoint + "?" + url_params

        return url_request

    def refresh(self, refresh_token: str) -> OAuthTokens: ...


SCOPES = ["write:users"]

test = MALOAuthClient(
    "http://localhost:8080/callback", os.getenv("MAL_CLIENT_ID"), SCOPES[0]
)
print(test.initialize())
