import json
import os
from typing import Callable

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv(".env")
if not (SLACK_BOT_TOKEN := os.environ.get("SLACK_BOT_TOKEN")):
    raise ValueError("SLACK_BOT_TOKEN environment variable is not set.")
if not (SLACK_APP_TOKEN := os.environ.get("SLACK_APP_TOKEN")):
    raise ValueError("SLACK_APP_TOKEN environment variable is not set.")


# Install the Slack app
app = App(token=SLACK_BOT_TOKEN)


@app.message("")
def message_hello(message: dict, say: Callable) -> None:
    """Respond to a message with a message."""
    print(message)
    say(f"received {json.dumps(message)}")


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()  # type: ignore
