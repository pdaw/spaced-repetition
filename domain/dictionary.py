from typing import List
from domain.exception import DomainException


class UnsupportedLanguageException(DomainException):
    pass


class Language:
    __name = None  # type: str
    __supported_languages = ['en']

    def __init__(self, name: str):
        if name in self.__supported_languages:
            self.__name = name
        else:
            raise UnsupportedLanguageException

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return NotImplemented


class WordDefinition:
    __definition = None  # type: str

    def __init__(self, definition: str):
        self.__definition = definition

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return NotImplemented

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

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return NotImplemented

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
            if existing_definition == definition:
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
            if existing_word == word:
                return True

        return False
