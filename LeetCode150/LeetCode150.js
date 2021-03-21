var evalRPN = function(tokens) {
    let numbers = []
    tokens.forEach(item=>{
        switch(item){
            case '+':{
                numbers.push(numbers.pop() + numbers.pop())
                break
            }
            case "-":{
                numbers.push(0-(numbers.pop() - numbers.pop()))
                break
            }
            case '*':{
                numbers.push(numbers.pop() * numbers.pop())
                break
            }
            case '/':{
                numbers.push(parseInt(1.0/(numbers.pop() / numbers.pop())))
                break
            }
            default:{
                numbers.push(parseInt(item))
            }
        }
    })
    return numbers[0]
};
let tokens = ["4","13","5","/","+"]

console.log(evalRPN(tokens))