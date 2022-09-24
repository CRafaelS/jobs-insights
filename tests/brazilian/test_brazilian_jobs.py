from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    expected_result = {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }
    assert (
        read_brazilian_file("tests/mocks/brazilians_jobs.csv")[0]
        == expected_result
    )
