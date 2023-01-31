import random


#Getting the user id of the anonymous partner looking for
def get_random_anonim_userid(users):
    random_index = random.randint(0, len(users) - 1)
    
    return users[random_index]
