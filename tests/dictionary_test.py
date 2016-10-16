import pytest
from domain.dictionary import Word, Language, WordDefinition, Phrase, \
    DefinitionAlreadyExistsException, WordInPhraseAlreadyExistsException


def test_raise_exception_while_adding_duplicated_definition_to_word():
    with pytest.raises(DefinitionAlreadyExistsException):
        word = Word('lint', Language('en'))
        definition = WordDefinition("short threads that come off the surface of cloth when it is being produced")
        duplicated_definition = WordDefinition(
            "short threads that come off the surface of cloth when it is being produced"
        )

        word.add_definition(definition)
        word.add_definition(duplicated_definition)


def test_raise_exception_while_adding_duplicated_word_to_phrase():
    with pytest.raises(WordInPhraseAlreadyExistsException):
        phrase = Phrase("My name is Peter", Language('en'))
        word = Word('name', Language('en'))
        duplicated_word = Word('name', Language('en'))

        phrase.add_word(word)
        phrase.add_word(duplicated_word)
