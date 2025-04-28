class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0
        
        m, n = len(image), len(image[0])
        
        # Search for left boundary (column)
        left = self.binary_search_column(image, 0, y, 0, m-1, True)
        
        # Search for right boundary (column)
        right = self.binary_search_column(image, y, n-1, 0, m-1, False)
        
        # Search for top boundary (row)
        top = self.binary_search_row(image, 0, x, left, right, True)
        
        # Search for bottom boundary (row)
        bottom = self.binary_search_row(image, x, m-1, left, right, False)
        
        return (right - left + 1) * (bottom - top + 1)
    
    def binary_search_column(self, image, start, end, top, bottom, find_left):
        while start < end:
            mid = start + (end - start) // 2 if find_left else end - (end - start) // 2
            
            # Check if this column has any black pixel
            has_black = False
            for i in range(top, bottom + 1):
                if image[i][mid] == '1':
                    has_black = True
                    break
            
            if has_black:
                if find_left:
                    end = mid  # Continue searching left
                else:
                    start = mid  # Continue searching right
            else:
                if find_left:
                    start = mid + 1  # Move right
                else:
                    end = mid - 1  # Move left
        
        return start
    
    def binary_search_row(self, image, start, end, left, right, find_top):
        while start < end:
            mid = start + (end - start) // 2 if find_top else end - (end - start) // 2
            
            # Check if this row has any black pixel
            has_black = False
            for j in range(left, right + 1):
                if image[mid][j] == '1':
                    has_black = True
                    break
            
            if has_black:
                if find_top:
                    end = mid  # Continue searching up
                else:
                    start = mid  # Continue searching down
            else:
                if find_top:
                    start = mid + 1  # Move down
                else:
                    end = mid - 1  # Move up
        
        return start