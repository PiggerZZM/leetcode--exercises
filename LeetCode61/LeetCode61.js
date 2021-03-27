var rotateRight = function(head, k) {
  if(head == null){
    return head
  }
  let h = new ListNode(0)
  h.next = head
  let right = head
  let left = head
  let index = 0
  let length = 0
  while(right!=null){
    length += 1
    right= right.next
  }
  right = head
  k = k % length
  while(right.next != null){
    if(index >= k){
      left = left.next
    }
    right = right.next
    index += 1
  }

  right.next = h.next
  h.next = left.next
  left.next = null
  return h.next

};