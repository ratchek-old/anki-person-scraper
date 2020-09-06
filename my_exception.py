class noVboxError(Exception):
    '''Raised when the wikipedia page doesn't have a vbox, so scraping won't work'''
    pass


class noPicError(Exception):
    '''Raised when couldn't find a picture in the vbox, so scraping won't work'''
    pass
