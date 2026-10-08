import os

print("BOT_TOKEN exists:", "BOT_TOKEN" in os.environ)
print("BOT_TOKEN length:", len(os.getenv("BOT_TOKEN", "")))
