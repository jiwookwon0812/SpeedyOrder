import queue
import CList

class Q:
    def __init__(self):
        self.queue = CList.CList()
        self.count = 0
    
    def enqueue(self, item):
        self.queue.insert_front(item)
        self.count += 1
        return
    
    def dequeue(self):
        if (self.count > 0):
            self.count -= 1
            cnode = self.queue.delete_back()
            return cnode.item
        return None
    
    def dequeue_target(self, target):
        if (self.count > 0):
            self.count -= 1
            cnode = self.queue.search_target(target)
            self.queue.delete_target(target)
            return cnode.item
        return None

    def size(self):
        return self.count
    
    def print_queue(self):
        self.queue.print_head()


# test_queue = Q()
# test_queue.enqueue(("qwe",1))

# test_queue.print_queue()
# test_queue.dequeue_target(1)
# test_queue.print_queue()

# q = Q()
# q.enqueue(['치즈버거', 43])
# q.enqueue(['아이스크림', 56])
# q.print_queue()
# print(q.dequeue_target(43))
# q.print_queue()