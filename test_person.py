import pytest
from person import Person

class TestPerson:

    @pytest.fixture
    def person(self):
        return Person('Max', 2000)

    def test_person_init(self, person):
        assert person.name == 'Max'
        assert person.birth_year  == 2000

    def test_persons_address(self, person):
        person.address = 'Musterort'
        assert person.address == 'Musterort'

    def test_person_print(self, person, capsys):
        person.address = 'Testadresse'
        print(person)
        captured = capsys.readouterr()
        assert captured.out == 'Person: Max\n\tAlter :   2000\n\tAdresse : Testadresse\n'