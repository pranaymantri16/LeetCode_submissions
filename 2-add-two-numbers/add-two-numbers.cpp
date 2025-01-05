/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* createLinkedList(const vector<int>& values) {
        ListNode* dummy_head = new ListNode(0);
        ListNode* current = dummy_head;

        for (int val : values) {
            current->next = new ListNode(val);
            current = current->next;
        }

        return dummy_head->next;
    }


     ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        vector<int> result;
        int carry = 0;

        while (l1 || l2 || carry) {
            int sum_val = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
            carry = sum_val / 10;

            result.push_back(sum_val % 10);

            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }

        return createLinkedList(result);
    }
};