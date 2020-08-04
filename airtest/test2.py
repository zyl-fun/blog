# -*- encoding=utf8 -*-
__author__ = "xingdao_1"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://7/",
    ])


# script contenttouch(Template(r"tpl1596187345003.png", record_pos=(0.356, -0.499), resolution=(1080, 1920)))

print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)