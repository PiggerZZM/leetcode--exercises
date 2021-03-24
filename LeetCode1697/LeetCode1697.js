var distanceLimitedPathsExist = function(n, edgeList, queries) {
  let m = new Map()
  let result = []
  edgeList.map(item=>{
    let [first,second,val] = item
    if(first > second){
      [first,second] = [second,first]
    }
    let fs = first.toString() + second.toString()
    if(m.has(fs)){
      if(val < m.get(fs)){
        m[fs] = val
      }
    }else{
      m.set(fs,val)
    }
  })
  console.log(m)
  queries.map(item=>{
    let [first,second,val] = item
    if(first > second){
      [first,second] = [second,first]
    }
    let fs = first.toString() + second.toString()
    if(m.has(fs)){
      if(m.get(fs) >= val){
        result.push(false)
      }else{
        result.push(true)
      }
    }
  })
  return result
};


