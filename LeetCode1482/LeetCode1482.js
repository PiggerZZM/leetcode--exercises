var minDays = function(bloomDay, m, k) {
  if(bloomDay.length < m*k){
    return -1
  }
  const canMake = function(day){

  }
  let minDay = Math.min(...bloomDay)
  let maxDay = Math.max(...bloomDay)
  let result = maxDay
  while(minDay < maxDay){
      let mid = Math.floor((minDay + maxDay)/2)
      let i = canMake(mid)
      if(i === 0){
          if(result > mid){
              result = mid
          }
      }else if(i<0){
          minDay = mid + 1
      }else{
          maxDay = mid - 1
      }
  }
  return result
};