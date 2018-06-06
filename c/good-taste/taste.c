#include <stdio.h>
#include <stdlib.h>

typedef struct node node;
struct node{
   int value;
   node* next;
};

struct list{
   node* head;
   node* tail;
};
typedef struct list list;

list* createList(){
   list* newList = (list*)malloc(sizeof(list));
   newList->head = NULL;
   newList->tail = NULL;
   return newList;
}

void appendToList(list* list, int value){
   node* newNode = (node*)malloc(sizeof(node));
   newNode->value = value;
   newNode->next = NULL;

   if (list->head == NULL){
      list->head = newNode;
      list->tail = newNode;
   }else{
      list->tail->next = newNode;
      list->tail = newNode;
   }

   return;
}

void printList(list* list){
   for (node* node=list->head; node!=NULL; node=node->next){
      printf("%d\n", node->value);
   }
}

void freeList(list* list){

   for (node* curr=list->head; curr!=NULL;){
      node* next = curr->next;
      free(curr);
      curr = next;
   }

   free(list);
}

/*

Bad Taste Snippet

remove_list_entry(entry)
{
   prev = NULL;
   walk = head;

   // Walk the list

   while (walk != entry){
      prev = walk;
      walk = walk->next;
   }

   // Remove the entry by updating the
   // head or the previous entry

   if (!prev)
      head = entry->next;
   else
      prev->next = entry->next;
}

*/


void removeValueFromListBad(list* list, int value){
   node* prev = NULL;
   node* walk = list->head;

   // Walk the list
   while(walk->value != value){
      prev = walk;
      walk = walk->next;
   }

   // Remove the entrybu updating the head or the previous entry
   if (!prev)
      list->head = walk->next;
   else
      prev->next = walk->next;
   
   free(walk);
}

/*

Good Taste Snippet

remove_list_entry(entry)
{
   // The "indirect" pointer points to the
   // *address* of the thing we'll update

   indirect = &head;

   // Walk the list, looking for the thing that
   // points to the entry we want to remove

   while ((*indirect) != entry)
      indirect = &(*indirect)->next;

   // .. and just remove it
   *indirect = entry->next;
}
*/

/*
// ??????
void removeValueFromListGood(list* list, int value){
   void* prev = NULL;
   void* indirect = &(list->head);

   while ((*indirect->value) != value)
      prev = &(*indirect);
      indirect = &(*indirect)->next;

   *indirect = &(*indirect->next;

   return;
}
*/




int main(){

   list* myList = createList();

   appendToList(myList, 6);
   appendToList(myList, 9);
   appendToList(myList, 8);
   appendToList(myList, 5);

   printf("Before:\n\n");
   printList(myList);

   removeValueFromListBad(myList, 8);

   printf("After:\n\n");
   printList(myList);

   freeList(myList);

   return 0;
}