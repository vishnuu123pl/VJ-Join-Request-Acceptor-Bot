from os import environ

API_ID = int(environ.get("API_ID", "13305226"))
API_HASH = environ.get("API_HASH", "8cde2475d6b0cb1162b89ebbac71a95d")
BOT_TOKEN = environ.get("BOT_TOKEN", "5079210218:AAHXnnkfARPeqZGQlaKNsIC9ts8LU9Z0_28")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001362823844"))
ADMINS = int(environ.get("ADMINS", "1258310642"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
