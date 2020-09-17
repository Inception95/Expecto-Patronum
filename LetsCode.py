# Question: Given a linked list, swap every two adjacent nodes and return its head. (not modify the value, only nodes itself may be changed)

def swapPairs(self, head: ListNode):
  """Check if the linked list is None or only one node"""
  if not head or not head.next:
    return head
  """create a head before head"""
  dummy = cur = ListNode(0)
  dummy.next = head
  
  while cur.next and cur.next.next:
    """Link the second node to dummy first, and link the third node to first node, and link the first to second"""
    """Get 1st and 2nd nodes"""
    first = cur.next
    sec = cur.next.next
    """reverse, so head to 1st changes to head to 2nd"""
    cur.next = sec
    """connect 3rd to 1st, and re-connect 2nd to 1st(different order now)"""
    first.next = sec.next
    sec.next = first
    cur = cur.next.next # iterate every two nodes
  return dummy.next


# Given the root of a binary tree, return the number of uni-value subtrees.

class Solution:
  def countUnivalSubtrees(self, root: TreeNode) -> int:
    self.count = 0
    self.is_valid_part(root, 0)
    return self.count
  
  def is_valid_part(self, node, val):
    
    #base case
    if node is None: return True
    
    # check all children
    if not all([self.is_valid_part(node.left, node.val),
                self.is_valid_part(node.right, node.val)]): #?https://stackoverflow.com/questions/19389490/how-do-pythons-any-and-all-functions-work
      return False
    
    # if passed the check, count once
    self.count += 1
    
    return node.val == val
