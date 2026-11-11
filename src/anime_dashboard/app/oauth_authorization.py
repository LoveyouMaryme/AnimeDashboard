import secrets
from urllib.parse import urlencode

import requests
from requests.exceptions import HTTPError

from anime_dashboard.app.oauth_client import OAuthClient
from anime_dashboard.infrastructure.token_storage import TokenStorage


class OAuthClientAuthorization:
    def __init__(self, client: OAuthClient, storage: TokenStorage):
        self.client = client
        self.storage = storage

    def start(self) -> tuple[str, str, str]:
        """
        Start the Authorization Process if the storage doesn't
        contain any access token inside

        args:
            storage : The storage we use to stock our OAuth Tokens


        """

        if self.storage.load() is None:
            state = secrets.token_urlsafe(32)
            code_verifier = secrets.token_urlsafe(32)
            code_challenge = code_verifier
            url_endpoint = self.client.authorization_endpoint

            params = {
                "response_type": "code",
                "client_id": self.client.client_id,
                "redirect_uri": self.client.redirect_uri,
                "scope": self.client.scope,
                "code_challenge": code_challenge,
                "code_challenge_method": "plain",
                "state": state,
            }

            url_params = urlencode(params)
            url_request = url_endpoint + "?" + url_params

            return [url_request, state, code_verifier]

    def complete(
        self,
        server_state_code: str,
        client_state_code: str,
        authorization_code: str,
        code_verifier: str,
    ) -> str:
        try:
            data = {
                "client_id": self.client.client_id,
                "client_secret": self.client.client_secret,
                "grant_type": "authorization_code",
                "code": authorization_code,
                "redirect_uri": self.client.redirect_uri,
                "code_verifier": code_verifier,
            }
            if server_state_code == client_state_code:
                response = requests.post(
                    self.client.token_endpoint, data=data, timeout=30
                )

            print(response)

            response.raise_for_status()
            tokens = response.json()

            return tokens
        except HTTPError as err:
            # Check if it was specifically a 400 error
            if err.response.status_code == 400:
                print("Caught a 400 Bad Request!")
                print("Server message:", err.response.text)
            else:
                print(f"Caught another HTTP Error: {err.response.status_code}")
