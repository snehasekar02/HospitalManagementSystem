class PatientNumberNotFoundException(Exception):
    """Exception raised when an invalid patient ID is encountered"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
