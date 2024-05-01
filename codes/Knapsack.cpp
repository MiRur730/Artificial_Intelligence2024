int solve(vector<int>&weight,vector<int>&value,int index,int W){
    if(index==0){
        if(weight[0]<=W){
            return value[0];
        }
        else{
            return 0
        }
    }
    int include=0;
    if(weight[index]<=W){
         include=value[index]+solve(weight,value,index-1,W-weight[index])
    }

    int exclude=0+solve(weight,capaciity,index-1,W);

    int ans=max(exclude,include);
    return ans;

}