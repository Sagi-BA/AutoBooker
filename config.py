import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
GOOGLE_CLOUD_SPEECH_KEY = os.getenv('GOOGLE_CLOUD_SPEECH_KEY')

# Database Configuration
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Other Configuration
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', 60))
