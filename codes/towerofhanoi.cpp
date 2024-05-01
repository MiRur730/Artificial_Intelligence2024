#include<iostream>
using namespace std;


class Solution{
    public:
long long count=0;
void TOHhelper(int N,int source,int dest,int aux){
if(N>0){
    TOHhelper(N-1,source,aux,dest);
    count++;
    TOHhelper(N-1,aux,dest,source);
}

}
long long toh(int N,int source,int dest,int aux){
    TOHhelper(N,source,dest,aux);
    return count;
}
};


int main() {
    Solution sol;
    int N = 3; // Change N to the number of disks
    int source = 1; // Change source to the source peg index
    int dest = 3; // Change dest to the destination peg index
    int aux = 2; // Change aux to the auxiliary peg index

    long long moves = sol.toh(N, source, dest, aux);
    cout << "Total moves required: " << moves << endl;

    return 0;
}