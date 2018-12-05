Cowrie
======

![Travis CI Status](https://travis-ci.org/cowrie/cowrie.svg?branch=master "Travis CI Status")

# Cowrie GitHub repository edited by panjks-

## 修改内容

1. 添加了日志中外网IP的json字段，格式为`{"dest_ip": 127.0.0.1}`

2. ~~修改了Linux下`free`命令的内存大小。~~

   因更新后cowrie实现了简单的动态显示内存，暂时使用该功能，暂未进行测试。

3. ~~修改hostname为`ubuntu`，文件路径为：`honeyfs/etc/hostname`~~

   这个需要使用配置文件中的hostname字段进行修改。

4. 修改pre-login banner为`Ubuntu 16.04.5 LTS \n \l`，文件路径为：`honeyfs/etc/issuel`

5. 修改post-login banner为以下，文件路径为：`honeyfs\etc\motd`

   ```
   
   Welcome to Ubuntu 16.04.5 LTS (GNU/Linux 4.4.0-1066-aws x86_64)
   
    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage
   
     Get cloud support with Ubuntu Advantage Cloud Guest:
       http://www.ubuntu.com/business/services/cloud
   
   0 packages can be updated.
   0 updates are security updates.
   
   
   Last login: Mon Aug 27 06:27:10 2018 from 127.0.0.1
   
   ```

6. 修改cpu信息为`Intel(R) Xeon(R) CPU X5650 @ 2.67GHz`，文件路径为：`honeyfs/proc/cpuinfo`

## 待修改内容

1. 定时删除日志？

# Welcome to the Cowrie GitHub repository

This is the official repository for the Cowrie SSH and Telnet
Honeypot effort.

# What is Cowrie

Cowrie is a medium interaction SSH and Telnet honeypot designed to
log brute force attacks and the shell interaction performed by the
attacker.

[Cowrie](http://github.com/cowrie/cowrie/) is developed by Michel Oosterhof.

## Slack

You can join the Cowrie community at the following [Slack workspace](http://bit.ly/cowrieslack)

## Features

Some interesting features:

* Fake filesystem with the ability to add/remove files. A full fake filesystem resembling a Debian 5.0 installation is included
* Possibility of adding fake file contents so the attacker can `cat` files such as `/etc/passwd`. Only minimal file contents are included
* Session logs are stored in an [UML Compatible](http://user-mode-linux.sourceforge.net/)  format for easy replay with original timings with the `bin/playlog` utility.
* Cowrie saves files downloaded with wget/curl or uploaded with SFTP and scp for later inspection
log
Additional functionality over standard kippo:

* SFTP and SCP support for file upload
* Support for SSH exec commands
* Logging of direct-tcp connection attempts (ssh proxying)
* Forward SMTP connections to SMTP Honeypot (e.g. [mailoney](https://github.com/awhitehatter/mailoney))
* Logging in JSON format for easy processing in log management solutions
* Many, many additional commands

## Docker

Docker versions are available.
* Get the Dockerfile directly at https://github.com/cowrie/docker-cowrie
* Run from Docker Hub with: ```docker pull cowrie/cowrie```

## Requirements

Software required:

* Python 2.7+, (Limited Python 3 support available for SSH only)
* python-virtualenv

For Python dependencies, see requirements.txt

## Files of interest:

* `cowrie.cfg` - Cowrie's configuration file. Default values can be found in `etc/cowrie.cfg.dist`
* `share/cowrie/fs.pickle` - fake filesystem
* `etc/userdb.txt` - credentials allowed or disallowed to access the honeypot
* `honeyfs/` - file contents for the fake filesystem - feel free to copy a real system here or use `bin/fsctl`
* `honeyfs/etc/issue.net` - pre-login banner
* `honeyfs/etc/motd` - post-login banner
* `var/log/cowrie/cowrie.json` - transaction output in JSON format
* `var/log/cowrie/cowrie.log` - log/debug output
* `var/lib/cowrie/tty/` - session logs, replayable with the `bin/playlog` utility.
* `var/lib/cowrie/downloads/` - files transferred from the attacker to the honeypot are stored here
* `share/cowrie/txtcmds/` - file contents for simple fake commands
* `bin/createfs` - used to create the fake filesystem
* `bin/playlog` - utility to replay session logs

## Is it secure?

Maybe. See [FAQ](https://github.com/cowrie/cowrie/wiki/Frequently-Asked-Questions)

## I have some questions!

Please visit https://cowrie.slack.com/ and join the #questions channel

## Contributors

Many people have contributed to Cowrie over the years. Special thanks to:

* Upi Tamminen (desaster) for all his work developing Kippo on which Cowrie was based
* Dave Germiquet (davegermiquet) for TFTP support, unit tests, new process handling
* Olivier Bilodeau (obilodeau) for Telnet support
* Ivan Korolev (fe7ch) for many improvements over the years.
* Florian Pelgrim (craneworks) for his work on code cleanup and Docker.
* And many many others.

