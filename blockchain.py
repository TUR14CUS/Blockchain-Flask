from enum import Enum
from flask_restful import Resource
from flask import jsonify

class Endpoints(Enum):
    MINE_BLOCK = '/mine_block'
    GET_CHAIN = '/get_chain'
    IS_VALID = '/is_valid'

class Block:
    def __init__(self, index, timestamp, proof, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.proof = proof
        self.previous_hash = previous_hash

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = Block(index=len(self.chain) + 1,
                      timestamp=str(datetime.datetime.now()),
                      proof=proof,
                      previous_hash=previous_hash)
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

# Mining a new block
class MineBlockResource(Resource):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def get(self):
        previous_block = self.blockchain.get_previous_block()
        previous_proof = previous_block.proof
        proof = self.blockchain.proof_of_work(previous_proof)
        previous_hash = self.blockchain.hash(previous_block)
        block = self.blockchain.create_block(proof, previous_hash)
        response = {
            'message': 'Congratulations, you just mined a block!',
            'index': block.index,
            'timestamp': block.timestamp,
            'proof': block.proof,
            'previous_hash': block.previous_hash
        }
        return jsonify(response), 201
    
# Getting the full Blockchain
class BlockchainResource(Resource):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def get(self):
        response = {'chain': [vars(block) for block in self.blockchain.chain],
                    'length': len(self.blockchain.chain)}
        return jsonify(response), 200

# Checking if the Blockchain is valid
class IsValidResource(Resource):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def get(self):
        is_valid = self.blockchain.is_chain_valid(self.blockchain.chain)
        if is_valid:
            response = {'message': 'All good. The Blockchain is valid.'}
        else:
            response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
        return jsonify(response), 200