class Single:
    """
    The context of the Singleton
    """
    
    def __init__(self, **vars) -> None:
        for name, value in vars.items():
            setattr(self, name, value)