# python_practice NeuralCoinBlock

import hashlib

class NeuralCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
t1 = "Anna sends 2 NC to Bob"
t2 = "Bob sends 4.2 NC to Mike"
t3 = "Daniel sends 3.2 NC to Drake"
t4 = "Josh sends 0.3 NC to Anna"
t5 = "Mike sends 1 NC to Daniel"
t6 = "Drake sends 5.4 NC to Josh"

initial_block = NeuralCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(initial_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)