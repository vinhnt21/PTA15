"""
Input:
nums là 1 list chứa các số nguyên dương
target là 1 số nguyên dương

Output:
1 list chứa 2 phần tử và vị trí của 2 phần tử trong 
nums mà tổng của chúng bằng target

Ví dụ:
nums = [2, 7, 11, 15]
target = 9

Output: [0,1]
"""

nums = [2, 7, 11, 15]
target = 26


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


print(two_sum(nums, target))

# test_cases = [
#     {"nums": [1, 5, 3, 8], "target": 9},  # Kỳ vọng [1, 2]
#     {"nums": [3, 2, 4], "target": 6},  # Kỳ vọng [1, 2]
#     {"nums": [10, 2, 7, 8], "target": 15},  # Kỳ vọng [2, 3]
#     {"nums": [1, 3, 5, 7, 9], "target": 12},  # Kỳ vọng [1, 4]
#     {"nums": [4, 6, 1, 9, 7, 10], "target": 16},  # Kỳ vọng [1, 5]
# ]

# # Vòng for để in ra kết quả cho từng test case
# for i, case in enumerate(test_cases, 1):
#     nums = case["nums"]
#     target = case["target"]
#     result = two_sum(nums, target)
#     print(f"Test case {i}: nums = {nums}, target = {target}, Output = {result}")
