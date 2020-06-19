class Usuario:
    def __init__(self,
                 id:int = None,
                 nome: str = '',
                 login: str = '',
                 senha: str = ''):
        self.__id = id
        self.__nome = nome
        self.__login = login
        self.__senha = senha


    def __str__(self) -> str:
        return f'{self.__id};' \
               f'{self.__nome};' \
               f'{self.__login};' \
               f'{self.__senha};'

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, valor: int) -> None:
        self.__id = valor

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str) -> None:
        self.__nome = valor

    @property
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, valor: str) -> None:
        self.__login = valor

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, valor: str) -> None:
        self.__senha = valor