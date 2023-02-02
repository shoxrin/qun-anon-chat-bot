import random


#Getting the user id of the anonymous partner looking for
def get_random_anonim_userid(anonim_user_id, user_id):
    anonim_user_id.remove(user_id)
    random_index = random.randint(0, len(anonim_user_id) - 1)
    
    return anonim_user_id[random_index]

def get_random_group_id(groups_id):
    group_id = random.randint(0, len(groups_id) - 1)
    
    return group_id
