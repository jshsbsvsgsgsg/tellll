CLIENT_ID = "8357861387f34931a018d986bc3d794e"
CLIENT_SECRET = "7f5ef685f346497d9b91254de5dedd86"
API_ID = 1806802
API_HASH = "d049c66c31e53ff950a9d9dbb16ad6e7"
INITIAL_TOKEN = "AQDkCt9tPJohc3zD9YzeaT_DmeqppImrz1jlKeA4eLq7-jCbXWb5D-htJMp6c2rvVzsJ7JrTkiM0Gri9R9nMJ2wFuo4K7LTA8ih2yOj0kcsF9Jn750bd2FtIvpl99CPmYaW24F1mMQYMy0PPusIvSEvVTz5_ELusOMfCsquHpj8IGJimGTFJHsOyEu9O5e121yhfLnG1USh50ffdQf0kqFAvy-Ft1bXceUNtIbYQw8abWD8ew-oQ"
INITIAL_BIO = ""
LOG = "https://t.me/joinchat/Qyp2LlD9E2dTTfJICJqltA"
# the escaping is necessary since we are testing against a regex pattern with it.
SHUTDOWN_COMMAND = "\/\/stop"
# The key which is used to determine if the current bio was generated from the bot ot from the user. This means:
# NEVER use whatever you put here in your original bio. NEVER. Don't do it!
KEY = '🎶'
# The bios MUST include the key. The bot will go though those and check if they are beneath telegrams character limit.
BIOS = [KEY + ' Now Playing: {interpret} - {title} {progress}/{duration}',
        KEY + ' Now Playing: {interpret} - {title}',
        KEY + ' : {interpret} - {title}',
        KEY + ' Now Playing: {title}',
        KEY + ' : {title}']
# Mind that some characters (e.g. emojis) count more in telegram more characters then in python. If you receive an
# AboutTooLongError and get redirected here, you need to increase the offset. Check the special characters you either
# have put in the KEY or in one of the BIOS with an official Telegram App and see how many characters they actually
# count, then change the OFFSET below accordingly. Since the standard KEY is one emoji and I don't have more emojis
# anywhere, it is set to one (One emoji counts as two characters, so I reduce 1 from the character limit).
OFFSET = 1
# reduce the OFFSET from our actual 70 character limit
LIMIT = 70 - OFFSET
