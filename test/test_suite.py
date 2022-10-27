#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from test.controller.test_pessoa_controller import TestPessoaController

def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPessoaController))

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    test_suite()

