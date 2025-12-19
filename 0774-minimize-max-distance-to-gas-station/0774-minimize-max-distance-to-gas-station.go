import "math"

func minmaxGasDist(stations []int, k int) float64 {
    n := len(stations)
    
    right := 0.0
    for i := 1; i < n; i++ {
        gap := float64(stations[i] - stations[i-1])
        if gap > right {
            right = gap
        }
    }

    check := func(mid float64) bool {
        needed := 0
        for p := 1; p < n; p++ {
            gap := float64(stations[p] - stations[p-1])
            needed += int(math.Ceil(gap/mid)) - 1  // ✅ Must use Ceil for floats
        }
        return needed <= k
    }

    left := 1e-6
    for i := 0; i < 100; i++ {
        mid := (right + left) / 2
        if check(mid) {
            right = mid
        } else {
            left = mid
        }
    }

    return right
}