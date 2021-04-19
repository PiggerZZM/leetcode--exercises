var removeElement = function(nums, val) {
  let i = 0
    while(i<nums.length){
      if(nums[i] === val) {
          nums.splice(i, 1)
      }else{
          i++
      }
    }
    console.log(nums)
  return nums.length
};

removeElement([3,2,2,3,3,4,5,6,7,8,9],3)