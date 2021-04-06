var removeDuplicates = function(nums) {
  if(nums.length <= 2){
    return nums.length
  }
  let number = 100000
  let count = 0
  for(let index = 0;index<nums.length;){
    if(number == nums[index]){
      if(count < 2){
        count++
        index++
      }else{
        nums.splice(index,1)
      }
    }else{
      number = nums[index]
      count = 1
      index++
    }
  }
  return nums.length
};

console.log(removeDuplicates([1,1,1,2,2,3,3,3]))