#We need a valid sudoku board. 
#Only have to check for values that are within in the board, blank spaces don't count for anythign
#Since we are trying to avoid duplicates in very particular situations, my way of thinking about this problem is to have a hashmap represeting the row values, column values, and square values. How we can do this is the keys will represent either the row, column or square, and then the value will be the values within that column. We can check in every iteration through the board and check to see if these values are already in the hashmaps and if so return false. If we pass through it all return true.
#The time for this will be O(n^2) because we will constantly have to subsequentally search for every value across the board.
#The space will be O(n^2) because in the worst case we will be adding every value to our hashmaps
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                point = board[row][col]
                if point == ".":
                    continue
                else:
                    if (point in rows[row]) or (point in cols[col]) or (point in squares[row//3, col//3]):
                        return False
                    else:
                        rows[row].add(point)
                        cols[col].add(point)
                        squares[(row//3, col//3)].add(point)

        return True
