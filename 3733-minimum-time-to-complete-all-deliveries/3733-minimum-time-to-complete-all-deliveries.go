func minimumTime(d []int, r []int) int64 {

    gcd := func(a int, b int) int { 
        for b != 0 {
            t := b 
            b = a % b 
            a = t 
        }
        return a 
    }

     lcm := func(a int , b int) int {
        return (a * b) / gcd(a, b)
    }

    check := func(mid int, d []int, r []int) bool{
        both := mid / lcm(r[0], r[1])
        first := mid - (mid / r[0])
        second :=  mid - (mid / r[1])
        avail := mid - both

        if (first < d[0] || second < d[1]){
            return false
        }

        return avail >= (d[0] + d[1])
    }

    left  := 0 
    right  := (d[0] * r[0]) + (d[1] * r[1])
    res := -1
    for left <= right {
        mid := left + (right - left) / 2
        if check(mid, d, r){
            res = mid 
            right = mid - 1
        }else{
            left = mid + 1
        }
    }
    return int64(res) 
}