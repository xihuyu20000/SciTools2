'''
api/db 所有的数据库操作，不区分数据库
'''
from api import config
from api.dao.db import ad_dataset, ad_tbls, dim_dataset, dim_user, ods_bib, dim_config, dim_org
from api.dao.db import __create, __drop, __truncate, __execute
##################################################################################
create_ad_dataset = ad_dataset.create if config.db_is_clickhouse else None
drop_ad_dataset = ad_dataset.drop if config.db_is_clickhouse else None
execute_ad_dataset = ad_dataset.execute if config.db_is_clickhouse else None
insert_ad_dataset = ad_dataset.insert if config.db_is_clickhouse else None
query_ad_dataset = ad_dataset.query if config.db_is_clickhouse else None
##################################################################################
create_ad_tbls = ad_tbls.create if config.db_is_clickhouse else None
drop_ad_tbls = ad_tbls.drop if config.db_is_clickhouse else None
execute_ad_tbls = ad_tbls.execute if config.db_is_clickhouse else None
insert_ad_tbls = ad_tbls.insert if config.db_is_clickhouse else None
query_ad_tbls = ad_tbls.query if config.db_is_clickhouse else None
##################################################################################
create_dim_config = dim_config.create if config.db_is_clickhouse else None
drop_dim_config = dim_config.drop if config.db_is_clickhouse else None
insert_dim_config = dim_config.insert if config.db_is_clickhouse else None
delete_dim_config = dim_config.delete if config.db_is_clickhouse else None
query_dim_config = dim_config.query if config.db_is_clickhouse else None
##################################################################################

create_dim_dataset = dim_dataset.create if config.db_is_clickhouse else None
drop_dim_dataset = dim_dataset.drop if config.db_is_clickhouse else None
insert_dim_dataset = dim_dataset.insert if config.db_is_clickhouse else None
find_dim_dataset = dim_dataset.query if config.db_is_clickhouse else None
update_dim_dataset = dim_dataset.update if config.db_is_clickhouse else None
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
