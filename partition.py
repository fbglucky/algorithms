def is_subset_sum(arr, n, sum):
    """
    Let isSubsetSum(arr, n, sum/2) be the function that returns true if
    there is a subset of arr[0..n-1] with sum equal to sum/2

    The isSubsetSum problem can be divided into two subproblems
     a) isSubsetSum() without considering last element
        (reducing n to n-1)
     b) isSubsetSum considering the last element
        (reducing sum/2 by arr[n-1] and n to n-1)
    If any of the above the above subproblems return true, then return true.
    isSubsetSum (arr, n, sum/2) = isSubsetSum (arr, n-1, sum/2) ||
                                  isSubsetSum (arr, n-1, sum/2 - arr[n-1])
    """
    # Base Cases
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    # If last element is greater than sum, then
    # ignore it
    if arr[n - 1] > sum:
        return is_subset_sum(arr, n - 1, sum)

    ''' else, check if sum can be obtained by any of  
    the following 
    (a) including the last element 
    (b) excluding the last element'''

    return is_subset_sum(arr, n - 1, sum) or is_subset_sum(arr, n - 1, sum - arr[n - 1])


# Returns true if arr[] can be partitioned in two
# subsets of equal sum, otherwise false
def find_partion(arr, n):
    # Calculate sum of the elements in array
    sum = 0
    for i in range(0, n):
        sum += arr[i]
        # If sum is odd, there cannot be two subsets
    # with equal sum
    if sum % 2 != 0:
        return False

        # Find if there is subset with sum equal to
    # half of total sum
    return is_subset_sum(arr, n, sum // 2)


# Driver program to test above function
arr = [3, 1, 5, 9, 12]
n = len(arr)
if find_partion(arr, n):
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")
