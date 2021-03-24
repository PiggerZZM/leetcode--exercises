var removePalindromeSub = function(s) {
  if(s.length == 0){
    return 0
  }
  let set = new Set(s.split(""))
  if(set.size == 1){
    return 1
  }else{
    if(s == s.split("").reverse().join("")){
      return 1
    }else{
      return 2
    }
  }
  };
console.log(removePalindromeSub('abb'))