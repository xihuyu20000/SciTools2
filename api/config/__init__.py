'''
api/config负责管理所有的配置信息
'''

# 存放数据文件的个目录
base_file_dir = '.'

# 数据源类型
ds_cnki_es5 = 'cnki_es5'
ds_gbt_7714_2015 = 'gbt_7714_2015'
ds_note_express = 'note_express'
ds_cnki_html = 'cnki_html'

# 数据字典
dict_stop = 'dict_stop'  # 停用词词典
dict_synonym = 'dict_synonym'  # 同义词词典
dict_country = 'dict_country'  # 国家字典
dict_province = 'dict_province'  # 省份字典
dict_org = 'dict_org'  # 机构字典

# 数据去重
clean_article_redu = 'clean_article_redu'   # 文献去重
clean_split_words = 'clean_split_words' # 智能分词


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
tbl_ods_bib = 'default.ods_bib'
