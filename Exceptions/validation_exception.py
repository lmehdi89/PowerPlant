class ValidationException(Exception):
    def __init__(self, property_name: str, message: str):
        super().__init__(message)
        self.property_name = property_name
