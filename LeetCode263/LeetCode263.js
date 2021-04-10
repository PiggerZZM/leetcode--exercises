var isUgly = function(n) {
  if(n<=0) return false
  while(n>0){
    if(n%2===0){
      n = Math.floor(n/2)
      continue
    }else if(n%3===0){
      n = Math.floor(n/3)
      continue
    }else if(n%5===0){
      n = Math.floor(n/5)
      continue
    }else if(n===1){
      return true
    }else{
      return false
    }
  }
  return true
};