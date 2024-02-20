from hatchet_sdk import Hatchet
from dotenv import load_dotenv

load_dotenv()

# Create a Hatchet instance that will be shared across all workflows
hatchet = Hatchet(debug=True)
