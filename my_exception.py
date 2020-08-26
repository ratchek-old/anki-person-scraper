class noVboxError(Exception):
    '''Raised when the wikipedia page doesn't have a vbox, so scraping won't work'''
    pass
