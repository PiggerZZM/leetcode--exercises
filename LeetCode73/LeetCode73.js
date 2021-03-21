var setZeroes = function(matrix) {
  let rowSet = new Set()
  let colSet = new Set()
  matrix.forEach((element,row) => {
      element.forEach((item,col)=>{
          if(item == 0){
              rowSet.add(row)
              colSet.add(col)
          }
      })
  });
  matrix.forEach((element,row)=>{
      element.forEach((item,col)=>{
          if(rowSet.has(row) || colSet.has(col)){
              element[col] = 0
          }
      })
  })

  return matrix
};

let matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
console.log(setZeroes(matrix));