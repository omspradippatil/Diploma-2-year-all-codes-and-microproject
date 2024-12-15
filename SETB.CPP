 #include <stdio.h>
 #define MAX_SIZE 100
 int binarySearch(int arr[], int left, int right, int target) {
 while (left <= right) {
 int mid = left + (right- left) / 2;
 if (arr[mid] == target) {
 return mid;
 }
 if (arr[mid] < target) {
 left = mid + 1;
 } else {
 right = mid- 1;
 }
 }
 return-1;
 }
 int main() {
 int arr[MAX_SIZE];
 int n, target;
 printf("Enter the number of elements: ");
 scanf("%d", &n);
 if (n > MAX_SIZE) {
 printf("Error: Number of elements exceeds the maximum allowed size.\n");
return 1;
 }
 printf("Enter the sorted elements:\n");
 for (int i = 0; i < n; i++) {
 scanf("%d", &arr[i]);
 }
 printf("Enter the number to search: ");
 scanf("%d", &target);
 int result = binarySearch(arr, 0, n- 1, target);
 if (result !=-1) {
 printf("Number found at index %d.\n", result);
 } else {
 printf("Number not found.\n");
 }
 return 0;
 }
