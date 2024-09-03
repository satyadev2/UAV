#include <bits/stdc++.h>
using namespace std;
int solve(vector<int> a, vector<int> b)
{
    int count = 0;
    vector<int> res;
    unordered_set<int> s;
    for (auto i : a)
    {
        s.insert(i);
    }
    for (auto i : b)
    {
        if (s.find(i) == s.end())
        {
            count++;
        }
    }
    return count;
}
int main()
{
}