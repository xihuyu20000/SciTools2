from api import const
from api.dao.models import BaseDao
from api.util.utils import Logger

'''
高级图表：图表定义。
'''
class AdGraph(BaseDao):
    def __init__(self):
        self.graphid = ''
        self.userid = ''
        self.tblid = ''
        self.graphname = ''
        self.option = ''

        self._log = Logger(__name__).get_log
        self.TBL_NAME = const.tbl_ad_graphs
        self._create_sql = """
            CREATE TABLE ad_graphs(
                graphid String DEFAULT toString(generateUUIDv4()) COMMENT '主键',
                userid String NOT NULL COMMENT '用户表主键',
                tblid String NOT NULL COMMENT '数据元表主键',
                graphname String COMMENT '表名称',
                option String COMMENT 'echarts的配置项目'
            ) ENGINE = MergeTree() PARTITION  BY graphid ORDER BY graphid PRIMARY KEY graphid
        """

ad_graph = AdGraph()