#!/usr/bin/python
#-*- coding:utf-8 -*-

import unittest
import operators


class OperatorsTests(unittest.TestCase):

	def test_add(self):
		self.assertEquals(5, operators.add(2, 3))

	def test_mul(self):
		self.assertEquals(14, operators.mul(5, 3))
