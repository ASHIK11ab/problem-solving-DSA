# Sorting

This branch contains problems on sorting.

| Problems Index |
| --- |
| 1. [4Sum](#problem-title:-4sum) |

### Problem Title: 4SUM

#### Problem statement
```
- Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums-[d] == target
- You may return the answer in any order.
```

#### Sample Input and Output
```
  Input: nums = [1,0,-1,0,-2,2], target = 0
  Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

  Input: nums = [2,2,2,2,2], target = 8
  Output: [[2,2,2,2]]
```

#### Objective
- The objective of the problem is to find the list of all
quadruplets whose sum makes up to a given target.

#### Approach to the solution
1. Sort the given list in non decreasing order.
1. First pick a number from the sorted list (we pick the middle element)
and the remaining three numbers from the remaining list.
1. For finding the second number repeat the same process as in the previous
 step (pick a second element) and find the remaining two numbers.
1. Keep two pointers pointing the lefmost and righmost element in the list.
1. If the sum of the four numbers is equal to the target:
  1. Then, add the four numbers to our result and move left pointer to point to
      next element and move right pointer to point to its before element.
      > 1. The reason to move left pointer by 1 and decrement the right pointer by
        1 is because if we only move one pointer (say we move only the left 
        pointer by 1).
      > 1. All the elements in the remaining list will either be greater or equal
        to the element which left pointer pointed before.
      >  1. So, the sum of the resulting four elements selected later on will be either greater or equal to
        the target.
      >  1. Same is the case when we move only the right pointer to point to its before
        element, in that case the sum of the four elements will either be lesser or
        equal to the target.
  1. If the sum is lesser than the target move the left pointer to point to next
      element in the list.
  1. If the sum is greater than the target move the right pointer to point to the
      before element in the list.

#### Solution implementation
- The implementation to the solution can be found [here.](https://github.com/ASHIK11ab/problem-solving-DSA/tree/sorting/4sum.py)

#### LeetCode stats
  <p>
    <img src="https://img.shields.io/static/v1?label=Status&message=Accepted&color=success">
  </p>
  <p>
    <img src="https://img.shields.io/static/v1?label=Runtime&message=1880 ms&color=blue"></p>
  <p>
    <img src="https://img.shields.io/static/v1?label=Memory&message=14.5 MB&color=blueviolet">
  </p>

## Creator & Maintainer:
<a href="https://github.com/ASHIK11ab">
  <img style="border-radius: 50px" src="https://avatars2.githubusercontent.com/u/58099865?s=460&u=dc835e2281a9265edf2b48059f1c8151be89a1b1&v=4" width="70px" height = "70px"> 
</a> 

[Ashik Meeran Mohideen](https://github.com/ASHIK11ab)

&copy; copyrights 2021. All rights reserved.

Licensed under [MIT LICENSE](https://github.com/ASHIK11ab/problem-solving-DSA/blob/main/LICENSE)