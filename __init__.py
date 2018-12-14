# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from . import work
from . import company


def register():
    Pool.register(
        work.Work,
        module='project_employee', type_='model',
        depends=['company']
    )
    Pool.register(
        company.Employee,
        module='project_employee', type_='model',
        depends=['company']
    )
