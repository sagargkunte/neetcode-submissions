class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        if(s.length==1) return false
        let stack = new Array()
        for(let i=0;i<s.length;i++) {
            if(s.charAt(i)=="(") stack.push(")")
            else if(s.charAt(i)=="{") stack.push("}")
            else if(s.charAt(i)=="[") stack.push("]")
            else {
                if(s.charAt(i)!=stack.pop()) return false;
            }
        }
        return stack.length!=0?false:true
    }
}
