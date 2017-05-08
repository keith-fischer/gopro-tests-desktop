



class scrapeAccessible():
    def __init__(self, app):
        self.ap = app
        self.test = []
        self.ui = {}
        self.action_node = None
        self.action_attrib_name = None
        self.action_attrib_value = None
        self.validate_node = None