

class Notification(object):
    """Notification """
    def __init__(self):
        super(Notification, self).__init__()

    def notify(self,string):
        pass

class MockNotification(Notification):
    def notify(self,string):
        print("****"+string+"****")
