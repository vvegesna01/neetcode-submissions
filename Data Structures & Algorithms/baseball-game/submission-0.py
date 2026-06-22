class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []
        score = 0

        for op in operations:
            print("score_stack", score_stack)
            if op == "+":
                int1 = score_stack[-1]
                int2 = score_stack[-2]
                score_stack.append(int1+int2)
            
            elif op == "D":
                prev_score = score_stack[-1]
                score_stack.append(prev_score * 2)
            
            elif op == "C":
                score_stack.pop()
            
            else:
                score_stack.append(int(op))
        
        while score_stack:
            score += score_stack.pop()
        
        return score


