# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from decimal import Decimal
from collections import defaultdict

from sql.aggregate import Sum
from sql.operators import Concat

from trytond.model import (
    ModelView, ModelSQL, Model, UnionMixin, DeactivableMixin, fields)
from trytond.model import fields
from trytond.pyson import Eval, Id
from trytond.transaction import Transaction
from trytond.pool import PoolMeta
from trytond.tools import reduce_ids, grouped_slice


__all__ = ['Work', 'Employee']



class Work(metaclass=PoolMeta):
    __name__ = 'project.work'
    assigned = fields.Many2One('company.employee', 'Assigned', required=False)
