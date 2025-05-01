class Grand_father:

    def cart(self):

        print('Grand father car')


class Father(Grand_father):

    def carto(self):

        print('Fathers car')


class Son(Father):
    def cartoon(self):
        pass


test = Son()
test.cart()



