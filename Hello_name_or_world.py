def hello(name= ''):
    if len(name) is 0:
        return ('Hello, World!')
    else:
        return ('Hello, ' + name.capitalize() + '!' )
    