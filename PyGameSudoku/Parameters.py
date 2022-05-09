def LoadParameters():
    with open(".\\app.config") as file:
        from  json import load
        from PyGameSudoku.DynamicClass import DynamicClass
        _dict = load(file)
        Config = DynamicClass(_dict)
        return Config

Config = LoadParameters()

def LoanItems(Config):
    output = []
    from PyGameSudoku.ButtonClass import ButtonClass
    for id, dc in Config.items.__dict__.items():
        if dc.type == "button":
            button = ButtonClass(id)
            button.update(dc)
            output.append(button)
    return output

ButtonItems = LoanItems(Config)