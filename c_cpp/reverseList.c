//
// Created by young on 02/01/2021.
//
#include <stddef.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *reverseList(struct ListNode *head) {
    typedef struct ListNode *PtrToLNode;

    PtrToLNode new_head, old_head, temp;

    old_head = head;
    new_head = NULL;

    while (old_head) {
        temp = old_head->next;
        old_head->next = new_head;
        new_head->next = old_head;
        old_head = temp;
    }
    head = new_head;

    return head;
}

struct ListNode *ReverseList(struct ListNode *pHead) {
    struct ListNode *pReversedHead = NULL;
    struct ListNode *pNode = pHead;
    struct ListNode *pPrev = NULL;

    while (pNode != NULL) {
        struct ListNode *pNext = pNode->next;
        if (pNext == NULL) pReversedHead = pNode;

        pNode->next = pPrev;
        pPrev = pNode;
        pNode = pNext;
    }
    return pReversedHead;
}
