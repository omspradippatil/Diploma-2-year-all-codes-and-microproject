 #include <stdio.h>
 #define MAX_SIZE 100
 void displayArray(int arr[], int size);
 void deleteElement(int arr[], int *size, int position);
 int main() {
 int arr[MAX_SIZE];
 int size = 0;
 printf("Enter the number of elements in the array: ");
 scanf("%d", &size);
 if (size > MAX_SIZE || size < 0) {
 printf("Invalid size! Must be between 0 and %d.\n",
 MAX_SIZE);
 return 1;
 }
 printf("Enter %d elements: ", size);
 for (int i = 0; i < size; i++) {
 scanf("%d", &arr[i]);
 }
 printf("Array before deletion: ");
 displayArray(arr, size);
 int position;
 printf("Enter the position of the element to delete: ");
 scanf("%d", &position);
 deleteElement(arr, &size, position);
printf("Array after deletion: ");
 displayArray(arr, size);
 return 0;
 }
 void displayArray(int arr[], int size) {
 for (int i = 0; i < size; i++) {
 printf("%d ", arr[i]);
 }
 printf("\n");
 }
 void deleteElement(int arr[], int *size, int position) {
 if (position < 0 || position >= *size) {
 printf("Invalid position!\n");
 return;
 }
 for (int i = position; i < *size- 1; i++) {
 arr[i] = arr[i + 1];
 }
 (*size)--;
 }