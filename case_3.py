user_pick = '3aabacbebebe'
letters_limit = int(user_pick[0])
user_pick = ''.join(user_pick[1:])
test = []


def generate_longest():
    S = user_pick
    k = letters_limit

    # We can take len() of empty string
    longest = ''

    # Case 1: fewer characters in S than k, impossible
    if len(S) < k:
        return longest

    # Case 2: if the substring is == k, AND it has k unique, only option
    elif len(S) == k and len(set(S)) == k:
        return S

    # Case 3: we can check substrings
    for s1 in range(len(S)):
        substring = S[s1:]

        # Exactly k! This could be a solution
        if len(set(substring)) == k:

            substring = S[s1:]
            if len(substring) > len(longest):
                longest = substring

        # Greater than k, could be? But we need to trim
        else:
            while len(set(substring)) > k:

                # Remove last element, try again
                substring = substring[:-1]  # remove last element
                if len(set(substring)) == k and len(substring) > len(longest):
                    longest = substring

    # If we still have empty for longest, return -1 as desired
    if longest == '':
        longest = -1

    return longest

print(generate_longest())

# test = ''.join(user_pick[0:letters_limit])
# test = []
# while len(set(test)) <= letters_limit and len(test) <= len(user_pick):
#     for i in range(len(user_pick)):
#         test.append(user_pick[i])

# for i in test:
#     if i in test[test.index(i):test.index(i) + letters_limit]:
#         continue
#     else:
#         test.remove(i)


# for i in user_pick:
#     test.append(i) if i + 1
#     print(i)
# for i in user_pick:
#
#     print(ord(i))
print(test)
print(user_pick)
