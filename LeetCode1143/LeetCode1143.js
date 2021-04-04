var longestCommonSubsequence = function(text1, text2) {

    let dp = []
    for(let i=0;i<text1.length+1;i++){
        let d = []
        for(let j =0;j<text2.length+1;j++){
            d[j] = 0
        }
        dp.push(d)
    }
    for(let i = 1;i<text1.length+1;i++){
        for(let j =1;j<text2.length+1;j++){
            if(text1[i-1] === text2[j-1]){
                dp[i][j] = dp[i-1][j-1] + 1
            }else{
                dp[i][j] = Math.max(dp[i-1][j],dp[i][j-1])
            }
        }
    }
    return dp[text1.length][text2.length]
};
let text1 = 'abcde'
let text2 = 'abcdefg'
longestCommonSubsequence(text1,text2)
