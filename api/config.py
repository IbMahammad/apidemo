from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")  #getenv gedecek env faylindan api_key deyisenini goturecek

if not API_KEY:
    raise ValueError("API_KEY not found in env file.")

