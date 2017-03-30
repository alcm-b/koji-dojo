#!/usr/bin/python

import koji
s = koji.ClientSession("http://172.17.0.3/kojihub")
tasks = s.listTasks(opts={'method': 'buildArch', 'state': [koji.TASK_STATES['FAILED']], 'decode': True})
for i in tasks:
        print i['id']

