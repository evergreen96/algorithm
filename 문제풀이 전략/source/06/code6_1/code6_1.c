#include <stdio.h>
#include <stdlib.h>
#define MAX 100
#define TRUE 1
#define FALSE 0

// 함수 원형
void MakeRandomNumber(void);
void SelectionSort(void);
void DisplayBuffer(void);
int IsNumberExit(int, int);
int Buf[MAX];

// 정렬할 데이터의 초기화
void MakeRandomNumber(void)
{
	int i, Num;
	i = 1;
	srand((unsigned)time(NULL));
	Buf[0] = 100;

	while (i < MAX) {
		Num = rand() % MAX;
		if (!IsNumberExit(Num, i)) {
			Buf[i] = Num;
			i++;
		}
	}
}

void SelectionSort(void)
{
	int i, j, min, dummy;

	for (i = 0; i < MAX; i++) {
		min = i;

		for (j = i + 1; j < MAX; j++)
			if (Buf[j] < Buf[min])
				min = j;

		dummy = Buf[min];
		Buf[min] = Buf[i];
		Buf[i] = dummy;
	}
}

// 배열 Buf에 저장된 데이터 출력
void DisplayBuffer(void)
{
	int i;

	for (i = 0; i < MAX; i++) {
		if ((i % 10) == 0)
			printf("\n");

		printf("%4d ", Buf[i]);
	}

	printf("\n");
}

// 이미 생성된 값이 아닌지를 검사
int IsNumberExit(int number, int index)
{
	int i;

	for (i = 0; i < index; i++) {
		if (Buf[i] == number || number == 0)
			return TRUE;
	}

	return FALSE;
}

void main()
{
	printf("정렬할 데이터 초기화 \n");

	MakeRandomNumber();
	DisplayBuffer();
	printf("정렬 후 데이터 \n");

	SelectionSort();
	DisplayBuffer();
	printf("\n");
}