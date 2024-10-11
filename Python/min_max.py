class Solution:
    def get_min_max(self, arr):
    
        mn = arr[0]
        mx = arr[0]

        for i in range(len(arr)):
            if arr[i] < mn:
                mn = arr[i]
            elif arr[i] > mx:
                mx = arr[i]

        return mn, mx


if __name__ == '__main__':
    arr = [3, 2, 1, 56, 10000, 167]
    ob = Solution()
    mn, mx = ob.get_min_max(arr)
    print(mn, mx)