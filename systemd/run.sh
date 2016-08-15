#!/bin/sh

cd /home/hms_logger/hms_logger/
. ./venv/bin/activate
exec hms_logger
