class MessageManager:
    def __init__(self):
        pass

    def publicPrint(self, msg: str):
        print(f"Publ> {msg}")

    def privatePrint(self, msg: str, player: int):
        print(f"Priv> Player {player}, {msg} ")

    def privateAsk(self, msg: str, player: int):
        return input(f"PriA> Player {player}, {msg} ")