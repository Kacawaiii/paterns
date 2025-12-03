"""
Hyperloop Pattern Implementation
A reactive, event-driven pattern for handling data flow in a continuous loop
"""

from typing import Callable, Any, List, Optional
from collections import deque
import time


class HyperloopPattern:
    """
    Hyperloop Pattern: A continuous event loop that processes data reactively.
    This pattern is useful for high-throughput, event-driven architectures.
    """
    
    def __init__(self, name: str = "Hyperloop"):
        self.name = name
        self.pipeline: List[Callable] = []
        self.queue = deque()
        self.running = False
        
    def add_stage(self, processor: Callable[[Any], Any]) -> 'HyperloopPattern':
        """Add a processing stage to the pipeline"""
        self.pipeline.append(processor)
        return self
    
    def push(self, data: Any) -> None:
        """Push data into the hyperloop queue"""
        self.queue.append(data)
    
    def process(self, data: Any) -> Any:
        """Process data through all stages in the pipeline"""
        result = data
        for stage in self.pipeline:
            result = stage(result)
        return result
    
    def run_once(self) -> Optional[Any]:
        """Process one item from the queue"""
        if self.queue:
            data = self.queue.popleft()
            result = self.process(data)
            return result
        return None
    
    def start(self, max_iterations: int = None) -> None:
        """Start the hyperloop processing"""
        self.running = True
        iterations = 0
        
        while self.running:
            if max_iterations and iterations >= max_iterations:
                break
                
            if self.queue:
                self.run_once()
                iterations += 1
            else:
                time.sleep(0.01)  # Prevent busy waiting
                
    def stop(self) -> None:
        """Stop the hyperloop"""
        self.running = False


# Example usage and demonstration
if __name__ == "__main__":
    # Create a hyperloop pattern instance
    hyperloop = HyperloopPattern("DataProcessor")
    
    # Add processing stages
    hyperloop.add_stage(lambda x: x * 2)  # Stage 1: Double the value
    hyperloop.add_stage(lambda x: x + 10)  # Stage 2: Add 10
    hyperloop.add_stage(lambda x: f"Result: {x}")  # Stage 3: Format
    
    # Push data
    hyperloop.push(5)
    hyperloop.push(10)
    hyperloop.push(15)
    
    # Process data
    print("Processing data through hyperloop...")
    for i in range(3):
        result = hyperloop.run_once()
        print(result)
