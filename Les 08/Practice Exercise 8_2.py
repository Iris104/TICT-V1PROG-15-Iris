import random
def monopolyworp():
    nummer1 = random.randrange(1, 11)
    nummer2 = random.randrange(1, 11)
    som = nummer1 + nummer2
    print('{} + {} = {}'.format(nummer1, nummer2, som))
    dubbel = nummer1 == nummer2
    while dubbel:
        print('{} + {} = {} (dubbel)'.format(nummer1, nummer2, som))
        if dubbel*2:
           print('{} + {} = {} (direct naar gevangenis)'.format(nummer1, nummer2, som))
           break

print(monopolyworp())