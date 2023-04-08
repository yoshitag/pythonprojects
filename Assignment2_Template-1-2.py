#Notice: do not change the function names

# Takes an integer and determines if even numbers are on left side and odd numbers on right side
# Input: Integer x | Output: boolean
# e.g. x = 14356 , (even_on_left = True) | False (1 is left of 4)
# e.g. x = 246193 , (even_on_left = True) | True 
# e.g. x = 2419735 , even_on_left = False | False (even needs to be on the right)
# e.g. x = 5379142 , even_on_left = False | True 
def is_evenodd_split(x, even_on_left=True):
    digits = [int(d) for d in str(x)]
    n = len(digits)
    if even_on_left:
        # check if all even numbers are on the left side and all odd numbers are on the right side
        left, right = [], []
        for i, d in enumerate(digits):
            if d % 2 == 0:
                left.append(d)
            else:
                right = digits[i:]
                break
        return len(left) + len(right) == n and all(d % 2 == 0 for d in left) and all(d % 2 != 0 for d in right)
    else:
        # check if all odd numbers are on the left side and all even numbers are on the right side
        left, right = [], []
        for i, d in enumerate(digits):
            if d % 2 != 0:
                left.append(d)
            else:
                right = digits[i:]
                break
        return len(left) + len(right) == n and all(d % 2 != 0 for d in left) and all(d % 2 == 0 for d in right)

    pass

# Takes two strings and determines which has most repeated letter. Return "Neither" if both has same amount
# Input: String s, String t | Output: String
# e.g. s = "noob", t = "tattered" | String t ('t' repeated more than 'o')
# e.g. s = "stands", t = "stand" | String s ('s' is repeated more)
# e.g. s = "book", t = "steve" | String "Neither" ('o' is repeated same amount as 'e')
def count_repeated_letters(string):
    counts = {}
    for letter in string:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    max_count = max(counts.values())
    return max_count if max_count > 1 else 0
        
def get_more_repeated(s, t):
    str1_count = count_repeated_letters(s)
    str2_count = count_repeated_letters(t)

    if str1_count > str2_count:
        return s
    elif str2_count > str1_count:
        return t
    else:
        return "Neither"
    pass

# Takes two strings and determines if t is after s in alphabetical order. Assume strings are not the same.
# and longer words come after shorter words when otherwise identical
# Input: String s, String t | Output: boolean
# e.g. s = "head", t = "headway" | True (longer word and identical otherwise)
# e.g. s = "think", t = "thought" | True ("thought" is after "think" since 'o' is after 'i')
# e.g. s = "zebra", t = "alpha" | False ('a' is before 'z')
def is_alphabetical(s, t):
    for i in range(min(len(s), len(t))):
        if s[i] > t[i]:
            return False
        elif s[i] < t[i]:
            return True
    return len(s) <= len(t)

    pass

# Takes a string and returns a list of longest words in the string. Assume longest words are unique.
# Input: String s | Output: List of Strings
# e.g. "I came home from school and went straight to bed." | ['straight']
# e.g. "I read a long book. It was very good." | ['read', 'long', 'book', 'very', 'good'] 
#		(Note: Longest word is 4 characters but there are multiple)
import re
def get_longest_word(s):
    words = re.findall(r'\w+',s)
    max_length = max(len(word) for word in words)
    longest_words = tuple(word for word in words if len(word)==max_length)
    return longest_words
    
    pass

if __name__=="__main__":
    
    # Test Question 1
    # ====================
    print("\nQuestion 1")
    print("===========")
    q1_test1 = 14356
    q1_test2 = 246193
    q1_test3 = 2419735
    q1_test4 = 5379142
    q1_answer1 = is_evenodd_split(q1_test1)
    q1_answer2 = is_evenodd_split(q1_test2)
    q1_answer3 = is_evenodd_split(q1_test3, even_on_left=False)
    q1_answer4 = is_evenodd_split(q1_test4, even_on_left=False)
    print("> Your answer: \t" + str(q1_answer1))
    print("Right Answer: \tFalse")
    print("> Your answer: \t" + str(q1_answer2))
    print("Right Answer: \tTrue")
    print("> Your answer: \t" + str(q1_answer3))
    print("Right Answer: \tFalse")
    print("> Your answer: \t" + str(q1_answer4))
    print("Right Answer: \tTrue")

    # Test Question 2
    # ====================
    print("\nQuestion 2")
    print("===========")
    q2_test1_s = "noob"
    q2_test1_t = "tattered"
    q2_test2_s = "stands"
    q2_test2_t = "stand"
    q2_test3_s = "book"
    q2_test3_t = "steve"
    q2_answer1 = get_more_repeated(q2_test1_s, q2_test1_t)
    q2_answer2 = get_more_repeated(q2_test2_s, q2_test2_t)
    q2_answer3 = get_more_repeated(q2_test3_s, q2_test3_t)
    print("> Your answer: \t" + str(q2_answer1))
    print("Right Answer: \ttattered")
    print("> Your answer: \t" + str(q2_answer2))
    print("Right Answer: \tstands")
    print("> Your answer: \t" + str(q2_answer3))
    print("Right Answer: \tNeither")

    # Test Question 3
    # ====================
    print("\nQuestion 3")
    print("===========")
    q3_test1_s = "head"
    q3_test1_t = "headway"
    q3_test2_s = "think"
    q3_test2_t = "thought"
    q3_test3_s = "zebra"
    q3_test3_t = "animal"
    q3_answer1 = is_alphabetical(q3_test1_s, q3_test1_t)
    q3_answer2 = is_alphabetical(q3_test2_s, q3_test2_t)
    q3_answer3 = is_alphabetical(q3_test3_s, q3_test3_t)
    print("> Your answer: \t" + str(q3_answer1))
    print("Right Answer: \tTrue")
    print("> Your answer: \t" + str(q3_answer2))
    print("Right Answer: \tTrue")
    print("> Your answer: \t" + str(q3_answer3))
    print("Right Answer: \tFalse")

    # Test Question 4
    # ====================
    print("\nQuestion 3")
    print("===========")
    q4_test1 = "I came home from school and went straight to bed."
    q4_test2 = "I read a long book. It was very good."
    q4_answer1 = get_longest_word(q4_test1)
    q4_answer2 = get_longest_word(q4_test2)
    print("> Your answer: \t" + str(q4_answer1))
    print("Right Answer: \t['straight']")
    print("> Your answer: \t" + str(q4_answer2))
    print("Right Answer: \t['read', 'long', 'book', 'very', 'good']")

