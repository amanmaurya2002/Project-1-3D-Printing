from give_print.models import Material, Supplier

# Contains custom made utilities used by project.

def find_suppliers(specification):
    suppliers = specification.material.with_suppliers.all()
    return suppliers