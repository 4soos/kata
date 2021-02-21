typedef struct {
    int len;
    int top1;
    int top2;
    int *s1;//栈1，入栈=入队
    int *s2;//栈2，出栈=出队
} CQueue;


CQueue* cQueueCreate() {
    CQueue *queue = malloc(sizeof(CQueue));
    queue->len = 10000;
    queue->top1 = -1;
    queue->top2 = -1;
    queue->s1 = malloc(queue->len * sizeof(int));
    queue->s2 = malloc(queue->len * sizeof(int));
    return queue;
}

void cQueueAppendTail(CQueue* obj, int value) {
    if(obj->top1 == -1)
        while(obj->top2 != -1)
            obj->s1[++(obj->top1)] = obj->s2[obj->top2--];
    obj->s1[++(obj->top1)] = value;
}

int cQueueDeleteHead(CQueue* obj) {
    if(obj->top2 == -1)
        while(obj->top1 != -1)
            obj->s2[++(obj->top2)] = obj->s1[obj->top1--];
    return obj->top2==-1 ? -1 : obj->s2[obj->top2--];
}

void cQueueFree(CQueue* obj) {
    free(obj->s1);
    free(obj->s2);
    free(obj);
}

/**
 * Your CQueue struct will be instantiated and called as such:
 * CQueue* obj = cQueueCreate();
 * cQueueAppendTail(obj, value);
 
 * int param_2 = cQueueDeleteHead(obj);
 
 * cQueueFree(obj);
*/


#define MaxSize 1000

typedef struct {
    int in_top, out_top;
    int *push_stack;
    int *pop_stack;
}ArrayQueue;

ArrayQueue *arrayQueue() {
    ArrayQueue obj = (ArrayQueue)malloc(sizeof(ArrayQueue));
    obj.pop_stack = (int*) malloc(MaxSize * sizeof(int));
    obj.push_stack = (int*) malloc(MaxSize * sizeof(int));
    obj.in_top = -1;
    obj.out_top = -1;
    return obj;
}

void QueueAppendTail(ArrayQueue* obj, int value) {
    obj->push_stack[++(obj->in_top)] = value; // insert new element
}

int QueueDeleteHead(ArrayQueue* obj) {
    if (obj->out_top == -1) {
        if (obj->in_top == -1) return -1;
        while (obj->in_top > -1)
            obj->pop_stack[++(obj->out_top)] = obj->push_stack[obj->in_top--];
    }

    return obj->pop_stack[(obj->out_top)--];
}

void QueueFree(ArrayQueue* obj) {
    free(obj->push_stack);//回收资源
    obj->push_stack = NULL;//删除指针(置空)解除映射
    free(obj->pop_stack);
    obj->pop_stack = NULL;
    free(obj);
    obj = NULL;
}
