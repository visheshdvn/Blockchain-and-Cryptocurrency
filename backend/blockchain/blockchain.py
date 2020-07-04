from backend.blockchain.block import Block

class Blockchain():
    
    def __init__(self):
        self.chain = [Block.genesis()]
        
    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))
        
    def __repr__(self):
        return f'Blockchain: {self.chain}'
    
    def replace_chain(self, chain):
        """
        Replace the following chain with the incoming one if the following applies:
        - The incoming chain must be longer than the local one.
        - The incoming chain is formatted properly.
        """
        if len(chain) <= len(self.chain):
            raise Exception('Cannot replace. The incoming chain must be longer')
        
        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Cannot replace. The incoming chain is invalid: {e}')
        
        self.chain = chain


    @staticmethod
    def is_valid_chain(chain):
        """
        validate the incoming chain
        Enforce the following rules of the blockchain
        - the chain must start with genesis block
        - block must be formattd correctly
        """
        if chain[0] != Block.genesis():
            raise Exception('The genesis block must be valid')
        
        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)
                
        
def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')
    
    
if __name__ == "__main__":
    main()
