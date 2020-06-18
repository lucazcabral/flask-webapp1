# -*- coding: UTF-8 -*-

class Jogo:
    def __init__(
            self,
            ano: int = None,
            nome: str = '',
            categoria: str = '',
            publicador: str = '',
            console: str = ''
    ):
        self.__ano = ano
        self.__nome = nome
        self.__categoria = categoria
        self.__publicador = publicador
        self.__console = console
        print(str(self))

    def __str__(self):
        return f'{self.nome} / {self.publicador} ({self.categoria})'

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, valor: int) -> None:
        self.__ano = valor

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str) -> None:
        self.__nome = valor

    @property
    def categoria(self) -> str:
        return self.__categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        self.__categoria = valor

    @property
    def publicador(self) -> str:
        return self.__publicador

    @publicador.setter
    def publicador(self, valor: str) -> None:
        self.__publicador = valor

    @property
    def console(self) -> str:
        return self.__console

    @console.setter
    def console(self, valor: str) -> None:
        self.__console = valor