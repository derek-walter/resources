class MyClass:
    """
    Description of my class
    Attributes
    ----------
    None
    Methods
    -------
    None
    Examples
    --------
    >>> mc = MyClass()
    """

    def __init__(self, item: bool = True):
        pass

    def return_values(self, values: list = []):
        """
        Return your values.
        Parameters
        ----------
        values : 1D list-like
        Returns
        -------
        tuple of (values, count)
        """
        return (values, len(values))