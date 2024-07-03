from chatterbot import ChatBot
from chatterbot import comparisons, response_selection

bot = ChatBot(
    'Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": comparisons.levenshtein_distance,
            "response_selection_method": response_selection.get_first_response
        }
    ],
)

def get_response(usrText):
    if usrText.strip() != 'Bye':
        result = bot.get_response(usrText)
        reply = str(result)
        return reply
    else:
        return 'Bye'
