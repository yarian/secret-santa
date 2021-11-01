from person import Person

# Sample person file
# The PEOPLE variable is used by the pairing procedure

_a_person = Person(name="Name", email="email_address", gift_preferences="""
I like:
Beer especially Belgians and Sours
Candles that smell like forests and log cabins
Cool looking plants that I won't kill
"Art of" books for games I enjoy playing
""")
_another_person = Person("name", "email")
_a_person.add_relationship(_another_person)

PEOPLE = [
    _a_person,
    _another_person,
]