var maxCount = function(m, n, ops) {
  let i = 140001
  let j = 140001
  ops.map(item=>{
    let x = item[0]
    let y = item[1]
    if(x < i){
      i = x
    }
    if(y < j){
      j = y
    }
  })
  return ops.length === 0?n*m:i*j
};