class English:
    def __init__(self, creds):
        if creds != "english":
            raise Exception("Invalide creds")
        
    def translation(self):
        return "From English Language"
