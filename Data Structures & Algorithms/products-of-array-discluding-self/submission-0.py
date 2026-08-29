class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create prefix array
        pre = 1
        prefix = []
        for n in nums:
            pre *= n
            prefix.append(pre)

        # create postfix array
        post = 1
        postfix = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            post *= nums[i]
            postfix[i] = post

        # create output array
        # for output i, prefix[i-1] * postfix[i+1]
        out = 1
        output = []
        output.append(1*postfix[1]) # first
        for i in range(1, len(nums)-1):
            out = prefix[i-1] * postfix[i+1]
            output.append(out)
        # last
        output.append(1*prefix[len(nums)-2])
        return output