"""
Information Architecture (IA) Pattern
A pattern for organizing and structuring information in a systematic way
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class IANode:
    """Represents a node in the information architecture"""
    id: str
    title: str
    content: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    children: List['IANode'] = field(default_factory=list)
    parent: Optional['IANode'] = None
    
    def add_child(self, child: 'IANode') -> 'IANode':
        """Add a child node"""
        child.parent = self
        self.children.append(child)
        return child
    
    def get_path(self) -> List[str]:
        """Get the path from root to this node"""
        path = []
        current = self
        while current:
            path.insert(0, current.title)
            current = current.parent
        return path
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert node to dictionary representation"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'metadata': self.metadata,
            'children': [child.to_dict() for child in self.children]
        }


class InformationArchitecture:
    """
    Information Architecture Pattern: Organizes content hierarchically
    Useful for content management systems, navigation structures, and knowledge bases
    """
    
    def __init__(self, root_title: str = "Root"):
        self.root = IANode(id="root", title=root_title)
        self.nodes: Dict[str, IANode] = {"root": self.root}
        
    def add_node(self, node_id: str, title: str, parent_id: str = "root", 
                 content: Optional[str] = None, metadata: Optional[Dict] = None) -> IANode:
        """Add a node to the information architecture"""
        if node_id in self.nodes:
            raise ValueError(f"Node with id '{node_id}' already exists")
        
        parent = self.nodes.get(parent_id)
        if not parent:
            raise ValueError(f"Parent node '{parent_id}' not found")
        
        node = IANode(
            id=node_id,
            title=title,
            content=content,
            metadata=metadata or {}
        )
        parent.add_child(node)
        self.nodes[node_id] = node
        return node
    
    def get_node(self, node_id: str) -> Optional[IANode]:
        """Get a node by its ID"""
        return self.nodes.get(node_id)
    
    def find_nodes(self, title: str) -> List[IANode]:
        """Find nodes by title"""
        return [node for node in self.nodes.values() if node.title == title]
    
    def get_structure(self) -> Dict[str, Any]:
        """Get the complete structure as a dictionary"""
        return self.root.to_dict()
    
    def print_tree(self, node: Optional[IANode] = None, level: int = 0) -> None:
        """Print the tree structure"""
        if node is None:
            node = self.root
        
        indent = "  " * level
        print(f"{indent}{node.title} ({node.id})")
        
        for child in node.children:
            self.print_tree(child, level + 1)


# Example usage
if __name__ == "__main__":
    # Create an information architecture
    ia = InformationArchitecture("Knowledge Base")
    
    # Add top-level categories
    ia.add_node("patterns", "Design Patterns", "root")
    ia.add_node("architecture", "Architecture", "root")
    
    # Add sub-categories
    ia.add_node("creational", "Creational Patterns", "patterns")
    ia.add_node("behavioral", "Behavioral Patterns", "patterns")
    ia.add_node("structural", "Structural Patterns", "patterns")
    
    # Add specific patterns
    ia.add_node("singleton", "Singleton Pattern", "creational", 
                content="Ensures a class has only one instance")
    ia.add_node("observer", "Observer Pattern", "behavioral",
                content="Defines a one-to-many dependency between objects")
    ia.add_node("hyperloop", "Hyperloop Pattern", "behavioral",
                content="A reactive, event-driven continuous processing pattern")
    
    # Print the structure
    print("Information Architecture Structure:")
    ia.print_tree()
