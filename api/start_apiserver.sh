# -*- coding: utf-8 -*-
#!/bin/bash
chmod u+x ./main.py
nohup  python ./main.py  start>apiserver_log 2>&1 &