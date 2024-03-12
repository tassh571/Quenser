# -*- coding: utf-8 -*-

from QuenserLibrary.QuenserLibrary import *


class QuenserLibrary(
            'QuenserLibrary', 
            'QuenserLibrary1'
):
	""" สวัสดีชาวโลก Hello World
	"""

	def __init__(self):
		"""test for QuenserLibrary
        """
		for base in QuenserLibrary.__bases__:
			base.__init__(self)
		