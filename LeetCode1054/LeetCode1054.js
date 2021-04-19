var rearrangeBarcodes = function(barcodes) {
    if(barcodes.length===1) return barcodes
  let codes = new Map()
  let result = []
  barcodes.map(item=>{
    if(codes.has(item)){
      codes.set(item,codes.get(item) + 1)
    }else{
      codes.set(item,1)
    }
  })

  let keys = Array.from(codes.keys()).sort((x,y)=>{
      if(codes.get(x) - codes.get(y)>0){
          return -1
      }else{
          return 1
      }
  })
    let index = 0
    for(let key of keys){
        if(index === result.length) index = 1
        for(let i = 0;i<codes.get(key);i++){
            result.splice(index,0,key)
            index += 2
            if(index > result.length){
                index = 1
            }
        }
    }
    console.log(result)
    return result
};
rearrangeBarcodes([1,1,2])
