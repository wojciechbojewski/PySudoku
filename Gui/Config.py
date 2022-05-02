import json

class GameParameters(object):
    _instance = None
    Config = None
    def __new__(cls):
        if cls._instance is None:
            with open(".\\Gui\\main_board.json") as file:
                    cls.Config = json.load(file)
            cls._instance = super(GameParameters, cls).__new__(cls)
        return cls._instance


