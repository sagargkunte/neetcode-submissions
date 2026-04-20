class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let stack = new Array()

        for(let i=0;i<tokens.length;i++) {
            if(tokens[i] == "+") {
                let num2 = Number(stack.pop())
                let num1 = Number(stack.pop())
                stack.push(num1+num2)
            } else if(tokens[i] == "-") {
                let num2 = Number(stack.pop())
                let num1 = Number(stack.pop())
                stack.push(num1-num2)
            } else if(tokens[i] == "*") {
                let num2 = Number(stack.pop())
                 let num1 = Number(stack.pop())
                stack.push(num1*num2)
            } else if(tokens[i] == "/") {
                let num2 = Number(stack.pop())
                let num1 = Number(stack.pop())
                stack.push(Math.trunc(num1/num2))
            } else {
                stack.push(Number(tokens[i]))
            }
        }
        return stack[0]
    }
}
