#include <iostream>
#include<vector>
using namespace std;

void addSolution(vector<vector<int>>&board, vector<vector<int>>&ans,int n){
    vector<int> temp;
    
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
             temp.push_back(board[i][j]);
        }
    }
    ans.push_back(temp);
}

bool isSafe(int row,int col,vector<vector<int>>& board,int n){
    int x=row;
    int y=col;



    while (y>=0){
        if(board[x][y]==1){
        return false;
        }
            
    y--;
        
    }

 //same diagnol

  x=row;
  y=col;
 while(x>=0 && y>=0){
    if(board[x][y]==1){
        return false;
        }
        x--;
        y--;
}

  x=row;
  y=col;
 while(x<n && y>=0){
    if(board[x][y]==1){
        return false;
        }
        x++;
        y--;
}
return true;
}


void solve(int col,vector<vector<int>>&board,vector<vector<int>>&ans,int n){

//base case
if (col==n){
    addSolution(board,ans,n);
}

//solve 1case rest recursion will solve

for(int row=0;row<n;row++){
    if(isSafe(row,col,board,n)){
        board[row][col] = 1;
        solve(col+1,board,ans,n);

        board[row][col] =0;
    }
}
}

vector<vector<int>> nQueen(int n){
   vector<vector<int>> board(n,vector<int>(n,0));
   vector<vector<int>> ans;


   solve(0,board,ans,n);
   return ans;
}


void printBoard(const vector<vector<int>>& board) {
    for (const auto& row : board) {
        for (int cell : row) {
            cout << cell << " ";
        }
        cout << endl;
    }
    cout << endl;
}

int main() {
    int n = 4; // Change n to the desired size of the board
    vector<vector<int>> solutions = nQueen(n);
    cout << "Total solutions for " << n << "-Queens: " << solutions.size() << endl;
    cout << "One of the solutions:" << endl;
    if (!solutions.empty()) {
        printBoard(solutions[0]); // Print the first solution
    }
    return 0;
}
