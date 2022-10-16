class Question1:
    def rotateArray(self, nums, k):

        k = k % len(nums)
        nums = self.reverse(nums, 0, len(nums)-1)
        nums = self.reverse(nums, 0, k-1)
        nums = self.reverse(nums, k, len(nums)-1)

        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums

print(Question1().rotateArray([1,2,3,4,5,6,7,8,9,10], 2))
print(Question1().rotateArray([1,2,3,4,5,6,7,8,9,10], 15))
print(Question1().rotateArray([1,2,3,4,5,6,7,8,9,10], 1))
print(Question1().rotateArray([1,2,3,4,5,6,7,8,9,10], 100))