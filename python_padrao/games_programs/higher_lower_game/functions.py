import random

# variables

celebs = [
    {'celeb 1 - biggest celeb someware' : 400000000},
    {'celeb 2 - biggest celeb over there' : 400000012300},
    {'celeb 3 - biggest celeb back home' : 40000000220},
    {'celeb 4 - biggest celeb on the try river area' : 400000042100},
    {'celeb 5 - biggest celeb on guton galaxy' : 40000430000123},  
    ]


# random celeb

def random_celeb():
    rand_celeb = random.choice(celebs)

    followers = list(rand_celeb.values())[0]
    celeb = list(rand_celeb.keys())[0]

    return celeb, followers


celeb, followers = random_celeb()

print(f"{celeb} - {followers}")
