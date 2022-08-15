class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"
        
        
def max_value(items, capacity):
    """The maximum value achievable with a given list of items and a given
       knapsack capacity."""
    n = len(items)
    matrix = [[0 for i in range(capacity + 1)] for i in range (n + 1)]
    items_used = {}
    #Runs through the grid
    for index in range(n + 1):
        for value in range(capacity + 1):
            if index == 0 or value == 0:
                matrix[index][value] = 0
                #Elif, move back the index
            elif items[index - 1].weight <= value:
                maximum = max(items[index - 1].value + matrix[index - 1][value - items[index - 1].weight]
                , matrix[index - 1][value])
                matrix[index][value] = maximum
                #items_used.append(maximum)
            else:
                matrix[index][value] = matrix[index - 1][value]
                #items_used.append(matrix[index - 1][value])
    
    result = matrix[n][capacity]
    
    #Studying the range function is interesting innit?
    for index in range(n, 0, -1):
        if result <= 0:
            break
            #Destroy
        elif result != matrix[index - 1][value]:
            #Continue is a keyword? WHERE HAS IT BEEN ALL MY LIFE!?
            #Item isn't there
            #Interesting
            items_used[items[index-1]] = items[index-1].weight
            result = result - items[index - 1].value
            value = value - items[index - 1].weight
        
    items_used = list(items_used.keys())
    return matrix[n][capacity], items_used

# The example in the lecture notes
items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
maximum = max_value(items, 10)
print(maximum)

