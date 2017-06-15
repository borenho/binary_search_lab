class BinarySearch(list):
    def __init__(self, a, b):
        """ Class constructor method """
        # Initialize the super class
        super().__init__()

        # Populate the class
        for i in range(1, a+1):
            self.append(i * b)

        # Get length of object
        self.length = len(self)
        

    def search(self, item):
        """
            Locate item by binary search
        """
        count = 0
        # Get the first item, last item, and middle item in the sorted list
        lower = 0
        upper = len(self) - 1
        found = False

        
        if item in self:
            
            # Return the last item if it is item
            if item == self[-1]:
                index = upper
                found = True

            # Peform Binary search using a while loop
            while lower <= upper and not found:
                # Get mid value
                mid = int((lower + upper) / 2)
                # Return mid item if it is item
                if self[mid] == item:
                    index = mid
                    found = True
                else:
                    count += 1
                    if item < self[mid]:    # Search on the lower part of the list only
                        upper = mid - 1
                    else:
                        lower = mid + 1     # Search the upper part of the list
        
            return {'count': count, 'index': index}

        else:
            # if item not found in list
            index = -1
            found = True

            return {'count': count, 'index': index}
                        

