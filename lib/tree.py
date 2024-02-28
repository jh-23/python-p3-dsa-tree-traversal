class Tree:
  def __init__(self, root = None):
    self.root = root
    
    

  def get_element_by_id(self, id):
    return self.dfs(self.root, id)
  
  def dfs(self, node, target_id):
    if node['id'] == target_id:
      return node
    
    for child in node['children']:
      result = self.dfs(child, target_id)
      if result:
          return result
        
    return None
