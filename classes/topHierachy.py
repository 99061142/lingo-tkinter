class Type(type):
    def __repr__(self) -> str:
        return self.__name__ # Return the class name as a string