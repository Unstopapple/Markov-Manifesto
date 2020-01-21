import random
thing = {}

thing['noodle'] = [1, 2, 3]
thing['tree'] = [3, 8, 6]
thing['tree'].append(7)

for obj in thing:
    print(thing[random.choice(list(thing))])
