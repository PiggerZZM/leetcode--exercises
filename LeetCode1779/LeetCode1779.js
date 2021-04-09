var nearestValidPoint = function(x, y, points) {
  let result = -1
  let distence = 10000
  points.map((item,index)=>{
    if(item[0] == x || item[1] == y){
      let d = Math.abs(item[0] - x) + Math.abs(item[1] - y)
      if(d < distence){
        result = index
        distence = d
      }
    }
  })
  return result
};

console.log(nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]))