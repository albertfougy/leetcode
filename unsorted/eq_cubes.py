# Print all positive integer solutions to a^3 + b^3 = c^3 + d^3 where a,b,c,d are integers between 1 and 1000

n = 1000
nums = range(1, n + 1)
mapping = {}
for c in nums:
    for d in nums:
        result = c ** 3 + d ** 3
        mapping.setdefault(result, []).append([c, d])

for pairs in mapping.values():
    cross = [(x, y) for x in pairs for y in pairs]
    print(cross)
