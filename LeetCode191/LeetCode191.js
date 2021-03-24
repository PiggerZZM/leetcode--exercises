var hammingWeight = function(n) {
    let result = 0
    for(let i = 0;i<32;i++){
      console.log(1<<i)
      if((n&(1<<i)) != 0){
        result ++
      }
  }
  return result
};
let n = 00000000000000000000000000001011
console.log(hammingWeight(n))