/**
 *  Definition for singly-linked list.
 * 
 *  struct ListNode {
 *      int val;
 *      struct ListNode *next;
 *  }
 * 
 * */
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

int* reversePrint(struct ListNode* head, int* returnSize) {
    if (head == NULL) {
        *returnSize = 0;
        return malloc(sizeof(int) * 10000);
    }

    int *ans = reversePrint(head->next, returnSize);
    ans[(*returnSize)++] = head->val;

    return ans;
}

// test
int main() {
    struct ListNode ln1;
    struct ListNode ln2;
    struct ListNode ln3;
    ln1.val = 0;
    ln2.val = 1;
    ln3.val = 2;

    ln1.next = &ln2;
    ln2.next = &ln3;
    ln3.next = NULL;
    
    int size;
    reversePrint(&ln1, &size);

    printf("The list node size is %d", size);

    return 0;
}