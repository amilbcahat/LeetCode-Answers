class MyCalendarTwo:

    def __init__(self):
        self.overlap_books = []
        self.books = []

    def book(self, startTime: int, endTime: int) -> bool:
        for booking in self.overlap_books: 
            if max(startTime, booking[0]) < min(endTime, booking[1]):
                return False #False on triple

        for booking in self.books:
            if max(startTime, booking[0]) < min(endTime, booking[1]):
                self.overlap_books.append([max(startTime, booking[0]), min(endTime, booking[1])]) #Doublde overlap ad


        self.books.append([startTime, endTime]) #Add on single or double overlap
        return True
         
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)