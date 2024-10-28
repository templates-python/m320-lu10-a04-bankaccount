class AccountIndexException(Exception):

    def __init__(self, index, max):
        super().__init__(f'Ungültiger Indexwert: {max} Einträge vorhanden, Nummer {index} gefordert')