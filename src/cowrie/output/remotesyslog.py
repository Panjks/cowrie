# -*- coding: utf-8 -*-
# Simple syslog logger

"""
@Time : 2018/11/27 17:28
@Author : Panjks-
@Description : Remote Syslog Output
"""

from __future__ import absolute_import, division

import logging
import logging.handlers
import json

import cowrie.core.output
from cowrie.core.config import CONFIG


class Output(cowrie.core.output.Output):

    def __init__(self):
        self.host = CONFIG.get('output_remotesyslog', 'host')
        self.port = CONFIG.get('output_remotesyslog', 'port')
        cowrie.core.output.Output.__init__(self)

    def start(self):
        self.logger = logging.getLogger()
        fh = logging.handlers.SysLogHandler((self.host, int(self.port)), logging.handlers.SysLogHandler.LOG_AUTH)
        formatter = logging.Formatter('%(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def stop(self):
        pass

    def write(self, logentry):
        for i in list(logentry.keys()):
            # remove twisted 15 legacy keys
            if i.startswith('log_'):
                del logentry[i]

        self.logger.error(json.dumps(logentry).rstrip('\t\r\n\0'))
