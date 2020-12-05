from collections import namedtuple

class tree:
    __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_balanced_tree(tree):
    BalancedStat = collections.namedtuple(
        'BalancedStat', ('balanced', 'height')
    )

    def check_balanced(tree):
        
        # base case
        if tree is None:
            return BalancedStat(True, -1)
        
        # if not balanced then jump out of that node and return false
        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStat(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return Balanced(False, 0)

        height = max(left_result, right_result) + 1
        is_balanced = abs(left_result - right_result) <= 1

        return BalancedStat(is_balanced, height)
    
    return BalancedStat.balanced



    

        