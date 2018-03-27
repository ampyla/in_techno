from __future__ import absolute_import
import rules

#from .predicates import *


##@rules.predicate
#def is_company_guest(user,company):
#    return user in company.managers.all()

@rules.predicate
def is_authenticated(user):
    return user.is_authenticated()
@rules.predicate
def is_editors_group(user):
    return user.groups.filter(name='CompanyEditors').exists()

can_change_entry= rules.has_perm('company.views_entry')

is_editors = rules.is_group_member('CompanyEditors')
is_guest = rules.is_group_member('CompanyGuest')

#rules.add_perm('Company', is_editors)
rules.add_perm('company', rules.is_authenticated)
rules.add_perm('company.views_entry',  is_editors_group)



#rules.add_perm('Company.change_Company12', is_company_manager) # | is_superuser
