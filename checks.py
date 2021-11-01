from collections import Counter, defaultdict
from email.policy import default
from gift_pairing import GiftPairings
from tabulate import tabulate
from person import Person

a = Person("a", "")
b = Person("b", "")
c = Person("c", "")
d = Person("d", "")
e = Person("e", "")
f = Person("f", "")
g = Person("g", "")
a.add_relationship(b)
c.add_relationship(d)
people = [a, b, d, c, e, f, g]


def check_randomness(verbose=True):
    a_recipients_count = Counter()
    gifts_from_x_to_y = defaultdict(lambda:defaultdict(int))
    for p1 in people:
        for p2 in people:
            gifts_from_x_to_y[p1][p2] = 0
    for i in range(1000):
        pairing = GiftPairings(people)
        as_recipient = pairing["a"]
        a_recipients_count.update([as_recipient])

        name_pairings = [(p[0].name, p[1].name) for p in pairing]
        for p in name_pairings:
            gifts_from_x_to_y[p[0]][p[1]] += 1
    
    table = []
    for p1 in people:
        row = [p1]
        for p2 in people:
            row.append(gifts_from_x_to_y[p1.name][p2.name])
        table.append(row)
    names = [p.name for p in people]
    names.insert(0, "")
    print("Times that gifter (on left) was paired with recipient (on top).")
    print(tabulate(table, headers=names))
    return a_recipients_count.most_common()[0][0]

def check_for_favorred():
    print(f"""
Running 100 experiments.

In each experiment we generate 1,000 gifter/recipient pairings.
We then count how often each person appeared as a's gift recipient. 
In theory each person should come out roughly the same number of times except for b who should never appear because they're in a relationship.

After running the experiment each time, we keep track of who was the most frequently returned recipient.
After 100 runs, we should see a mix of people getting chosen most often.
""")
    favorred_count = Counter()
    for i in range(100):
        print(f"Running experiment {i}.", end='\r')
        favorred_count.update([check_randomness(verbose=True)])
    print(favorred_count)

check_randomness()