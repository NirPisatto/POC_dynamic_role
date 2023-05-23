import sys
import math
import random
import time

# set maximum recursion depth
sys.setrecursionlimit(10001)

all_permissions = {
    "1": {"permission": "view_user", "level": "user"},
    "2": {"permission": "view_other_user", "level": "user"},
    "3": {"permission": "create_user", "level": "user"},
    "4": {"permission": "create_other_user", "level": "user"},
    "5": {"permission": "edit_user", "level": "user"},
    "6": {"permission": "edit_other_user", "level": "user"},
    "7": {"permission": "delete_user", "level": "user"},
    "8": {"permission": "delete_other_user", "level": "user"},
}


def user_can(target_sum):
    results = []
    remaining_sum = target_sum

    pattern_entities = []
    laergest_entity = 1
    while laergest_entity <= target_sum:
        pattern_entities.insert(0, laergest_entity)
        laergest_entity *= 2

    for current_entiry in pattern_entities:
        if current_entiry <= remaining_sum:
            results.append(int(math.log2(current_entiry)))
            remaining_sum -= current_entiry

    if remaining_sum > 0:
        return []

    return results


def is_user_can_do(user_permission, action):
    if action in user_can(user_permission):
        return True
    return False


current_role = 0
numbers = list(range(1, 500))
random.shuffle(numbers)
random_numbers = numbers[:300]

for a in random_numbers:
    current_role += 2**a

last_time = time.time()
print("Current role :", current_role)
print("Is user can view_user : ", is_user_can_do(current_role, 1))
print("Exucution time : ", time.time() - last_time)
