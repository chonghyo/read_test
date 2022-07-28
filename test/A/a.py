"""
====================================
 :mod:`a` module a
====================================
.. moduleauthor:: hyo156 <hyo156@kitech.re.kr>
.. note:: PSID

explanation
=====

module exam

Revision History
-------------------

 * [2022/07/22] - module cccc
"""
import numpy as np


class A:
    """testest
    """
    def __init__(self, a: int):
        """ class gener

        :param a: gener param

        >>> a = A(10)
        """
        self.a = a

    def print_value(self):
        """ a print method

        >>> A(10).print_value()
        10
        """
        print(self.a)

