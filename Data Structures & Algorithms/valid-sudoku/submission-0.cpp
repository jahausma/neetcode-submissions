class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // we are checking for duplicates so we could use an unordered_map
        // create hash_map for each row, column, and square
        // unordered_map<int, char> hash_row;   // first number is row and second is element of board
        // unordered_map<int, char> hash_col;   // first number is col and second is element of board
        // unordered_map<int,char> hash_square; // first number is square and second is element of board

        // we could also use bitmasking to find if duplicates are found
        // initialize array for each row, col, and square
        int row[9] = {0};
        int col[9] = {0};
        int square[9] = {0};

        // iterate through each row and col
        // we can find which square each element would belong to by using square = (r/3) * 3 + (c/3)

        for(int r = 0; r < 9; r++){
            for(int c =0; c < 9; c++){
                if(board[r][c] == '.'){continue;}

                int val = board[r][c] - '1';

                if((row[r] & (1 << val)) || (col[c] & (1 << val)) || 
                    (square[(r/3)*3 + (c/3)] & (1 << val))) {
                        return false;
                    }

                row[r] |= (1 << val);
                col[c] |= (1 << val);
                square[(r/3)*3 + (c/3)] |= (1 << val);

            }
        }
        return true;
    }
};
