/*
	Given an array A[1~n], please write code to find the smallest and largest element with function template form efficiently.
What is the complexity (BigO) of your implementation?
[Note] The basic algorithm use O(2n) comparison.
Ans:

The above code uses a divide-and-conquer approach to find the minimum and maximum elements of an array. It compares elements in pairs, and then compares the smaller element with the current minimum and the larger element with the current maximum. This reduces the number of comparisons to 3n/2 - 2 1.

Therefore, the complexity of this implementation is O(n).

*/

public static void FindMinMax<T>(T[] arr, out T min, out T max) where T : IComparable<T>
{
    if (arr == null || arr.Length == 0)
    {
        throw new ArgumentException("The array is null or empty.");
    }

    min = arr[0];
    max = arr[0];

    for (int i = 1; i < arr.Length; i += 2)
    {
        if (i == arr.Length - 1)
        {
            if (arr[i].CompareTo(min) < 0)
            {
                min = arr[i];
            }
            else if (arr[i].CompareTo(max) > 0)
            {
                max = arr[i];
            }
        }
        else
        {
            if (arr[i].CompareTo(arr[i + 1]) < 0)
            {
                if (arr[i].CompareTo(min) < 0)
                {
                    min = arr[i];
                }

                if (arr[i + 1].CompareTo(max) > 0)
                {
                    max = arr[i + 1];
                }
            }
            else
            {
                if (arr[i + 1].CompareTo(min) < 0)
                {
                    min = arr[i + 1];
                }

                if (arr[i].CompareTo(max) > 0)
                {
                    max = arr[i];
                }
            }
        }
    }
}