class Birb:
    """
    This is borb.
    """

    def __init__(self):
        self.noise = "CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAW"
        pass

    def screech(self):
        """
        Birb go reeeeeeeeeeeeeeee.
        """
        print(self.noise)


def floof(birb: Birb) -> None:
    """
    It floofs
    """
    print("Good birb")
