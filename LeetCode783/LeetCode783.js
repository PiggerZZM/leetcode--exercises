function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

function Tree(nums){
    let treeNodeList = []
    let root = new TreeNode(nums.pop(0))
    treeNodeList.push(root)
    while(treeNodeList.length > 0){
        let node = treeNodeList.pop(0)
        if(nums.length > 0){
            let num = nums.pop(0)
            if(num != null){
                node.left = new TreeNode(num)
                treeNodeList.push(node.left)
            }
        }else{
            break
        }
        if(nums.length > 0){
            let num = nums.pop(0)
            if(num != null){
                node.right = new TreeNode(num)
                treeNodeList.push(node.right)
            }
        }else{
            break
        }
    }
    return root
}

var minDiffInBST = function(root) {
  let result = 100000
  let nodeList = []
  const ds = function(root){
    if(root == null) return
    ds(root.left)
    if(nodeList.length>0){
        let num = nodeList.pop()
        if(result > Math.abs(num - root.val)){
            result = Math.abs(num - root.val)
        }
        nodeList.push(root.val)
    }else{
        nodeList.push(root.val)
    }
    ds(root.right)
  }
  ds(root)

  return result
};

let root = Tree([90,69,null,49,89,null,52])
console.log(minDiffInBST(root))
