#include <vector>
#include <stack>

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    vector<int> reversePrint(ListNode* head) {
        vector<int> res;
        while(head) {
            res.push_back(head->val);
            head = head->next;
        }
        reverse(res.begin(), res.end());

        return res;
    }

    
    vector<int> reversePrint1(ListNode* head) {
        vector<int> res;

        if (!head) return res;
        reversPrint1(head->next);
        res.push_back(head->val);
        return res; 
    }


    vector<int> reversePrint1(ListNode* head) {
        stack<int> st;
        while(head) {
            st.push(head->val);
            head = head->next;
        }

        while(!st.empty()) {
            res.push_back(st.top());
            st.pop();
        }
        return res;   
    }
}；