/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var canBeEqual = function(s1, s2) {
    for (let i=0; i<4;i++){
        if (s1[i]!=s2[i]){
            if (i+2<4 && s1[i]===s2[i+2]);
            else if (i-2>=0 && s1[i]===s2[i-2]);
            else return false;
        }
    }
    return true;
};