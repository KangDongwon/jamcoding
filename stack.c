#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 10 // 스택의 최대 크기

// 스택 구조체 정의
typedef struct {
    int items[MAX_SIZE]; // 스택 요소를 저장하는 배열
    int cursor; // 스택의 맨 위 요소의 인덱스를 가리킴
} Stack;

Stack stack; // 스택 구조체 전역 변수

// 스택 초기화 함수
void initStack() {
    stack.cursor = -1; // 스택이 비어있는 상태로 초기화
}

// 스택이 비어있는지 확인하는 함수
bool isEmpty() {
    return stack.cursor == -1;
}

// 스택이 가득 차있는지 확인하는 함수
bool isFull() {
    return stack.cursor == MAX_SIZE - 1;
}

// 스택에 요소를 추가하는 함수 (푸시)
void push(int item) {
    if (isFull()) {
        printf("Stack overflow\n");
        return;
    }
    stack.items[++stack.cursor] = item;
}

// 스택에서 요소를 제거하고 반환하는 함수 (팝)
int pop() {
    if (isEmpty()) {
        printf("Stack underflow\n");
        return -1; // 임의의 값 반환
    }
    return stack.items[stack.cursor--];
}

void printStack() {
    if (isEmpty()) {
        printf("stack is empty!");
        return;
    }

    int i;
    printf("\n");

    for(i=stack.cursor; i>=0; i--) {
        printf("%d item : %d\n", i, stack.items[i]);
    }

    printf("\n");
}

int main() {

    initStack();

    push(1);
    push(2);
    push(3);

    printStack();

    printf("pop! item %d\n", pop());

    printStack();

    return 0;
}