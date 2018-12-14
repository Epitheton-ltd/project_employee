"""
 File name: company.py
 Date:      2018/12/14 11:29
 Author:    mzimen@epitheton.com
"""

from trytond.model import fields
from trytond.pool import Pool, PoolMeta

class Employee(metaclass=PoolMeta):
    __name__ = 'company.employee'
    projects = fields.One2Many('project.work', 'assigned', 'Projects', required=False)

# :vim set sw=4 ts=4 fileencoding=utf-8 expandtab:
