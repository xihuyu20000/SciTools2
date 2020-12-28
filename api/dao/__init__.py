'''
api/db 所有的数据库操作，不区分数据库
'''
##################################################################################
from api.dao.ad_dataset import ad_dataset
from api.dao.ad_tbls import ad_tbls
from api.dao.dim_config import dim_config
from api.dao.sci_meta import sci_meta
from api.dao.dim_org import dim_org
from api.dao.dim_user import dim_user
from api.dao.sci_dataset import sci_dataset

create_ad_dataset = ad_dataset.create
drop_ad_dataset = ad_dataset.drop
execute_ad_dataset = ad_dataset.execute
insert_ad_dataset = ad_dataset.insert
query_ad_dataset = ad_dataset.query
##################################################################################
create_ad_tbls = ad_tbls.create
drop_ad_tbls = ad_tbls.drop
execute_ad_tbls = ad_tbls.execute
insert_ad_tbls = ad_tbls.insert
query_ad_tbls = ad_tbls.query
##################################################################################
create_dim_config = dim_config.create
drop_dim_config = dim_config.drop
insert_dim_config = dim_config.insert
delete_dim_config = dim_config.delete
query_dim_config = dim_config.query
##################################################################################

create_dim_dataset = sci_meta.create
drop_dim_dataset = sci_meta.drop
insert_dim_dataset = sci_meta.insert
find_dim_dataset = sci_meta.query
update_dim_dataset = sci_meta.update
##################################################################################

create_dim_org = dim_org.create
drop_dim_org = dim_org.drop
insert_dim_org = dim_org.insert
find_dim_org = dim_org.query

###################################################################################

create_dim_user = dim_user.create
drop_dim_user = dim_user.drop
insert_dim_user = dim_user.insert
get_user = dim_user.get_user

##################################################################################

create_ods_bib = sci_dataset.create
drop_ods_bib = sci_dataset.drop
insert_ods_bib = sci_dataset.insert
update_ods_bib = sci_dataset.update
# delete_ods_bib = sci_dataset.delete
query_sci_dataset = sci_dataset.query

##################################################################################
