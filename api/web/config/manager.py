from pydantic.main import BaseModel



class ConfigForm(BaseModel):
    stopwords_style: str= '1'
    stopwords_text: str = ''

    splitwords_style: str= '1'
    splitwords_text: str = ''

    synonymwords_style: str= '1'
    synonymwords_text: str = ''

    orgnorm_style:str= '1'
    orgnorm_text:str = ''

    combineauthor_style: str= '1'
    combineauthor_text: str = ''

    combineorg_style: str= '1'
    combineorg_text: str = ''

    combineprovince_style: str= '1'
    combineprovince_text: str = ''

    combinecountry_style: str= '1'
    combinecountry_text: str = ''

    combinefund_style: str= '1'
    combinefund_text: str = ''

    combinebranch_style: str= '1'
    combinebranch_text: str = ''

    kw_freq_style: str = ''
    kw_freq_value: int = 1



from api import dao, config

class ConfigManager:
    def __init__(self):
        pass

    def save(self, form : ConfigForm):
        userid = 'test'
        # 先删除再插入
        dao.delete_dim_config(userid)
        dd = [{'userid':'test', 'style':k, 'values':str(v)} for k,v in form.dict().items()]
        sql = """ INSERT INTO {} (userid, style, values) VALUES """.format(config.tbl_dim_config)
        dao.insert_dim_config(sql, dd)

    def find(self, sql):
        return dao.query_dim_config(sql)

configManager = ConfigManager()