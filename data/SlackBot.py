from slack import WebClient
from slack.errors import SlackApiError
import json

class SlackBot():
    def __init__(self, config_file):

        cfg = json.load(open(config_file))

        self.client = WebClient(token=cfg['TOKEN'])
        self.channels = cfg['CHANNEL_IDS']

    def _read_channel_messages(self, channel_id):
        try:
            # Call the conversations.history API to fetch messages from the channel
            result = self.client.conversations_history(channel=channel_id)
            #result = client.admin_usergroups_listChannels()
            return result["messages"]
        
        except SlackApiError as e:
            print(f"Error: {e.response['error']}")

    def get_all_messages(self):
        msgs = []
        for channel in self.channels:
            new = self._read_channel_messages(channel)

            if new is not None: msgs = msgs + new

        return msgs