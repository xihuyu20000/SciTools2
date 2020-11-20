'''
api/db 所有的数据库操作，不区分数据库
'''
from api import config
from api.db.clickhouse_db import ch_dim_dict, ch_ods_bib, ch_dim_threshold

##################################################################################

create_dim_dict = ch_dim_dict.create_dim_dict if config.db_is_clickhouse else None
drop_dim_dict = ch_dim_dict.drop_dim_dict if config.db_is_clickhouse else None
truncate_dim_dict = ch_dim_dict.truncate_dim_dict if config.db_is_clickhouse else None
insert_dim_dict = ch_dim_dict.insert_dim_dict if config.db_is_clickhouse else None
delete_dim_dict = ch_dim_dict.delete_dim_dict if config.db_is_clickhouse else None

##################################################################################

create_dim_threshold = ch_dim_threshold.create_dim_threshold if config.db_is_clickhouse else None
drop_dim_threshold = ch_dim_threshold.drop_dim_threshold if config.db_is_clickhouse else None
truncate_dim_threshold = ch_dim_threshold.truncate_dim_threshold if config.db_is_clickhouse else None
insert_dim_threshold = ch_dim_threshold.insert_dim_threshold if config.db_is_clickhouse else None
delete_dim_threshold = ch_dim_threshold.delete_dim_threshold if config.db_is_clickhouse else None

##################################################################################

create_ods_bib = ch_ods_bib.create_ods_bib if config.db_is_clickhouse else None
drop_ods_bib = ch_ods_bib.drop_ods_bib if config.db_is_clickhouse else None
truncate_ods_bib = ch_ods_bib.truncate_ods_bib if config.db_is_clickhouse else None
insert_ods_bib = ch_ods_bib.insert_ods_bib if config.db_is_clickhouse else None
update_ods_bib = ch_ods_bib.update_ods_bib if config.db_is_clickhouse else None
delete_ods_bib = ch_ods_bib.delete_ods_bib if config.db_is_clickhouse else None
find_ods_bib = ch_ods_bib.find_ods_bib if config.db_is_clickhouse else None

##################################################################################
