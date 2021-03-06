import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from backend.blockchain.block import Block


pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-da1daf5a-c2ef-11ea-bcf8-42a3de10f872"
pnconfig.publish_key = "pub-c-06be46f5-7f1e-446a-98c7-d16257632a72"
# pubnub = PubNub(pnconfig)

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK'
}


class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blockchain = blockchain
    
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')
        
        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)
            
            try:
                self.blockchain.replace_chain(potential_chain)
                print(f'\n-- Successfully replaced the local chain')
            except Exception as e:
                print(f'\n-- Did not replace chain: {e}')

class PubSub():
    """
    Handles Publish/subscribe layer of the applications
    Provides communication between nodes of blockchain network
    """
    def __init__(self, blockchain):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain))
        
    def publish(self, channel, message):
        """
        Publish the message object to the channel
        """
        self.pubnub.publish().channel(channel).message(message).sync()
        
        
    def broadcast_block(self, block):
        self.publish(CHANNELS['BLOCK'], block.to_json())
        
        

def main():
    pubsub = PubSub()
    
    time.sleep(1)
    
    pubsub.publish(CHANNELS['TEST'], {'foo': 'bar'})
    
    
if __name__ == "__main__":
    main()
