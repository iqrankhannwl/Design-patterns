class Urdu:

    def __init__(self, creds) -> None:
        if creds != "urdu":
            raise Exception("Invalide creds")
    
    def translation(self):
        return "From Urdu Language"