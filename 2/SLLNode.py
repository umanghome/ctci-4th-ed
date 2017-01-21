class Node (object):
  def __init__ (self, value):
    self.value = value
    self.next = None

  def append_to_tail (self, value):
    node = Node(value)
    n = self
    while n.next is not None:
      n = n.next
    n.next = node

  def print_from_node (self):
    n = self
    while True:
      print (n.value)
      if n.next is None:
        break
      n = n.next

def delete_node (head, value, once = True):
  if head.value == value:
    return head.next
  n = head
  while True:
    if n.next is None:
      break
    if n.next.value == value:
      n.next = n.next.next
      if once:
        break
    else:
      n = n.next
  return head

head = Node('a')
head.append_to_tail('b')
head.append_to_tail('c')
head.append_to_tail('d')
head.append_to_tail('c')
head.append_to_tail('e')
head.append_to_tail('c')
head.print_from_node()
print '\n\n';
head = delete_node(head, 'c')
head.print_from_node()