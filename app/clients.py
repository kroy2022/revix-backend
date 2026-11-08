"""
Generate Clients to persist across service
"""
import boto3, os
from dotenv import load_dotenv

load_dotenv()

def get_s3_client():
    return boto3.client(
        service_name="s3",
        endpoint_url=str(os.getenv("CLOUDFLARE_ENDPOINT_URL")),
        aws_access_key_id=str(os.getenv("CLOUDFLARE_ACCESS_KEY_ID")),
        aws_secret_access_key=str(os.getenv("CLOUDFLARE_SECRET_ACCESS_KEY")),
        region_name="auto",
    )