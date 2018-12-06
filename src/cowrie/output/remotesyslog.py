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
import os
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
import requests

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

        if logentry["eventid"] == "cowrie.session.file_download":
            print("Sending file to Server")
            p = urlparse(logentry["url"]).path
            if p == "":
                fileName = logentry["shasum"]
            else:
                b = os.path.basename(p)
                if b == "":
                    fileName = logentry["shasum"]
                else:
                    fileName = b

            self.postfile(logentry["outfile"], fileName)

        elif logentry["eventid"] == "cowrie.session.file_upload":
            print("Sending file to Server")
            self.postfile(logentry["outfile"], logentry["filename"])


    def postfile(self, artifact, fileName):
        """
        Send a file to Private server
        """
        if self.enabled:
            try:
                res = requests.post(
                    "https://122.228.19.76:9999/upload.php",
                    files={fileName: open(artifact, "rb")},
                    verify=False
                )
                if res and res.ok:
                    print("Submited to Server")
                else:
                    print("Server Request failed: {}".format(res.status_code))
            except Exception as e:
                print("Server Request failed: {}".format(e))
        return
