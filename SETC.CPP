 #include <stdio.h>
 #define MAX_SIZE 100
 void bubbleSort(int arr[], int n) {
 int i, j, temp;
 for (i = 0; i < n- 1; i++) {
 int swapped = 0;
 for (j = 0; j < n- i- 1; j++) {
 if (arr[j] > arr[j + 1]) {
 temp =arr[j];
 arr[j] = arr[j + 1];
 arr[j + 1] = temp;
 swapped = 1;
 }
 }
 if (swapped == 0) {
 break;
 }
 }
 }
 void printArray(int arr[], int size) {
 for (int i = 0; i < size; i++) {
 printf("%d ", arr[i]);
 }
 printf("\n");
 }
 int main() {
 int arr[MAX_SIZE];
 int n;
printf("Enter the number of elements: ");
 scanf("%d", &n);
 if (n > MAX_SIZE) {
 printf("Error: Number of elements exceeds the maximum allowed size.\n");
 return 1;
 }
 printf("Enter the elements:\n");
 for (int i = 0; i < n; i++) {
 printf("Element %d: ", i + 1);
 scanf("%d", &arr[i]);
 }
 bubbleSort(arr, n);
 printf("Sorted array:\n");
 printArray(arr, n);
 return 0;
    }