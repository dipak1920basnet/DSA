def is_sorted(self):
    # empty linked list is considered sorted
    if not self.head:
        return True
    
    current = self.head

    while current.next:
        if current.data > current.next.data:
            return False
        
        current = current.next
    
    return True

