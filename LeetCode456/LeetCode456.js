var find132pattern = function(nums) {
    let min = []
    let stack = []
    for(let i = 0;i<nums.length;i++){
        min.push(Math.min(...nums.slice(0,i+1)))
    }
    for(let i = nums.length - 1;i>=0;i--){
        if(nums[i] > min[i]){
            stack.push(nums[i])
            stack = stack.filter(item=>{
                return item > min[i]
            })
            if(nums[i] > Math.min(...stack)){
                return true
            }
        }

    }
    return false
};
let nums = [3,1,2]
console.log(find132pattern(nums))