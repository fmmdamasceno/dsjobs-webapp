import requests

from requests import auth
from utils.env import get_env_var

class GCloud:
  def __init__(self) -> None:
      self.url = get_env_var('API_URL')
      username = get_env_var('BASIC_AUTH_USERNAME')
      password = get_env_var('BASIC_AUTH_PASSWORD')
      self.credentials = (username, password)

  def predict(self, body: str) -> str:
      
      response = requests.post(url=self.url, data=body, auth=self.credentials)

      return response.json()