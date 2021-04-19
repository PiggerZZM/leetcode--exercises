var containsNearbyAlmostDuplicate = function(nums, k, t) {
  for(let index = 0;index < nums.length;index++){
    for(let i = index+1;i<=index+k && i < nums.length;i++){
      if(Math.abs(nums[i] - nums[index]) <= t){
        return true
      }
    }
  }
  return false
};

containsNearbyAlmostDuplicate([2147483646,2147483647],3,3)