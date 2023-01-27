from pprint import pprint
from .models import Company, Dimension

from django.db import connection
from django.db.models import Q
from functools import reduce

def list_children(dimension_id):
    """Lists the nested tree for a given Dimension.
    """
    tree = []
    level = -1
    dimension = Dimension.objects.get(id=dimension_id)

    tree = dimension.get_all_children(level)
    tree.extend(tree)
    return list(dict.fromkeys(tree))

def list_hierarchy(company_id):
    """Lists the complete nested hierarchy for a company.
    """
    company = Company.objects.get(id=company_id)
    company_tree = []

    dimensions = Dimension.objects.filter(company=company, parent=None)
    level = -1

    for dimension in dimensions:
        if dimension.has_children:
            tree = dimension.get_all_children(level)
            company_tree.extend(tree)

    return company_tree
