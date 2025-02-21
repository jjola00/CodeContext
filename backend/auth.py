import os
from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

API_KEY = os.getenv("API_KEY") 
API_KEY_NAME = "X-API-Key"  

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def verify_api_key(api_key: str = Security(api_key_header)):
    """
    Verify the API key provided in the request header.
    If the API key is invalid, raise an HTTP 403 error.
    """
    if api_key != API_KEY:
        raise HTTPException(
            status_code=403, 
            detail="Invalid API Key"
        )
    return api_key