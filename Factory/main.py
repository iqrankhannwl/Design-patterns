from lang_client import LanguageClient

creds = "urdu"
rudu = getattr(LanguageClient, creds)(creds=creds).translation()
print(rudu)
creds = "english"
english = getattr(LanguageClient, creds)(creds=creds).translation()
print(english)
