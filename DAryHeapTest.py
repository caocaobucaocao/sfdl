import DAryHeap
from test_util import build_random_list
from random import randint

heap = DAryHeap.DAryHeap(build_random_list(), randint(2, 4))
heap.build_max_d_heap_by_insert()
print(heap)
heap.d_heap_check()
res = heap.heap_delete(3)
heap.d_heap_check()
if res:
    print(res)
