class OrchidVision:


    def __init__(self):

        self.active = True



    def analyze(self, image):

        return (
            "I received an image. "
            "Vision analysis module is active."
        )


    def describe(self, image):

        return (
            "I can describe this image "
            "once the vision model is connected."
        )
