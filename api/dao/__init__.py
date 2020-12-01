'''
api/db 所有的数据库操作，不区分数据库
'''
from api import config
from api.dao.db.clickhouse_db import dim_dict, dim_file, dim_user, ods_bib

##################################################################################

create_dim_dict = dim_dict.create_dim_dict if config.db_is_clickhouse else None
drop_dim_dict = dim_dict.drop_dim_dict if config.db_is_clickhouse else None
truncate_dim_dict = dim_dict.truncate_dim_dict if config.db_is_clickhouse else None
insert_dim_dict = dim_dict.insert_dim_dict if config.db_is_clickhouse else None
delete_dim_dict = dim_dict.delete_dim_dict if config.db_is_clickhouse else None
##################################################################################

create_dim_file = dim_file.create_dim_file if config.db_is_clickhouse else None
drop_dim_file = dim_file.drop_dim_file if config.db_is_clickhouse else None
truncate_dim_file = dim_file.truncate_dim_file if config.db_is_clickhouse else None
insert_dim_file = dim_file.insert_dim_file if config.db_is_clickhouse else None
find_all_files = dim_file.find_all_files if config.db_is_clickhouse else None
##################################################################################

create_dim_user = dim_user.create_dim_user if config.db_is_clickhouse else None
drop_dim_user = dim_user.drop_dim_user if config.db_is_clickhouse else None
truncate_dim_user = dim_user.truncate_dim_user if config.db_is_clickhouse else None
insert_dim_dict = dim_user.insert_dim_user if config.db_is_clickhouse else None
get_user = dim_user.get_user if config.db_is_clickhouse else None

##################################################################################

create_ods_bib = ods_bib.create_ods_bib if config.db_is_clickhouse else None
drop_ods_bib = ods_bib.drop_ods_bib if config.db_is_clickhouse else None
truncate_ods_bib = ods_bib.truncate_ods_bib if config.db_is_clickhouse else None
insert_ods_bib = ods_bib.insert_ods_bib if config.db_is_clickhouse else None
update_ods_bib = ods_bib.update_ods_bib if config.db_is_clickhouse else None
delete_ods_bib = ods_bib.delete_ods_bib if config.db_is_clickhouse else None
find_ods_bib = ods_bib.find_ods_bib if config.db_is_clickhouse else None

##################################################################################
