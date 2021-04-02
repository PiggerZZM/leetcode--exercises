var subsetsWithDup = function(nums) {
    let result = []
    let numbers = new Set()
    nums = nums.sort()
    for(let i = 0;i< 2**nums.length;i++) {
        let re = []
        let is = i.toString(2).padStart(nums.length, '0').split("").reverse()
        is.map((it,index,all)=>{
            if(index >0){
                if(nums[index] != nums[index-1]){
                    re.push(nums[index])
                }
            }else{
                re.push(nums[index])
            }
        })
        result.push(re)
    }

    return result
};
nums = [1,2,3,3]
subsetsWithDup(nums)