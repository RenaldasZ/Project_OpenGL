from core.base import Base

# test input functions
class Test(Base):

    def initialize(self):
        print("Initializing program...")

    def update(self):

        # debug printing
        # if len(self.input.keyDownList) > 0:
        #     print("Keys down: ", self.input.keyDownList)
        
        # if len(self.input.keyPressedList) > 0:
        #     print("Keys pressed: ", self.input.keyPressedList)
        
        # if len(self.input.keyUpList) > 0:
        #     print("Keys up: ", self.input.keyUpList)

        # typical usage
        if self.input.isKeyDown("space"):
            print("Hello!")

# instatiate and run
Test().run()
