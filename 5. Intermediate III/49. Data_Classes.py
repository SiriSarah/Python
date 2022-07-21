from dataclasses import dataclass
from typing import Any

# Data classes, are used to store the data in Python
# It is mandatory to define the type of the attributes in the data class
# Hint: If you don't know the data type you can use "Any"
# Default values can be provided as well.

@dataclass
class Company:
    revenue: Any
    # Attributes with default values need to be declared after declaring the ones without default value.
    name: str = "SiriSarah LLC"
    zipcode: int = 84054
    
c = Company(0)
print(c.name)
print(c.zipcode)
print(c.revenue)

# In python, decorators are defined by "@" symbol. Data class is one among them.
# To do: Create functions, and more companies to play around with this code.

