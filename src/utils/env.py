from typing import Dict, Optional
from dotenv import dotenv_values
import os

def load_env() -> Dict[str, Optional[str]]:
  config = dotenv_values(".env")

  return config

def get_env_var(var: str) -> str:
  config = load_env()

  value = os.getenv(var)
  
  if value == None:
    value = config[var]
  return value