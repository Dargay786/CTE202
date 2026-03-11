#Task 1:
# Create a class named CustomList
class CustomList:

    # Constructor method (runs automatically when object is created)
    def __init__(self):
        # Variable to store the maximum capacity of the list
        self.capacity = 10
        
        # Underlying array (Python list) used to store elements
        self.data = [None] * self.capacity
        
        # Variable to track the current number of elements in the list
        self.current_size = 0

        # Print initial information
        print("Created new CustomList with capacity:", self.capacity)
        print("Current size:", self.current_size)


# Create an object of CustomList to test the constructor
my_list = CustomList()

#Task 2:
# Create a class named CustomList
class CustomList:

    # Constructor to initialize capacity, array, and size
    def __init__(self):
        self.capacity = 10                    # Maximum capacity of the list
        self.data = [None] * self.capacity    # Underlying array to store elements
        self.current_size = 0                 # Tracks number of elements

        print("Created new CustomList with capacity:", self.capacity)
        print("Current size:", self.current_size)

    # 1. append(element) - Add element to the end of the list
    def append(self, element):
        self.data[self.current_size] = element  # Store element at next empty position
        self.current_size += 1                  # Increase size count
        print("Appended", element, "to the list")

    # 2. get(index) - Retrieve element at a specific index
    def get(self, index):
        return self.data[index]                 # Return element at given index

    # 3. set(index, element) - Replace element at a specific index
    def set(self, index, element):
        self.data[index] = element              # Replace value at index
        print("Set element at index", index, "to", element)

    # 4. size() - Return the current number of elements
    def size(self):
        return self.current_size                # Return current size


# Testing the operations
my_list = CustomList()

my_list.append(5)
print("Element at index 0:", my_list.get(0))

my_list.set(0, 10)
print("Element at index 0:", my_list.get(0))

print("Current size:", my_list.size())