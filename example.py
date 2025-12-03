"""
HYPRL PATERNS IA - Combined Example
Demonstrates how Hyperloop Pattern and Information Architecture Pattern work together
"""

from hyperloop_pattern import HyperloopPattern
from ia_pattern import InformationArchitecture


def main():
    """
    Example combining both patterns:
    - Use IA Pattern to organize pattern definitions
    - Use Hyperloop Pattern to process pattern queries through a pipeline
    """
    
    print("=" * 60)
    print("HYPRL PATERNS IA - Combined Pattern Example")
    print("=" * 60)
    print()
    
    # 1. Create Information Architecture for organizing patterns
    print("1. Building Information Architecture...")
    ia = InformationArchitecture("Pattern Catalog")
    
    # Add pattern categories
    ia.add_node("behavioral", "Behavioral Patterns", "root",
                content="Patterns that deal with object collaboration and responsibilities")
    ia.add_node("creational", "Creational Patterns", "root",
                content="Patterns that deal with object creation mechanisms")
    ia.add_node("structural", "Structural Patterns", "root",
                content="Patterns that deal with object composition")
    
    # Add specific patterns
    ia.add_node("hyperloop", "Hyperloop Pattern", "behavioral",
                content="Reactive event-driven continuous processing",
                metadata={"complexity": "medium", "use_case": "stream_processing"})
    
    ia.add_node("observer", "Observer Pattern", "behavioral",
                content="One-to-many dependency between objects",
                metadata={"complexity": "low", "use_case": "event_handling"})
    
    ia.add_node("singleton", "Singleton Pattern", "creational",
                content="Ensures a class has only one instance",
                metadata={"complexity": "low", "use_case": "resource_management"})
    
    print("✓ Information Architecture created")
    print()
    ia.print_tree()
    print()
    
    # 2. Create Hyperloop Pattern for processing pattern queries
    print("2. Setting up Hyperloop Pattern for query processing...")
    hyperloop = HyperloopPattern("PatternQueryProcessor")
    
    # Add processing stages
    def extract_pattern_name(query):
        """Stage 1: Extract pattern name from query"""
        return query.lower().strip()
    
    def lookup_pattern(pattern_id):
        """Stage 2: Lookup pattern in IA"""
        node = ia.get_node(pattern_id)
        return node if node else f"Pattern '{pattern_id}' not found"
    
    def format_result(node):
        """Stage 3: Format the result"""
        if isinstance(node, str):
            return node
        
        path = " > ".join(node.get_path())
        metadata = ", ".join([f"{k}={v}" for k, v in node.metadata.items()])
        return f"""
Pattern: {node.title}
Path: {path}
Content: {node.content}
Metadata: {metadata}
"""
    
    hyperloop.add_stage(extract_pattern_name)
    hyperloop.add_stage(lookup_pattern)
    hyperloop.add_stage(format_result)
    
    print("✓ Hyperloop pipeline configured with 3 stages")
    print()
    
    # 3. Process queries through the hyperloop
    print("3. Processing pattern queries through hyperloop...")
    print()
    
    queries = ["hyperloop", "singleton", "observer"]
    
    for query in queries:
        hyperloop.push(query)
    
    for i in range(len(queries)):
        result = hyperloop.run_once()
        print(f"Query Result {i+1}:")
        print(result)
        print("-" * 60)
    
    print()
    print("=" * 60)
    print("✓ HYPRL PATERNS IA Demo Complete!")
    print("=" * 60)
    print()
    print("Summary:")
    print("- Information Architecture: Organized pattern catalog hierarchically")
    print("- Hyperloop Pattern: Processed queries through reactive pipeline")
    print("- Integration: Seamless data flow between patterns")


if __name__ == "__main__":
    main()
