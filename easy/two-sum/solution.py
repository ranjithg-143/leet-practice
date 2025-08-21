def find_two_sum(nums, target):
    hashmap = {}

    for idx, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], idx]
        hashmap[num] = idx

    return []


if __name__ == '__main__':
    print(find_two_sum([2, 7, 11, 15], 9))
    print(find_two_sum([3, 2, 4], 6))
    print(find_two_sum([3, 3], 6))
