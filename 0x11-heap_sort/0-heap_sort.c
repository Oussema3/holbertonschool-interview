#include "sort.h"
#include <math.h>

/**
 * swap_ - Swap between two elements in an array
 * @elem1: Pointer to element 1
 * @elem2: Pointer to the element 2
 */
void swap_(int *elem1, int *elem2)
{
int temp = *elem1;
*elem1 = *elem2;
*elem2 = temp;
}
/**
 * heapify - Put elements of 'a' in heap order, in-place
 *
 * @array: input: an unordered array
 * @size: the length of the input array
 */
void heapify(int *array, size_t size)
{
double iParent_size_i;
int start;

iParent_size_i = (int)((((int)size - 1) - 1) / 2);
start = (int)iParent_size_i;
while (start > 0 || start == 0)
{
siftDown(array, start, (int)size - 1, size);
start = start - 1;
}
}
/**
 * siftDown - Repair the heap whose root element is at index 'start',
 * assuming the heaps rooted at its children are valid.
 * @a: input: an unordered array
 * @start: root element index
 * @end: the last index of the array
 * @size: size of the array
 */
void siftDown(int *a, int start, int end, size_t size)
{
int root;
int iLeftChild_root;
int child;
int swap;

root = start;
while ((2 * root + 1 < end) || (2 * root + 1 == end))
{
iLeftChild_root = 2 * root + 1;
child = iLeftChild_root;
swap = root;
if (a[swap] < a[child])
swap = child;
if (((child + 1 < end) || (child + 1 == end)) && (a[swap] < a[child + 1]))
swap = child + 1;
if (swap == root)
return;
swap_(&a[root], &a[swap]);
print_array(a, size);
root = swap;
}
}
/**
 * heap_sort - sorts an array of integers in ascending order.
 * @array: input: an unordered array
 * @size: the length of the input array
 */
void heap_sort(int *array, size_t size)
{
int end;

if (size == 0)
return;
heapify(array, size);
end = (int)size - 1;
while (end > 0)
{
swap_(&array[end], &array[0]);
print_array(array, size);
end = end - 1;
siftDown(array, 0, end, size);
}
}
