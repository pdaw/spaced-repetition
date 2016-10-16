from typing import List
from domain.exception import DomainException


class Language:
    __name = None  # type: str

    def __init__(self, name: str):
        self.__name = name


class WordDefinition:
    __definition = None  # type: str

    def __init__(self, definition: str):
        self.__definition = definition

    def get_definition(self) -> str:
        return self.__definition


class DefinitionAlreadyExistsException(DomainException):
    pass


class Word:
    __name = None  # type: str
    __language = None  # type: Language
    __definitions = []  # type: List[WordDefinition]

    def __init__(self, name: str, language: Language):
        self.__name = name
        self.__language = language

    def get_name(self) -> str:
        return self.__name

    def add_definition(self, word_definition: WordDefinition):
        if self.__is_definition_duplicated(word_definition):
            raise DefinitionAlreadyExistsException(
                "Definition {0} for word {1} already exists".format(
                    word_definition.get_definition(),
                    self.__name
                )
            )

        self.__definitions.append(word_definition)

    def __is_definition_duplicated(self, definition: WordDefinition) -> bool:
        if not self.__definitions:
            return False

        for existing_definition in self.__definitions:
            if existing_definition.get_definition() is definition.get_definition():
                return True

        return False


class WordInPhraseAlreadyExistsException(DomainException):
    pass


class Phrase:
    __name = None  # type: str
    __language = None  # type: Language
    __words = []  # type: List[Word]

    def __init__(self, name: str, language: Language):
        self.__name = name
        self.__language = language
        self.__words = []

    def add_word(self, word: Word):
        if self.__is_word_duplicated(word):
            raise WordInPhraseAlreadyExistsException(
                "Word {0} in phrase {1} already exists".format(
                    word.get_name(), self.__name
                )
            )

        self.__words.append(word)

    def __is_word_duplicated(self, word: Word) -> bool:
        if not self.__words:
            return False

        for existing_word in self.__words:
            if existing_word.get_name() is word.get_name():
                return True

        return False