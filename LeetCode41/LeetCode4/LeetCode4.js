var findMedianSortedArrays = function(nums1, nums2) {
    if(nums1.length === 0){
        nums1 = nums2
    }
    if(nums2.length === 0){
        nums2 = nums1
    }
    let left = {index:0,num:0}
    let allEle = nums1.length + nums2.length
    let right = {index:allEle-1,num:0}
    let left1=0
    let left2 = 0
    let right1 = nums1.length-1
    let right2 = nums2.length-1
    while(left.index <= right.index && left1 < nums1.length && left2 < nums2.length && right1 >= 0 && right2 >= 0){
        if(nums1[left1] < nums2[left2]){
            left.num = nums1[left1]
            left1 ++
        }else{
            left.num = nums2[left2]
            left2 ++
        }
        left.index ++
        if(nums1[right1] < nums2[right2]){
            right.num = nums2[right2]
            right2--
        }else{
            right.num = nums1[right1]
            right1--
        }
        right.index --
    }
    if(left1>=nums1.length || right1<=0){
        if(left1>=nums1.length){
            left.num = nums2[parseInt(allEle/2-nums1.length)]
            right.num = nums2[parseInt(nums2.length - allEle/2) - 1]
        }else{
            left.num = nums2[parseInt(allEle/2)]
            right.num = nums2[parseInt(nums2.length - (allEle/2 - nums1.length)) - 1]
        }
    }
    if(left2>=nums2.length || right2<=0){
        if(left2>=nums2.length){
            left.num = nums1[parseInt(allEle/2-nums2.length)]
            right.num = nums1[parseInt(nums1.length - allEle/2) - 1]
        }else{
            left.num = nums1[parseInt(allEle/2)]
            right.num = nums1[parseInt(nums1.length - (allEle/2 - nums2.length)) - 1]
        }
    }
    return (left.num+right.num)/2
};
let nums1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22], nums2 = [0,6]
console.log(findMedianSortedArrays(nums1,nums2))