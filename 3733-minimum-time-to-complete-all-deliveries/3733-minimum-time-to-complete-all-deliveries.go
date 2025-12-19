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
        both := mid / lcm(r[0], r[1]) //Both recharge here 
        first := mid - (mid / r[0]) //d[1] recharge here 
        second :=  mid - (mid / r[1]) // d[2] recharge here 
        avail := mid - both //Left for available

        if (first < d[0] || second < d[1]){
            //Condition of invalid
            return false
        }

        //If availed boxes are more 
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