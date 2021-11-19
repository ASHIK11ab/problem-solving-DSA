class Solution:

  def __init__(self):
    self.quadruplets = []

  def fourSum(self, nums, target):
    nums.sort()
    if len(nums) < 4:
      return self.quadruplets

    mid = (0 + len(nums)) // 2
    
    while len(nums) >= 1:

      num1 = nums[mid]

      nums = nums[:mid] + nums[mid+1:]
      self.threeSum(nums[:], num1, target)
      
      mid = (0 + len(nums)) // 2

    return self.quadruplets


  def threeSum(self, nums, num1, target):
    if len(nums) < 3:
      return
    
    mid = (0 + len(nums)) // 2
    
    while len(nums) >= 1:

      num2 = nums[mid]

      nums = nums[:mid] + nums[mid+1:]
      self.twoSum(nums[:], num1, num2, target)
      
      mid = (0 + len(nums)) // 2

  
  def twoSum(self, nums, num1, num2, target):
    left = 0
    right = len(nums) - 1
    while left + 1 <= right:
      calculated_sum = num1 + num2 + nums[left] + nums[right]
      if calculated_sum == target:
        self.add_to_result([num1, num2, nums[left], nums[right]])
        left += 1
        right -= 1
      elif calculated_sum < target:
        left += 1
      else:
        right -= 1


  def add_to_result(self, candidate_quadruplet):
    candidate_quadruplet.sort()
    if candidate_quadruplet not in self.quadruplets:
      self.quadruplets.append(candidate_quadruplet)


def main():
  solution = Solution()
  print(solution.fourSum([-3,-2,-1,0,0,1,2,3], 0))


if __name__ == "__main__":
  main()