import time
import os
from pathlib import Path
CNKI = "cnki_custom_format"
UPLOAD_BASE_HOME = r'E:\workspace\workspace-js\scitools\apiserver\upload'

def get_upload_home():
    # 获得当前系统时间的字符串
    localtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    p = Path(os.path.join(UPLOAD_BASE_HOME, localtime))
    p.mkdir(exist_ok=True, parents=True)
    return p
