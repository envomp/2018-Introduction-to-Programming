# PR09

## Teooria

### Rekursioon

Rekursiivseteks funktsioonideks peetakse ennastkopeerivaid funktsioone ehk funktsioone, mis kutsuvad iseennast välja.

Enne ülesannete lahendamist oleks mõistlik tutvuda rekursiooniga Pydoci osakonnas: https://ained.ttu.ee/pydoc/recursion.html.

## Abimaterjalid ülesande lahendamiseks

*  Rekursioon: https://ained.ttu.ee/pydoc/recursion.html
*  Tsükkel: https://ained.ttu.ee/pydoc/loop.html
*  Sõne: https://ained.ttu.ee/pydoc/string.html

## Ülesanne

Fail Gitis: ``pr09_recursion/recursion.py``.

### Taust

Oled tudeng ja pead selle ära tegema, et 5p saada.

### Sisu

See ülesanne koosneb mitmest osast. Esimeses osas tuleb kirjuada kaks funktsiooni, mis teevad sama asja, kuid neist esimene tuleb kirjutada iteratiivselt (kasutades tsükleid) ning teine rekursiivselt. Teises osas tuleb kirjutada funktsioon, mis eemaldab etteantud sõnest numbrid ning tagastab ümberpööratud versiooni sellest sõnest. Kolmandas osas on ette antud kaks funktsiooni lahendatud kujul. Sinu ülesandeks on saada aru, mida need funktsioonid tegema peaksid ning kirjutada need ümber vastavalt rekursiiveks (esimene funktsioon) ja iteratiivseks (teine funktsioon).

``def x_sum_loop(nums, x) -> int:`` Funktsioon, mis saab ette täisarvude järjendi `nums` ja täisarvu `x`, ning tagastab listi igast x-ndast arvust koosneva summa. Siin ülesandes hakkab indekseerimine pihta ühest, mitte nullist. Ehk kui x = 0, siis on summa 0, kui x = 1, on summa listi kõikide liikmete summa ja nii edasi. Arvestada tuleb ka sellega, et x võib olla negatiivne, sel juhul tuleb numbreid hakata liitma tagantotsast alustades. Lahendus peab olema iteratiivne.

``def x_sum_recursion(nums, x) -> int:`` Funktsioon, mis saab ette täisarvude järjendi `nums` ja täisarvu `x`, ning tagastab listi igast x-ndast arvust koosneva summa. Siin ülesandes hakkab indekseerimine pihta ühest, mitte nullist. Ehk kui x = 0, siis on summa 0, kui x = 1, on summa listi kõikide liikmete summa ja nii edasi. Arvestada tuleb ka sellega, et x võib olla negatiivne, sel juhul tuleb numbreid hakata liitma tagantotsast alustades. Lahendus peab olema rekursiivne.

``def remove_nums_and_reverse(string):`` Funktsioon, mis saab ette sõne `string`, eemaldab sellest sõnest kõik numbrid, pöörab sõne ümber ning tagastab selle. Lahendus peab olema rekursiivne.

``def task1(string):`` Funktsioon, mis on lahendatud iteratiivselt. Sinu ülesandeks on aru saada, mida see funktsioon teeb ning kirjutada see ümber rekursiivseks.

``def task2(string):`` Funktsioon, mis on lahendatud rekursiivselt. Sinu ülesandeks on aru saada, mida see funktsioon teeb ning kirjutada see ümber iteratiivseks.

### Mall

    """Recursion is recursion."""
    
    
    def x_sum_loop(nums, x) -> int:
        """
        Given a list of integers and a number called x. Iteratively return sum of every x'th number in the list.
        
        In this task "indexing" starts from 1, so if x = 2 and nums = [2, 3, 4, -9], the output should be -6 (3 + -9).
        
        X can also be negative, in that case indexing starts from the end of the list, see examples below.
        
        If x is 0, the sum should be 0 as well.
    
        print(x_sum_loop([], 3))  # 0
        print(x_sum_loop([2, 5, 6, 0, 15, 5], 3))  # 11
        print(x_sum_loop([0, 5, 6, -5, -9, 3], 1))  # 0
        print(x_sum_loop([43, 90, 115, 500], -2))  # 158
        print(x_sum_loop([1, 2], -9))  # 0
        print(x_sum_loop([2, 3, 6], 5))  # 0
        print(x_sum_loop([6, 5, 3, 2, 9, 8, 6, 5, 4], 3))  # 15
        
        :param nums: list of integer
        :param x: number indicating every which num to add to sum
        :return: sum of every x'th number in the list
        """
        pass
    
    
    def x_sum_recursion(nums, x) -> int:
        """
        Given a list of integers and a number called x. Recursively return sum of every x'th number in the list.
        
        In this task "indexing" starts from 1, so if x = 2 and nums = [2, 3, 4, -9], the output should be -6 (3 + -9).
        
        X can also be negative, in that case indexing starts from the end of the list, see examples below.
        
        If x = 0, the sum should be 0 as well.
    
        print(x_sum_recursion([], 3))  # 0
        print(x_sum_recursion([2, 5, 6, 0, 15, 5], 3))  # 11
        print(x_sum_recursion([0, 5, 6, -5, -9, 3], 1))  # 0
        print(x_sum_recursion([43, 90, 115, 500], -2))  # 158
        print(x_sum_recursion([1, 2], -9))  # 0
        print(x_sum_recursion([2, 3, 6], 5))  # 0
        print(x_sum_recursion([6, 5, 3, 2, 9, 8, 6, 5, 4], 3))  # 15
        
        :param nums: list of integer
        :param x: number indicating every which num to add to sum
        :return: sum of every x'th number in the list
        """
        pass
    
    
    def remove_nums_and_reverse(string):
        """
        Recursively remove all the numbers in the string and return reversed version of that string without numbers.
        
        print(remove_nums_and_reverse("poo"))  # "oop"
        print(remove_nums_and_reverse("3129047284"))  # empty string
        print(remove_nums_and_reverse("34e34f7i8l 00r532o23f 4n5ot565hy7p4"))  # "python for life"
        print(remove_nums_and_reverse("  k 4"))  # " k  "
        
        :param string: given string to change
        :return: reverse version of the original string, only missing numbers
        """
        pass
    
    
    def task1(string):
        """
        Figure out what this code is supposed to do and rewrite it using recursion.
        
        :param string: given string
        :return: figure it out
        """
        for i in range(len(string)):
            if string[i] != str[len(string) - i - 1]:
                return False
        return True
    
    
    def task2(string):
        """
        Figure out what this code is supposed to do and rewrite it using iteration.
        
        :param string: given string
        :return: figure it out
        """
        if len(string) < 2:
            return string
        elif string[0] == string[1]:
            return string[0] + "-" + task2(string[1:])
        return string[0] + task2(string[1:])
