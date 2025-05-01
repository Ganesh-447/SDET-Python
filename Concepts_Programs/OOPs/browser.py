class Browser:

    def __init__(self,browser="Chrome"):
        self.browser = browser


    def openBrowser(self):
        print(f"opening the browser {self.browser}")


a=Browser()
a.openBrowser()