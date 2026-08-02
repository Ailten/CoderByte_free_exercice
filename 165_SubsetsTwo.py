
# subsets 2.
# https://leetcode.com/problems/subsets-ii/


def subsetsWithDup(nums: list[int]) -> list[list[int]]:

    class listHashable(list):
        def __hash__(self):
            return tuple(self).__hash__()

    output: set[listHashable] = set()

    for i in range(pow(2, len(nums))):
        grp = listHashable()
        for j in range(len(nums)):
            if i >> j & 1 == 1:
                grp.append(nums[j])
        output.add(grp)

    return list(output)


print(subsetsWithDup([1,2,2])) # [[],[1],[1,2],[1,2,2],[2],[2,2]]

# without set, check if grp is already present in output befor add.