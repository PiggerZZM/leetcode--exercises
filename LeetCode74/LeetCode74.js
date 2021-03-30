var searchMatrix = function(matrix, target) {
  let index = 0
  for(let i = matrix.length-1;i>=0;i--){
    if(matrix[i][0]<=target){
      index = i
      break
    }
  }
  for(let i = 0;i<matrix[index].length;i++)
  {
    if(matrix[index][i] == target){
      return true
    }
  }
  return false
};