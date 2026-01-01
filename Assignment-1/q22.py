result = 10 + 2 ** 3 * 4 // 5 - 3
# result = 10 + 8  * 4 // 5 - 3
# result = 10 + 8  * 0  - 3
# result = 10 + 0 - 3
# result = 7
print(result)

# I got wrong :(

########  Answered by LLM #######

# Step-by-step breakdown:

# Exponentiation first: 2 ** 3
#   2³ = 8
# Expression becomes: 10 + 8 * 4 // 5 - 3

#### Multiplication and floor division next (left to right):
#   First: 8 * 4 = 32
# Expression becomes: 10 + 32 // 5 - 3
#   Next: 32 // 5 (floor division → integer division, rounds down)
#   32 ÷ 5 = 6.4 → floor to 6
# Expression becomes: 10 + 6 - 3

#### Addition and subtraction (left to right):
#   First: 10 + 6 = 16
#   Then: 16 - 3 = 13


