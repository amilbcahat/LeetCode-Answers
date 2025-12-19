func countPairs(d []int) int {
    countMap := map[int]int{}

    mod := 1_000_000_007

    ans := 0

    for _, elem := range d {
        for p := 1; p <= 1 << 21; p *= 2 {
            complement := p - elem
            if countMap[complement] >= 0 {
                ans = (ans + countMap[complement]) % mod
            }
        }
        countMap[elem] += 1
    }

    return ans
}