import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback


pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-da1daf5a-c2ef-11ea-bcf8-42a3de10f872"
pnconfig.publish_key = "pub-c-06be46f5-7f1e-446a-98c7-d16257632a72"
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')


class PubSub():
    """
    Handles Publish/subscribe layer of the applications
    Provides communication between nodes of blockchain network
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())
        
    def publish(self, channel, message):
        """
        Publish the message object to the channel
        """
        self.pubnub.publish().channel(channel).message(message).sync()
        
        
        

def main():
    pubsub = PubSub()
    
    time.sleep(1)
    
    pubsub.publish(TEST_CHANNEL, {'foo': 'bar'})
    
    
if __name__ == "__main__":
    main()
