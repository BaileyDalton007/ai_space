from SlackBot import SlackBot
import re

class ArticleData():
    def __init__(self, slack_config="slack_config.json"):
        bot = SlackBot(slack_config)
        msgs = bot.get_all_messages()

        self.urls = []
        for msg in msgs:
            found_urls = self._find_url(msg.get('text'))
            self.urls = self.urls + found_urls

    def _find_url(self, string):
        # Don't ask, based off of https://www.geeksforgeeks.org/python-check-url-string/#
        regex = r"\b((?:https?:\/\/|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}\/)(?:[^\s()|[\]<>]+|\(([^\s()|[\]<>]+|(\([^\s()|[\]<>]+\)))*\))+(?:\(([^\s()|[\]<>]+|(\([^\s()|[\]<>]+\)))*\)|[^\s`!()|\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex, string)
        return [x[0] for x in url]

    def get_urls(self):
        return self.urls
    
    def write_to_txt(self, file_name="slack_output.txt"):
        with open(file_name, "w") as file:
            for item in self.get_urls():
                file.write(item + "\n")