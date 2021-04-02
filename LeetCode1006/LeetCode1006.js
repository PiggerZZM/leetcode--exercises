var clumsy = function(N) {
    let list = []
    for(let index = 0;N>0;index++){
      switch(index%4){
        case 0:{
          list.push(N)
          break;
        }
        case 1:{
          let m = list.pop()
          list.push(m*N)
          break
        }
        case 2:{
          let m = list.pop()
          list.push(Math.floor(m/N))
            break
        }
        case 3:{
          let m = list.pop()
          if(index <= 3){
              list.push(N+m)
          }else{
              list.push(m-N)
          }
            break
        }
      }
      N = N -1
  }
  return list.reduce((pre,next)=>{
    return pre-next
  })
}

console.log(clumsy(4))