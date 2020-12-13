from pydantic.main import BaseModel



class ConfigForm(BaseModel):
    stopwords_dict: str = ''
    stopwords_style: int
    stopwords_text: str = ''

    splitwords_style: int
    splitwords_text: str = ''

    synonymwords_style: int
    synonymwords_text: str = ''

    combineauthor_style: int
    combineauthor_text: str = ''

    combineorg_style: int
    combineorg_text: str = ''

    combineprovince_style: int
    combineprovince_text: str = ''

    combinecountry_style: int
    combinecountry_text: str = ''

    combinefund_style: int
    combinefund_text: str = ''

    combinebranch_style: int
    combinebranch_text: str = ''

    kw_freq_style: str = ''
    kw_freq_value: int = 1



from api import dao, config

class ConfigManager:
    def __init__(self):
        pass

    def save(self, form : ConfigForm):
        # 插入的value是个数组
        dd = [{'userid':'test', 'style':k, 'values':str(v).split('\n'), 'alias':''} for k,v in form.dict().items()]
        dao.insert_dim_config(dd)



configManager = ConfigManager()