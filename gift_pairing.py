import copy
import random

class GiftPairings:
    def __init__(self, people):
        self.gifter_to_recipient = {}
        self._generate_valid_pairing(people)

    def _generate_valid_pairing(self, people):
        pairing = None
        while pairing is None:
            try:
                pairing = self._generate_pairing(people)
            except Exception:
                continue
        self.gifter_to_recipient = pairing
        self.pairings = list(pairing.items())
    
    def _generate_pairing(self, people):
        recipients_left = copy.deepcopy(people)
        gifters = copy.deepcopy(people)
        random.shuffle(gifters) # Important step, otherwise introduces certain biases

        gifter_to_recipient = {}
        for gifter in gifters:
            valid_recipients = [person for person in recipients_left if person.can_be_santa_of(gifter)]
            if len(valid_recipients):
                recipient = random.choice(valid_recipients)
                recipient_idx = recipients_left.index(recipient)
                recipients_left.pop(recipient_idx)
                gifter_to_recipient[gifter] = recipient
            else:
                raise Exception("Cannot generate valid pairing with remaining people.")
        return gifter_to_recipient
    
    def __getitem__(self, x):
        if isinstance(x, int):
            return self.pairings[x]
        
        if isinstance(x, str):
            return self.gifter_to_recipient.get(x)
        
        return None
    
    def __iter__(self):
        return iter(self.pairings)
    
    def __len__(self):
        return len(self.pairings)
