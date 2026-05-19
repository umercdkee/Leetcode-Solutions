/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    const m = s.length;
    const dp = Array.from({length: m + 1}, () => Array(m+1).fill(0));
    let s2 = s.split('').reverse().join('');
    let maxLength = 0;
    let endIndex = 0;
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= m; j++) {
            if (s[i - 1] === s2[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
                if (i - dp[i][j] === m - j) {
                    if (dp[i][j] > maxLength) {
                        maxLength = dp[i][j];
                        endIndex = i;
                    }
                }
            }else {
                dp[i][j] = 0;
            }
        }
    }
    return s.substring(endIndex - maxLength, endIndex);
    
};