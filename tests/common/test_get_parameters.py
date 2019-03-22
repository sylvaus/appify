import sys
from unittest import TestCase

from appify.common.get_parameters import get_parameter_default_annotations


class TestGetParameters(TestCase):
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

    def test_get_parameters_single_param_str_default(self):
        def func(a="ab"):
            pass

        parameter_infos = get_parameter_default_annotations(func)
        self.assertListEqual(["a"], list(parameter_infos.keys()))
        self.assertEqual("a", parameter_infos["a"].name)
        self.assertEqual("ab", parameter_infos["a"].default)

    def test_get_parameters_single_param_str_annotation(self):
        if sys.version_info[0] <= 2:
            return

        def func(a:str):
            pass

        parameter_infos = get_parameter_default_annotations(func)
        self.assertListEqual(["a"], list(parameter_infos.keys()))
        self.assertEqual("a", parameter_infos["a"].name)
        self.assertEqual("str", parameter_infos["a"].type)

    def test_get_parameters_single_param_str_annotation_str_default(self):
        if sys.version_info[0] <= 2:
            return

        def func(a:str = "ab"):
            pass

        parameter_infos = get_parameter_default_annotations(func)
        self.assertListEqual(["a"], list(parameter_infos.keys()))
        self.assertEqual("a", parameter_infos["a"].name)
        self.assertEqual("str", parameter_infos["a"].type)
        self.assertEqual("ab", parameter_infos["a"].default)

    def test_get_parameters_multiple_params_no_default(self):
        def func(a, a_b, T_test_param, underscore_):
            pass

        parameter_infos = get_parameter_default_annotations(func)
        self.assertListEqual(["a", "a_b", "T_test_param", "underscore_"],
                             list(parameter_infos.keys()))
        self.assertEqual("a", parameter_infos["a"].name)
        self.assertEqual("a_b", parameter_infos["a_b"].name)
        self.assertEqual("T_test_param", parameter_infos["T_test_param"].name)
        self.assertEqual("underscore_", parameter_infos["underscore_"].name)

    def test_get_parameters_multiple_params_defaults(self):
        def func(a, a_b=12.5, T_test_param="abcd", underscore_=123):
            pass

        parameter_infos = get_parameter_default_annotations(func)
        self.assertListEqual(["a", "a_b", "T_test_param", "underscore_"],
                             list(parameter_infos.keys()))
        self.assertEqual("a", parameter_infos["a"].name)
        self.assertEqual(None, parameter_infos["a"].default)
        self.assertEqual("a_b", parameter_infos["a_b"].name)
        self.assertEqual(12.5, parameter_infos["a_b"].default)
        self.assertEqual("T_test_param", parameter_infos["T_test_param"].name)
        self.assertEqual("abcd", parameter_infos["T_test_param"].default)
        self.assertEqual("underscore_", parameter_infos["underscore_"].name)
        self.assertEqual(123, parameter_infos["underscore_"].default)

    def test_get_parameters_multiple_params_defaults_annotations(self):
        if sys.version_info[0] <= 2:
            return

        def func(a, a_b=12.5, T_test_param:str="abcd", underscore_:int=123):
            pass

        parameter_infos = get_parameter_default_annotations(func)
        self.assertListEqual(["a", "a_b", "T_test_param", "underscore_"],
                             list(parameter_infos.keys()))
        self.assertEqual("a", parameter_infos["a"].name)
        self.assertEqual(None, parameter_infos["a"].default)
        self.assertEqual(None, parameter_infos["a"].type)
        self.assertEqual("a_b", parameter_infos["a_b"].name)
        self.assertEqual(12.5, parameter_infos["a_b"].default)
        self.assertEqual(None, parameter_infos["a_b"].type)
        self.assertEqual("T_test_param", parameter_infos["T_test_param"].name)
        self.assertEqual("abcd", parameter_infos["T_test_param"].default)
        self.assertEqual("str", parameter_infos["T_test_param"].type)
        self.assertEqual("underscore_", parameter_infos["underscore_"].name)
        self.assertEqual(123, parameter_infos["underscore_"].default)
        self.assertEqual("int", parameter_infos["underscore_"].type)
