# CONCEPT
# Blockchain consists of blocks, which consist of transactions.
# Blocks are connected through "hashing", which are unique digital fingerprints


import hashlib

#Hashing example

hash = hashlib.sha256("random transaction".encode()).hexdigest()
#print(hash)

#Hash returns "a06ceafb52852b5089ef0134d6814231ef401b2c45faf5f7bf3b0c115ef1d0e0" instead of "initial transaction"

from block import Block

blockchain = []

genesis_block = Block("Initial Hash", ["Andrew sent 3 BTC to Ralph", "Sam sent 5 BTC to Mary", "George sent 2 BTC to William" ])

#Each new block will get a different hash, and making any sort of changes to the block will generate a completely different hash"

new_block = Block(genesis_block.block_hash, ["Brad sent 10 BTC to Jason", "Jack sent 4 BTC to Anne"])

print("Block hash: Genesis Block")
print(genesis_block.block_hash)

print("Block hash: New Block")
print(new_block.block_hash)