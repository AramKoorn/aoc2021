f = open("input.txt", "r")
lines = f.readlines()
lines = [int(x.strip('\n')) for x in lines]

# cnt = 0
# for i in range(1, len(lines)):
#     if lines[i] > lines[i - 1]:
#         cnt += 1

# print(cnt)

sum_3 = []

i = 0
tmp = 0
prev_sum = sum(lines[:3])
print(prev_sum)
cnt = 0
for idx in range(3, len(lines)):
    new_sum = prev_sum - lines[idx - 3] + lines[idx]
    if new_sum > prev_sum:
        cnt += 1

print(cnt)
