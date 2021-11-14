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
    if len(nums) < 2:
      return
    
    mid = (0 + len(nums)) // 2
    
    while len(nums) >= 1:

      num3 = nums[mid]

      nums = nums[:mid] + nums[mid+1:]
      self.oneSum(nums[:], num1, num2, num3, target)
      
      mid = (0 + len(nums)) // 2

    
  def oneSum(self, nums, num1, num2, num3, target):
    if len(nums) < 1:
      return
    
    mid = (0 + len(nums)) // 2
    
    while len(nums) >= 1:

      num4 = nums[mid]

      if num1 + num2 + num3 + num4 == target:
        candidate_quadruplet = list([num1, num2, num3, num4])
        candidate_quadruplet.sort()
        if candidate_quadruplet not in self.quadruplets:
          self.quadruplets.append(candidate_quadruplet)
      elif num1 + num2 + num3 + num4 < target:
        nums = nums[mid+1:]
      else:
        nums = nums[:mid]
        
      nums = nums[:mid] + nums[mid+1:]
      
      mid = (0 + len(nums)) // 2


def main():
  solution = Solution()
  print(solution.fourSum([-3,-2,-1,0,0,1,2,3], 0))


if __name__ == "__main__":
  main()