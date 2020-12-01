from pydantic.main import BaseModel

class ConfigForm(BaseModel):
    stopwords_dict: str = None

class ConfigManager:
    def __init__(self):
        pass

    def save(self, form : ConfigForm):
        pass


configManager = ConfigManager()