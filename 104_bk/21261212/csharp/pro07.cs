/*
	Continue from the previous question. Refactoring code using generics type for array type.
Ans:

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