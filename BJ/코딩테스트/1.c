#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char* ltrim(char*);
char* rtrim(char*);

int parse_int(char*);

typedef struct SinglyLinkedListNode SinglyLinkedListNode;
typedef struct SinglyLinkedList SinglyLinkedList;

struct SinglyLinkedListNode {
    int data;
    SinglyLinkedListNode* next;
};

struct SinglyLinkedList {
    SinglyLinkedListNode* head;
    SinglyLinkedListNode* tail;
};

SinglyLinkedListNode* create_singly_linked_list_node(int node_data) {
    SinglyLinkedListNode* node = malloc(sizeof(SinglyLinkedListNode));

    node->data = node_data;
    node->next = NULL;

    return node;
}

void insert_node_into_singly_linked_list(SinglyLinkedList** singly_linked_list, int node_data) {
    SinglyLinkedListNode* node = create_singly_linked_list_node(node_data);

    if (!(*singly_linked_list)->head) {
        (*singly_linked_list)->head = node;
    } else {
        (*singly_linked_list)->tail->next = node;
    }

    (*singly_linked_list)->tail = node;
}

void print_singly_linked_list(SinglyLinkedListNode* node, char* sep, FILE* fptr) {
    while (node) {
        fprintf(fptr, "%d", node->data);

        node = node->next;

        if (node) {
            fprintf(fptr, "%s", sep);
        }
    }
}


/*
 * Complete the 'getNumber' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts INTEGER_SINGLY_LINKED_LIST binary as parameter.
 */

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
typedef struct ListNdoe{
    int value;
    struct ListNode *Link;
}ListNode;

long getNumber(int *first) {
    int temp;
    temp = *first;
    ListNode *binary = (ListNode *)malloc(sizeof(ListNode));
    binary->value = 0;
    binary ->Link = NULL;
    
    if(temp >= 0){
        ListNode *newNode = (ListNode *)malloc(sizeof(ListNode));
        binary -> Link = newNode;
        newNode->value = 0;
        newNode ->Link = NULL;
        while(temp >= 1){
            ListNode *node2 = (ListNode *)malloc(sizeof(ListNode));
            node2 ->value = temp % 2;
            node2 -> Link = NULL;
            newNode ->Link = node2;
        }
    }
    else{
        ListNode *newNode = (ListNode *)malloc(sizeof(ListNode));
        newNode->value = 1;
        newNode ->Link = NULL;
    }
    
    

}

int main(){
    
    int x;
    scanf( "%d", &x);
    
    
    getNumber(&x);
    
}