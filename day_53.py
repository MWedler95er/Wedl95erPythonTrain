''' SET OPERATIONS'''

class SetOperations:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def union(self):
        return self.set1.union(self.set2)

    def intersection(self):
        return self.set1.intersection(self.set2)
    
    def intersection_update(self):
        self.set1.intersection_update(self.set2)
        return self.set1

    def difference_update(self):
        self.set1.difference_update(self.set2)
        return self.set1

    def difference(self):
        return self.set1.difference(self.set2)

    def symmetric_difference(self):
        return self.set1.symmetric_difference(self.set2)
    
    def print_sets(self):
        print("Set 1:", self.set1)
        print("Set 2:", self.set2)
    
set_operations = SetOperations({1, 2, 3, 4}, {3, 4, 5, 6})
set_operations.print_sets()
print("Union:", set_operations.union())
set_operations.print_sets()
print("Intersection:", set_operations.intersection())
set_operations.print_sets()
print("Difference:", set_operations.difference())
set_operations.print_sets()
print("Symmetric Difference:", set_operations.symmetric_difference())
set_operations.print_sets()
print("Intersection Update:", set_operations.intersection_update())
set_operations.print_sets()
print("Difference Update:", set_operations.difference_update())
set_operations.print_sets()

