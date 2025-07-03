class MyClass:

    # metodo publico
    def registry(self) -> None:
        print("Start Process")
        self.__verify()
        self.__verify_registry()
        self.__insert_data()
        print("End Process")

    # metodo privado
    def __verify(self) -> None:
        print("Verify data")

    def __verify_registry(self) -> None:
        print("Verify registry")

    def __insert_data(self) -> None:
        print("Insert DB")


obj = MyClass()
obj.registry()
