from dataclasses import dataclass

@dataclass
class Currency:
    name: str
    pennies: int
print(Currency(name="pounds", pennies=240))


