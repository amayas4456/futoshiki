import twitter
import yaml
import tempfile

def get_config():
    with open('config.yaml') as ymlfile:
        return yaml.load(ymlfile) # TODO: add param Loader=xxx

def get_api():
    cfg = get_config()

    api = twitter.Api(consumer_key=cfg['twitter']['consumer_key'],
                    consumer_secret=cfg['twitter']['consumer_secret'],
                    access_token_key=cfg['twitter']['access_token_key'],
                    access_token_secret=cfg['twitter']['access_token_secret'])
    return api

def tweet_pic(image):
    """Tweet the given pic
    
    Arguments:
        image {PIL.Image} -- Pillow Image object
    
    Returns:
        string -- Info of the created tweet
    """    
    api = get_api()

    # TODO: surely there must be a better way of doing this...
    with tempfile.NamedTemporaryFile() as fp: # This only works on Unix-based systems
        image.save(fp, format='PNG')
        return api.PostUpdate('Puzzle of the day', fp)
