import sys
from unittest import TestCase

if sys.version_info[0] > 2:
    from .python3_get_annotations import *


class TestGetParameterDefault(TestCase):
    def test_get_parameters_no_param(self):
        def func():
            pass

        parameter_infos = get_parameter_default_annotations(func)
        self.assertListEqual([], list(parameter_infos.keys()))

    def test_get_parameters_single_param_no_default(self):
        def func(a):
            pass

        parameter_infos = get_parameter_default_annotations(func)
        self.assertListEqual(["a"], list(parameter_infos.keys()))
        self.assertEqual("a", parameter_infos["a"].name)
        self.assertEqual(True, parameter_infos["a"].required)

    def test_get_parameters_single_param_str_default(self):
        def func(a="ab"):
            pass

        parameter_infos = get_parameter_default_annotations(func)
        self.assertListEqual(["a"], list(parameter_infos.keys()))
        self.assertEqual("a", parameter_infos["a"].name)
        self.assertEqual("ab", parameter_infos["a"].default)
        self.assertEqual(False, parameter_infos["a"].required)

    def test_get_parameters_multiple_params_no_default(self):
        def func(a, a_b, T_test_param, underscore_):
            pass

        parameter_infos = get_parameter_default_annotations(func)
        self.assertListEqual(["a", "a_b", "T_test_param", "underscore_"],
                             list(parameter_infos.keys()))
        self.assertEqual("a", parameter_infos["a"].name)
        self.assertEqual(True, parameter_infos["a"].required)
        self.assertEqual("a_b", parameter_infos["a_b"].name)
        self.assertEqual(True, parameter_infos["a_b"].required)
        self.assertEqual("T_test_param", parameter_infos["T_test_param"].name)
        self.assertEqual(True, parameter_infos["T_test_param"].required)
        self.assertEqual("underscore_", parameter_infos["underscore_"].name)
        self.assertEqual(True, parameter_infos["underscore_"].required)

    def test_get_parameters_multiple_params_defaults(self):
        def func(a, a_b=12.5, T_test_param="abcd", underscore_=123):
            pass

        parameter_infos = get_parameter_default_annotations(func)
        self.assertListEqual(["a", "a_b", "T_test_param", "underscore_"],
                             list(parameter_infos.keys()))
        self.assertEqual("a", parameter_infos["a"].name)
        self.assertEqual(NoDefault, parameter_infos["a"].default)
        self.assertEqual(True, parameter_infos["a"].required)
        self.assertEqual("a_b", parameter_infos["a_b"].name)
        self.assertEqual(12.5, parameter_infos["a_b"].default)
        self.assertEqual(False, parameter_infos["a_b"].required)
        self.assertEqual("T_test_param", parameter_infos["T_test_param"].name)
        self.assertEqual("abcd", parameter_infos["T_test_param"].default)
        self.assertEqual(False, parameter_infos["T_test_param"].required)
        self.assertEqual("underscore_", parameter_infos["underscore_"].name)
        self.assertEqual(123, parameter_infos["underscore_"].default)
        self.assertEqual(False, parameter_infos["underscore_"].required)

    def test_get_parameters_multiple_params_no_default_method(self):
        class TmpClass:
            def tmp(self, a, a_b, T_test_param, underscore_):
                pass
        inst = TmpClass()
        func = inst.tmp

        parameter_infos = get_parameter_default_annotations(func)
        self.assertListEqual(["a", "a_b", "T_test_param", "underscore_"],
                             list(parameter_infos.keys()))
        self.assertEqual("a", parameter_infos["a"].name)
        self.assertEqual(True, parameter_infos["a"].required)
        self.assertEqual("a_b", parameter_infos["a_b"].name)
        self.assertEqual(True, parameter_infos["a_b"].required)
        self.assertEqual("T_test_param", parameter_infos["T_test_param"].name)
        self.assertEqual(True, parameter_infos["T_test_param"].required)
        self.assertEqual("underscore_", parameter_infos["underscore_"].name)
        self.assertEqual(True, parameter_infos["underscore_"].required)

