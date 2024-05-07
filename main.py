import sys
import math
import random
import time
from itertools import combinations

import base64

def number_to_base64(num):
    # Convert integer to byte array
    byte_array = num.to_bytes((num.bit_length() + 7) // 8, 'big') or b'\0'
    
    # Encode byte array to Base64
    base64_encoded = base64.b64encode(byte_array)
    
    # Convert bytes to string
    return base64_encoded.decode()
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

def user_can_optimized(target_sum):
    results = []
    power = 0
    current_entity = 1

    # Create a list of powers of 2 that sum up to target_sum
    while current_entity <= target_sum:
        if current_entity & target_sum:  # Check if the current power of 2 is part of the sum
            results.append(power)
        power += 1
        current_entity <<= 1  # Shift to the next power of two

    return results

    
def is_user_can_do(user_permission, action):
    if action in user_can(user_permission):
        return True
    return False


def generate_powers_of_two_sums(n):
    # Generate the list of powers of two up to 2^n
    powers_of_two = [2 ** i for i in range(n)]

    # This dictionary will store the sum as the key and the list of indices as values
    sums_dict = {}

    # Generate all subsets of the powers_of_two list
    from itertools import combinations
    for r in range(1, len(powers_of_two) + 1):
        for subset in combinations(powers_of_two, r):
            subset_sum = sum(subset)
            # Convert subset from powers of two back to the indices of powers
            subset_indices = [1 << i for i in range(n) if (1 << i) in subset]
            sums_dict[subset_sum] = subset_indices

    return sums_dict

# Example usage:
n = 100
sums_dict = generate_powers_of_two_sums(n)
for key in sorted(sums_dict):
    print(f"{key}: {sums_dict[key]}")

size_in_bytes = sys.getsizeof(sums_dict)

print("Size of dictionary:", size_in_bytes, "bytes")

# To include sizes of all items in the dictionary
total_size = size_in_bytes
# for key, value in sums_dict.items():
#     total_size += sys.getsizeof(key) + sys.getsizeof(value)

print("Total size including keys and values:", total_size, "bytes")

current_role = 0
numbers = list(range(0, n))
random.shuffle(numbers)
random_numbers = numbers[:n]

for a in random_numbers:
    current_role += 2**a


terget = 1

print("Current role :",len(str(current_role))," - ", current_role)
print("     Base 64 :",len(number_to_base64(current_role))," - ", number_to_base64(current_role))
print("Total size of permissions: ", sys.getsizeof(current_role))
last_time = time.time()
permissions = user_can(current_role)
print("Extract [user_can]: ", time.time() - last_time)
print("        [user_can]: ", len(permissions))
last_time = time.time()
permissions = user_can_optimized(current_role)
print("Extract [user_can_opv]: ", time.time() - last_time)
print("        [user_can_opv]: ", len(permissions))
last_time = time.time()
permissions = sums_dict.get(current_role, [])
print("Extract [dict]: ", time.time() - last_time)
print("        [dict]: ", len(permissions))
last_time = time.time()
last_time = time.time()
if 1 in permissions:
        pass
print("User can: ", time.time() - last_time)


# print("Current role :", current_role)
# print("Exstract", )
# print("Is user can view_user : ", is_user_can_do(current_role, 1))
# print("Exucution time : ", time.time() - last_time)
