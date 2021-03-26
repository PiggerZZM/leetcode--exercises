var deleteDuplicates = function(head) {
  if(head == null){
    return head
  }
  let p = head
  let right = head.next
  while(right != null){
    if(p.val != right.val){
      p.next = right
      p = p.next
    }
    right = right.next
  }
  p.next = right
  return head
};