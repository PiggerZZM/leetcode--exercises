var maxSatisfied = function(customers, grumpy, X) {
    var sum = function(nums){
        return nums.reduce((pre,item)=>{
            if(pre == null){
                return item
            }else{
                return pre+item
            }
        })
    }
    let max = 0
    let left = 0
    let right = 0
    for(let i = 0; i<customers.length-X+1;i++){
        let s = sum(customers.slice(i,i+X))
        if(s > max){
            max = s
            left = i
            right = i+X
        }
    }
    grumpy.forEach((number,index)=>{
        if(number < 1 & !(index >= left && index <= right)){
            max += customers[index]
        }
    })
    return max
};
console.log(maxSatisfied([4,10,10],[1,1,0],2))