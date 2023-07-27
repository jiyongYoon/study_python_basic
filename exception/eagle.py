from exception.bird import Bird


class Eagle(Bird):

    def fly(self):
        print("very fast")


eagle = Eagle()
eagle.fly()