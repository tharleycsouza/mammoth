#!/bin/sh
/lib/systemd/systemd-sysv-install enable ssh
/usr/sbin/sshd -ddd