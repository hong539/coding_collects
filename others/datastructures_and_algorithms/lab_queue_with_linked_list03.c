#include <stdio.h>
#include <stdlib.h>

// 宣告節點結構
struct Node {
    int data;
    struct Node* next;
};

// 宣告佇列結構
struct Queue {
    struct Node *front, *rear;
};

// 初始化佇列
struct Queue* createQueue() {
    struct Queue* q = (struct Queue*)malloc(sizeof(struct Queue));
    q->front = q->rear = NULL;
    return q;
}

// 建立新節點
struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->next = NULL;
    return node;
}

// 判斷佇列是否為空
int isEmpty(struct Queue* q) {
    return (q->front == NULL);
}

// 將節點加入佇列
void enqueue(struct Queue* q, int data) {
    struct Node* node = newNode(data);
    if (isEmpty(q)) {
        q->front = q->rear = node;
        return;
    }
    q->rear->next = node;
    q->rear = node;
}

// 從佇列移除節點
void dequeue(struct Queue* q) {
    if (isEmpty(q)) {
        printf("Queue is empty\n");
        return;
    }
    struct Node* temp = q->front;
    q->front = q->front->next;
    free(temp);
}

// 取得佇列最前面的節點
int front(struct Queue* q) {
    if (isEmpty(q)) {
        printf("Queue is empty\n");
        return -1;
    }
    return q->front->data;
}

// 取得佇列最後面的節點
int rear(struct Queue* q) {
    if (isEmpty(q)) {
        printf("Queue is empty\n");
        return -1;
    }
    return q->rear->data;
}

int main() {
    struct Queue* q = createQueue();
    enqueue(q, 10);
    enqueue(q, 20);
    enqueue(q, 30);
    enqueue(q, 40);

    printf("Queue front: %d\n", front(q));
    printf("Queue rear: %d\n", rear(q));

    dequeue(q);
    dequeue(q);

    printf("Queue front: %d\n", front(q));
    printf("Queue rear: %d\n", rear(q));

    // Queue front: 10
    // Queue rear: 40
    // Queue front: 30
    // Queue rear: 40

    return 0;
}
