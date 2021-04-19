var removeDuplicates = function(nums) {
  let i = 1
  while(i<nums.length){
    if(nums[i] > nums[i-1]){
      i++
    }else{
      nums.splice(i,1)
    }
  }
};
removeDuplicates([1,1,2,3,4,4,5,5,5,5,5,6,6,7,8,9])