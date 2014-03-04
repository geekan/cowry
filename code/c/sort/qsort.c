#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists）。
步骤为：
从数列中挑出一个元素，称为 "基准"（pivot），
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面
（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。
这个称为分区（partition）操作。
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

算法伪代码
	function quicksort(q)
		var list less, pivotList, greater
		if length(q) ≤ 1 {
			return q
		} else {
			select a pivot value pivot from q
			for each x in q except the pivot element
				if x < pivot then add x to less
				if x ≥ pivot then add x to greater
			add pivot to pivotList
			return concatenate(quicksort(less), pivotList, quicksort(greater))
		}

原地(in-place)分区的版本
上面简单版本的缺点是，它需要Ω(n)的额外存储空间，也就跟归并排序一样不好。
额外需要的存储器空间配置，在实际上的实现，也会极度影响速度和高速缓存的性能。
有一个比较复杂使用原地（in-place）分区算法的版本，且在好的基准选择上，
平均可以达到O(log n)空间的使用复杂度。

	function partition(a, left, right, pivotIndex)
		pivotValue := a[pivotIndex]
		swap(a[pivotIndex], a[right]) // 把 pivot 移到結尾
		storeIndex := left
		for i from left to right-1
			if a[i] < pivotValue
				swap(a[storeIndex], a[i])
				storeIndex := storeIndex + 1
		swap(a[right], a[storeIndex]) // 把 pivot 移到它最後的地方
		return storeIndex	
	
这是原地分区算法，它分区了标示为 "左边（left）" 和 "右边（right）" 的串行部份，
借由移动小于a[pivotIndex]的所有元素到子串行的开头，留下所有大于或等于的元素接在他们后面。
在这个过程它也为基准元素找寻最后摆放的位置，也就是它回传的值。
它暂时地把基准元素移到子串行的结尾，而不会被前述方式影响到。
由于算法只使用交换，因此最后的数列与原先的数列拥有一样的元素。
要注意的是，一个元素在到达它的最后位置前，可能会被交换很多次。
一旦我们有了这个分区算法，要写快速排列本身就很容易：
	
	
	
*/


/*

35976481234
      |
选定一个基准元素，如8
然后置换8到最后一位。
35976441238
      |
开始for循环，从0到最后一位前
如果小于pivotValue，那么和storeIndex替换，并且storeIndex++

35796441238
   |
storeIndex:2

35697441238
    |
storeIndex:3

*/

int middle(int *a, int x, int y, int z)
{
	if (a[x] > a[y]) {
		if (a[y] > a[z])
			return y;
		else
			return z;
	} else {
		if (a[x] > a[z])
			return z;
		else
			return x;
	}
}

int select_pivot(int *a, int left, int right)
{
	int m = (left + right) / 2;
	//return middle(a, left, right, m);
	return left;
}

void swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

int partition(int *a, int left, int right, int pivotIndex)
{
	int i;
	int pivotValue = a[pivotIndex];
	int storeIndex = left;

	swap(a + pivotIndex, a + right);

	for (i = left; i < right - 1; i++) {
		if (a[i] < pivotValue) {
			swap(a + i, a + storeIndex);
			++storeIndex;
		}
	}
	swap(a + right, a + storeIndex);
	return storeIndex;
}

void quick_sort(int *a, int left, int right)
{
	int pivotIndex;
	int storeIndex;

	if (left < right) {
		pivotIndex = select_pivot(a, left, right);
		storeIndex = partition(a, left, right, pivotIndex);
		quick_sort(a, left, storeIndex - 1);
		quick_sort(a, storeIndex + 1, right);
	}
}

int main()
{
	int i;
	int asize = 5;
	int a[] = {1, 5, 9, 7, 3};
	quick_sort(a, 0, asize - 1);
	for (i = 0; i < asize; i++)
		printf("%d ", a[i]);
	return 0;
}