import random

card_ids = [*range(1, 21, 1)]
card_ids.remove(7)
card_ids.remove(13)
card_ids.remove(18)

print(card_ids)

i = 0
while len(card_ids) > 0:
    random_card = random.choice(card_ids)
    print(f'Player {i % 3} gets card {random_card}')
    card_ids.remove(random_card)
    i += 1


character_ids = [*range(1, 4 + 1, 1)]
print(character_ids)
