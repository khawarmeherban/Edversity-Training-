# ==================================================
# QUESTION 01: How do aliases behave for mutable lists?
# ==================================================

# SOLUTION:
original = [1, 2, 3]
alias = original
alias.append(4)
print(original)

# QUESTION 02: How can we create a true copy?
# ==================================================

# SOLUTION:
copy_of_list = original.copy()
copy_of_list.append(5)
print(copy_of_list)
print(original)

# Expected output:
# [1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4]
