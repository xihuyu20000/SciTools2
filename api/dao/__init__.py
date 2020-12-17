'''
api/db 所有的数据库操作，不区分数据库
'''
from api import config
from api.dao.db import dim_dataset, dim_user, ods_bib, dim_config, dim_org
from api.dao.db import __create, __drop, __truncate, __execute
##################################################################################
execute = __execute
create_dim_config = dim_config.create_dim_config if config.db_is_clickhouse else None
drop_dim_config = dim_config.drop_dim_config if config.db_is_clickhouse else None
truncate_dim_config = dim_config.truncate_dim_config if config.db_is_clickhouse else None
insert_dim_config = dim_config.insert_dim_config if config.db_is_clickhouse else None
delete_dim_config = dim_config.delete_dim_config if config.db_is_clickhouse else None
find_dim_config = dim_config.find_dim_config if config.db_is_clickhouse else None
##################################################################################

create_dim_dataset = dim_dataset.create_dim_dataset if config.db_is_clickhouse else None
drop_dim_dataset = dim_dataset.drop_dim_dataset if config.db_is_clickhouse else None
truncate_dim_dataset = dim_dataset.truncate_dim_dataset if config.db_is_clickhouse else None
insert_dim_dataset = dim_dataset.insert_dim_dataset if config.db_is_clickhouse else None
find_dim_dataset = dim_dataset.find_dim_dataset if config.db_is_clickhouse else None
update_dim_dataset = dim_dataset.update_dim_dataset if config.db_is_clickhouse else None
##################################################################################

create_dim_org = dim_org.create_dim_org if config.db_is_clickhouse else None
drop_dim_org = dim_org.drop_dim_org if config.db_is_clickhouse else None
truncate_dim_org = dim_org.truncate_dim_org if config.db_is_clickhouse else None
insert_dim_org = dim_org.insert_dim_org if config.db_is_clickhouse else None
find_dim_org = dim_org.find_dim_org if config.db_is_clickhouse else None

###################################################################################

create_dim_user = dim_user.create_dim_user if config.db_is_clickhouse else None
drop_dim_user = dim_user.drop_dim_user if config.db_is_clickhouse else None
truncate_dim_user = dim_user.truncate_dim_user if config.db_is_clickhouse else None
insert_dim_user = dim_user.insert_dim_user if config.db_is_clickhouse else None
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
