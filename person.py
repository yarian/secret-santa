class Person:
    def __init__(self, name, email, gift_preferences=None):
        self.name = name
        self.email = email
        self.partner = None
        self.gift_preferences = gift_preferences
    
    def add_relationship(self, person):
        self.partner = person
        person.partner = self
    
    def can_be_santa_of(self, recipient):
        not_gifting_self = recipient.name != self.name
        not_gifting_partner = recipient.name != self.partner
        return not_gifting_self and not_gifting_partner
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, str) and o == self.name:
            return True
        if isinstance(o, Person):
            return o.name == self.name

        return super.__eq__(self, o)
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name