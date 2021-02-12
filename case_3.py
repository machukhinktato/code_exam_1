import sys


def gen_k_streak(user_pick = '3aabacbebebe'):
    string = ''.join(user_pick[1:])
    k_qty = int(user_pick[0])
    k_streak = ''

    if len(string) < k_qty:
        sys.exit('there is no enough unique characters')

    elif len(string) == k_qty and len(set(string)) == k_qty:
        return string
    
    else:
        for elem in range(len(string)):
            substring = string[elem:]
            if len(set(substring)) == k_qty:
                substring = string[elem:]
                if len(substring) > len(k_streak):
                    k_streak = substring
    
            else:
                while len(set(substring)) > k_qty:

                    substring = substring[:-1]
                    if len(set(substring)) == k_qty and len(substring) > len(k_streak):
                        k_streak = substring

    return k_streak

print(gen_k_streak())
