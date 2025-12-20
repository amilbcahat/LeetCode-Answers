func longestOnes(nums []int, k int) int {

    prefix := []int{0}
    n := len(nums)
    for idx := 0; idx < n; idx++ {
        prefix = append(prefix, prefix[idx] + nums[idx])
    }

    numZeros := func(l int, r int) int {
        return (r - l + 1) - (prefix[r+1] - prefix[l])
    }

    check := func(st int, x int) bool {
        return numZeros(st, x) <= k
    }

    total := 0

    for st, _ := range nums {
        l := st 
        r := n - 1
        ans := st - 1
        for l <= r {
            mid := (l + r) / 2 
            if check(st, mid){
                ans = mid 
                l = mid + 1
            }else{
                r = mid - 1
            }
        }
        total = max(total, ans - st + 1)
    }

    return total
    
}