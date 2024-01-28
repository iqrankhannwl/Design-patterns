class Chiness:
    def __init__(self, creds):
        if creds != "chinese":
            raise Exception("Invalide creds")
        
    def translation(self):
        return "From Chines Language"


