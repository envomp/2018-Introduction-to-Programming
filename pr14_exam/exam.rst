PR14 Exam
========

Gitis: pr14_exam/exam.py

Näidiseksami 3p ülesanded (10tk).

Mall
----

.. code-block:: python

    def swap_items(dic: dict) -> dict:
        """
        Given a dictionary return a new dictionary where keys and values are swapped.
        If duplicate keys in the new dictionary exist, leave the first one.

        {"a": 1, "b": 2, "c": 3} => {1: "a", 2: "b", 3: "c"}
        {"Morning": "Good", "Evening": "Good"} => {"Good": "Morning"}

        :param dic: original dictionary
        :return: dictionary where keys and values are swapped
        """
        pass


    def find_divisors(number) -> list:
        """
        The task is to find all the divisors for given number in range to the given number's value.
        Divisor - a number that divides evenly into another number.
        Return list of given number divisors in ascending order.
        NB! Numbers 1 and number itself must be excluded if there are more divisors
        than 1 and number itself!
        (138) > [2, 3, 6, 23, 46, 69]
        (3) > [1, 3]
        :param number: int
        :return: list of number divisors
        """
        pass

    def sum_of_multiplies(first_num, second_num, limit) -> int:
        """
        The task is to find all the multiplies of each given of two numbers within the limit.
        Then, find the sum of those multiplies.
        (3, 5, 20) => 98
        :param first_num: first number
        :param second_num: second number
        :param limit: limit
        :return: sum of multiplies
        """
        pass

    def count_odds_and_evens(numbers: list) -> str:
        """
        The task is to count how many odd and even numbers does the given list contain.
        Result should be displayed as string "ODDS: {number of odds}
                                              EVENS: {number of evens}"

        :param numbers: list
        :return: str
        """
        pass

    def sum_between_25(numbers: list) -> int:
        """
        Return the sum of the numbers in the array.
        Ignore sections of numbers starting with a 2 and extending to the next 5.
        [2, 1, 7, 3, 5] => 0
        [1, 2, 3, 4, 5, 6, 2, 8, 9, 5, 1] => 8
        :param numbers: list
        :return:
        """
        pass


    def transcribe(dna_strand: str):
        """
        Write a function that returns a transcribed RNA strand from the given DNA strand,
        that is formed by replacing each nucleotide(character) with its complement: G => C, C => G, T => A, A => U
        Return None if it is not possible to transcribe a DNA strand

        "ACGTGGTCTTAA" => "UGCACCAGAAUU"
        "gcu" => None

        :param dna_strand: original DNA strand
        :return: transcribed RNA strand in the uppercase or None
        """
        pass

    def union_of_dict(d1: dict, d2: dict):
        """
        Given two dictionaries return dictionary that has all the key-value pairs that are the same in given dictionaries.

        union_of_dict({"a": 1, "b": 2, "c":3}, {"a": 1, "b": 42}) ==> {"a": 1}
        union_of_dict({}, {"bar": "foo"}) => {}
        """
        pass

    def reserve_list(input_strings: list) -> list:
         """
         Given list of strings, return new reversed list where each list element is
         reversed too. Do not reverse strings followed after element "python". If element is "java" -
         reverse mode is on again.
         P.S - "python" and "java" are not being reversed

         ['apple', 'banana', 'onion'] -> ['noino', 'ananab', 'elppa']
         ['lollipop', 'python', 'candy'] -> ['candy', 'python', 'popillol']
         ['sky', 'python', 'candy', 'java', 'fly'] -> ['ylf', 'java', 'candy', 'python', 'yks']
         ['sky', 'python', 'java', 'candy'] -> ['ydnac', 'java', 'python', 'yks']

         :param input_strings: list of strings
         :return: reversed list
         """
         pass

    def convert_binary_to_decimal(binary_list: list):
        """
        Extract binary codes of given length from list and convert to decimal numbers.

        [0, 0, 0, 0] => 0.
        [0, 1, 0, 0] => 4.

        :param binary_list: list of 1 and 0 (binary code)
        :return: number converted into decimal system
        """
        pass

    def print_pages(pages: str) -> list:
        """
        Find pages to print in console.

        examples:
        print_pages("2,4,9") -> [2, 4, 9]
        print_pages("2,4-7") -> [2, 4, 5, 6, 7]
        print_pages("2-5,7,10-12,17") -> [2, 3, 4, 5, 7, 10, 11, 12, 17]
        print_pages("1,1") -> [1]
        print_pages("2,1") -> [1, 2]

        :param pages: string containing page numbers and page ranges to print.
        :return: list of pages to print with no duplicates, sorted in increasing order.
        """
        pass
