var numRabbits = function(answers) {
  if(answers.length === 0) return 0
  let result = 0
  let map = new Map()
  answers.map(item=>{
    if(map.has(item) && map.get(item)>0){
      map.set(item,map.get(item)-1)
    }else{
      map.set(item,item)
      result += item+1
    }
  })
  return result
};