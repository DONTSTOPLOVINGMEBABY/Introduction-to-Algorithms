#include <stdio.h> 
#include <string.h> 
#include <stdbool.h> 

struct node {
    int data ; 
    struct node* next ; 
    struct node* prev ; 
} ; 

struct linked_list {
    struct node* head ;
} ; 

void list_prepend (struct linked_list * l, struct node * x) {
    x->next = l->head ; 
    x->prev = NULL ; 
    if (l->head != NULL){
        l->head->prev = x ; 
    }
    l->head = x ; 
}

struct node * list_search (struct linked_list * l, int key){
    struct node * ptr = l->head ; 
    while (ptr != NULL && ptr->data != key){
        ptr = ptr->next ; 
    }
    return ptr ; 
}

void list_delete (struct linked_list * l, struct node * x){
    if (x->prev != NULL){ x->prev->next = x->next ; }
    else { l->head = x->next ; }
    if (x->next != NULL){ x->next->prev = x->prev ; }
}

void list_insert (struct node * new_element, struct node * old_element){
    new_element->next = old_element->next ; 
    new_element->prev = old_element ; 
    if (old_element->next != NULL){ old_element->next->prev = new_element ; }
    old_element->next = new_element ;  
}


void print_linked_list (struct linked_list * l) {
    struct node * ptr = l->head ; 
    while (ptr != NULL){
        printf("%d\n", ptr->data) ; 
        ptr = ptr->next ; 
    }
    puts("") ; 
}


int main(){

    struct node first = { 1, NULL, NULL } ; 
    struct node second = { 2, NULL, NULL } ; 
    struct node third = { 3, NULL, NULL } ; 
    struct node fourth = { 4, NULL, NULL } ; 
    struct node fifth = { 5, NULL, NULL } ;  
    struct linked_list ll = { NULL } ; 


    list_prepend(&ll, &first) ; 
    list_prepend(&ll, &second) ; 
    list_prepend(&ll, &third) ; 
    list_prepend(&ll, &fourth) ; 
    
    print_linked_list(&ll) ; 

    puts("Removing third element from the list:") ; 
    list_delete(&ll, &third) ; 

    print_linked_list(&ll) ; 

    struct node * hello = list_search(&ll, first.data) ; 
    printf("Printing return result of hello: %d\n", hello->data) ; 

    puts("Inserting 1000 after 4...") ; 
    struct node one_thousand = { 1000, NULL, NULL } ; 
    list_insert(&one_thousand, &fourth) ; 

    print_linked_list(&ll) ; 

    return 0 ; 
}