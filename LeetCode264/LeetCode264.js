var nthUglyNumber = function(n) {
  let nums = [0,1]
  let p2 = 1,p3 = 1,p5 = 1
  if(n<nums.length){
      return nums[n]
  }
  for(let index = nums.length;index<=n;index++){
      nums[index] = Math.min(nums[p2]*2,nums[p3]*3,nums[p5]*5)
      if(nums[p2] * 2===nums[index]) {
              p2++
      }
      if(nums[p3] * 3===nums[index]) {
              p3++
      }
      if(nums[p5] * 5===nums[index]) {
              p5++
      }
  }
  return nums.pop()
};

console.log(nthUglyNumber(10))