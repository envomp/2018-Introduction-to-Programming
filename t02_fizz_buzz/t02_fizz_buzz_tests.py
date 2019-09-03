def run_introduction_script(runner, value="abc"):
    script_name = "t02.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python3.7', script_name, stdin=io.StringIO(value), cwd=working_dir)
    return script

input_prefix4 = "Mati\n7\n8\n" + "1\n4\n"

def _test_fizz_buzz(script_runner, nr):
    result = run_introduction_script(script_runner, input_prefix4 + str(nr))
    expected = str(nr)
    if nr % 15 == 0:
        expected = "FizzBuzz"
    elif nr % 3 == 0:
        expected = "Fizz"
    elif nr % 5 == 0:
        expected = "Buzz"
    assert result.stdout.find(f"FizzBuzz for number {nr} is: {expected}") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__ask_fizz_buzz_number(script_runner):
    result = run_introduction_script(script_runner, input_prefix4)
    assert result.stdout.find("Enter a FizzBuzz number:") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__fizz_buzz_number_when_fizz(script_runner):
    _test_fizz_buzz(script_runner, 3)
    _test_fizz_buzz(script_runner, 6)
    _test_fizz_buzz(script_runner, 9)
    _test_fizz_buzz(script_runner, 39969)

@pytest.mark.script_launch_mode('subprocess')
def test__fizz_buzz_number_when_buzz(script_runner):
    _test_fizz_buzz(script_runner, 5)
    _test_fizz_buzz(script_runner, 10)
    _test_fizz_buzz(script_runner, 20)
    _test_fizz_buzz(script_runner, 124385)


@pytest.mark.script_launch_mode('subprocess')
def test__fizz_buzz_number_when_fizzbuzz(script_runner):
    _test_fizz_buzz(script_runner, 15)
    _test_fizz_buzz(script_runner, 30)
    _test_fizz_buzz(script_runner, 45)
    _test_fizz_buzz(script_runner, 124390)


@pytest.mark.script_launch_mode('subprocess')
def test__fizz_buzz_number_when_number(script_runner):
    _test_fizz_buzz(script_runner, 1)
    _test_fizz_buzz(script_runner, 2)
    _test_fizz_buzz(script_runner, 4)
    _test_fizz_buzz(script_runner, 16)
    _test_fizz_buzz(script_runner, 7)
    _test_fizz_buzz(script_runner, 29)
    _test_fizz_buzz(script_runner, 31)
    _test_fizz_buzz(script_runner, 124391)
