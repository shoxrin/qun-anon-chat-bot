import random


#Getting the user id of the anonymous partner looking for
def get_random_anonim_userid(anonim_user_id, user_id):          
    try:
        random_index = random.randint(0, len(anonim_user_id) - 1)
        if user_id != anonim_user_id[random_index]:
            return [anonim_user_id[random_index], True]
        else:
            return [0, False]
        
    except Exception:
        return [0, False]

def get_random_group_id(groups_id):
    group_id = random.randint(0, len(groups_id) - 1)
    
    return group_id
