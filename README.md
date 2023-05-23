# Proof Of Concept Dynamic Roles and Permissions Database Less

## Introduction

Database query time can be a bottleneck in application performance. Static roles and permissions can lead to users being granted permissions they don't need, which can increase the number of database queries.

This proof of concept will demonstrate how dynamic roles and permissions can be used to reduce database query time and significantly simplify the control actions buttons in the front-end.

## Key Concept

I suppose using the addition of 2^n sequence to provide the permissions which users have. This means we are able to get a list of permissions from a single line of numbers.

Assume that we have list persmins as I showing below:

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

**In the traditional way** we have to bind a relationship role with any of the permissions above and query every request time and UI displaying.

If we have a role named general_user which can only view what we have to store, general_user has permission id 1 and general_user has permission id 2 in the database, and we have to query this and verify every time.

**For the new approach** we store only the sum of permission id 1 and permission id 2 (it must be 3) which belong to the general_user role in db. In the verify stage we only use the verify function which reverses the process of sum in order to define permission id 1 and 2.

Example:

Role A have permission [1,4,16,64] => sum of role A = 85

From 85 we are able to get [1,4,16,64] based on an algorithm in github.

The key is we are able to get specific numbers (2^?) from the sum of 2^x. We are able to verify permission without a database with a sample of function if we map our permission id to our route and ui hide/how.

## Logical proof using mathematical reasoning

To prove that the sum of any numbers in the sequence 2^n, where x is a whole number, is not equal to any number in the sequence that has not yet been included in the sum, we can use a proof by contradiction.

Assume that there exists a sum of numbers in the sequence that is equal to a number in the sequence that has not been included in the sum. Let's represent the numbers in the sequence as a1, a2, a3, ..., an, where n is the total number of numbers in the sequence.

According to our assumption, there exists a sum of numbers, let's say ai1 + ai2 + ai3 + ... + aim, that is equal to a number in the sequence, aj, where j > m and j ≤ n.

Now, let's consider the sum of all the numbers in the sequence, which can be represented as:

a1 + a2 + a3 + ... + an

Since the sequence is in ascending order, each subsequent number is greater than the sum of all the previous numbers. Therefore, we have:

a1 &lt; a1 + a2

a1 + a2 &lt; a1 + a2 + a3

a1 + a2 + a3 &lt; a1 + a2 + a3 + a4

...

a1 + a2 + a3 + ... + an-1 &lt; a1 + a2 + a3 + ... + an

Thus, we can conclude that the sum of any subset of numbers from the sequence is strictly less than the sum of all the numbers in the sequence.

However, in our assumption, we stated that there exists a subset sum equal to a number in the sequence that has not been included in the sum. This contradicts the fact that the subset sum is always strictly less than the sum of all the numbers in the sequence.

Therefore, we have proven that the sum of any numbers in the sequence 2^n, where x is a whole number, is not equal to any number in the sequence that has not yet been included in the sum.
