class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], lim: int) -> List[int]:
        from collections import deque, defaultdict
        sorted_nums = sorted(nums)
        groups = defaultdict(deque)
        group_map = {}
        curr_group = 0
        groups[curr_group].append(sorted_nums[0])
        group_map[sorted_nums[0]] = curr_group
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - groups[curr_group][-1] <= lim:
                groups[curr_group].append(sorted_nums[i])
            else:
                curr_group += 1
                groups[curr_group].append(sorted_nums[i])
            group_map[sorted_nums[i]] = curr_group
        for i in range(len(nums)):
            grp = group_map[nums[i]]
            nums[i] = groups[grp].popleft()
        return nums
