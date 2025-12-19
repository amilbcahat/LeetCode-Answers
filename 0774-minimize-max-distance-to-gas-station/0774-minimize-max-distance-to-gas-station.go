import "math"

func minmaxGasDist(stations []int, k int) float64 {
    n := len(stations)
    
    // Find max gap
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
            needed += int(math.Ceil(gap/mid)) - 1  // ✅ Correct formula
        }
        return needed <= k
    }

    // Float binary search
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
// ```

// ---

// ## The Bug Visualized
// ```
// Your formula:    gap + mid - 1 / mid
//                  └─────┬─────┘
//                        ↓
//                  gap + mid - (1/mid)    ← Division first!

// Example: gap=10, mid=3
//   Your:    10 + 3 - (1/3) = 12.67  ❌
//   Correct: (10 + 3 - 1) / 3 = 4    ✅