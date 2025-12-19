func minmaxGasDist(stations []int, k int) float64 {
    left := 0.0
    right := 0.0
    n := len(stations)
    for i := 1; i < n; i++ {
        gap := float64(stations[i] - stations[i - 1])
        if gap > right {
            right = gap
        }
    }

    var check func(mid float64, stations []int, k int) bool
    check = func(mid float64, stations []int, k int) bool {
        needed := 0 
        n := len(stations)
        for p := 1; p < n; p++ {
            gap := float64(stations[p] - stations[p-1])
            // Points needed = ceil(gap/mid) - 1 = floor(gap/mid) when gap > mid
            needed += int(gap / mid)      
        }  

        return needed <= k
    }

    //In go float is handled like this
    left = 1e-9
    for i := 0; i < 100 ; i++ {
        mid := (right + left) / 2 
        if check(mid, stations, k){
            right = mid
        }else{
            left = mid
        }
    }

    return right
}