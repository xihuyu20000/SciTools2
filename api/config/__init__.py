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

# 数据库clickhouse配置
clickhouse_ip = '192.168.61.100'
clickhouse_user = 'default'
clickhouse_password = 'admin'
clickhouse_db = 'default'

# 数据库表名称
tbl_ods_cnki_bib = 'default.ods_cnki_bib'
