import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "26477680").strip()
API_HASH = os.getenv("API_HASH", "b0d8504752cc1ecf52009ece2bdef0b8").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6621888094:AAFiXgDSPC2PwFnlU_AqFptimOser6AuJmE").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://uek4iv7la3bvm5:p83d5f560af48e547a6f00a853fad2e28344b937dbe448095ff2bf53cd54eef7c@cbbirn8v9855bl.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dase5nfs9hvv3").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "musik_supportdan")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
