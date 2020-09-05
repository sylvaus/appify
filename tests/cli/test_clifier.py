from appify.cli import Clifier


def test_clifier_should_work_for_functions_taking_zero_parameters():
    return_value = 123457854587

    def zero_args():
        return return_value

    cli = Clifier(zero_args)
    assert return_value == cli.run([])


def test_clifier_should_work_for_functions_taking_multiple_positional_parameters():
    def three_args(a, b, c):
        """
        :type a: str
        :type b: int
        :type c: int
        """
        return "{0} = {1}".format(a, b + c)

    cli = Clifier(three_args)
    assert three_args("result", 1, 2) == cli.run(["result", "1", "2"])
