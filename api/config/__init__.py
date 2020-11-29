'''
api/config负责管理所有的配置信息
'''

# 存放数据文件的个目录
import os

base_file_dir = '.'

# 数据源类型
ds_cnki_es5 = '题录—知网—es5'
ds_gbt_7714_2015 = '题录—GBT 7714-2015'
ds_note_express = '题录—知网—NoteExpress'
ds_cnki_html = 'cnki_html'

# 数据字典
dict_stop = 'dict_stop'  # 停用词词典
dict_synonym = 'dict_synonym'  # 同义词词典
dict_country = 'dict_country'  # 国家字典
dict_province = 'dict_province'  # 省份字典
dict_org = 'dict_org'  # 机构字典

# 数据去重
clean_article_redu = 'clean_article_redu'  # 文献去重
clean_split_words = 'clean_split_words'  # 智能分词

# 当前正在使用的数据库类型
db_is_clickhouse = True
db_is_pg = False

# 数据库clickhouse配置
clickhouse_ip = '192.168.61.100'
clickhouse_user = 'default'
clickhouse_password = 'admin'
clickhouse_db = 'default'

# 数据库表名称
tbl_dim_threshold = 'default.dim_threshold'
tbl_dim_dict = 'default.dim_dict'
tbl_dim_year = 'default.dim_year'
tbl_ods_bib = 'default.ods_bib'

# 配置文件的路径
_base = os.path.join(os.path.abspath('.').split(r"api")[0], 'api', 'config')
user_cut_dict_path = os.path.join(_base, 'user_cut.dict')
