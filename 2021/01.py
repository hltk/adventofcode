from aocd import data

*nums, = map(int, data.split("\n"))

print(sum(a < b for a, b in zip(nums, nums[1:])))
print(sum(a < b for a, b in zip(nums, nums[3:])))
