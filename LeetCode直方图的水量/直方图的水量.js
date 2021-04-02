var trap = function(height) {
    let result = 0
    var water = function(h,M){
        if(h.length < 2){
            return 0
        }
        let max = Math.max(...h)
        let index = h.findIndex(item=>item === max)
        switch(M){
            case 'left':{
                for(let i = index;i<h.length;i++){
                    result += max-h[i]
                }
                water(h.slice(0,index),'left')
                break
            }
            case 'right':{
                for(let i = 0;i<index;i++){
                    result += max - h[i]
                }
                water(h.slice(index+1,),'right')
                break
            }
        }
    }
    let max = Math.max(...height)
    let index = height.findIndex(item=>item == max)
    water(height.slice(0,index),'left')
    water(height.slice(index+1,),'right')
    return result
};

console.log(trap([8,1,0,2,1,0,1,3,2,1,2,1]))