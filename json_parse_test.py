import json
import unittest
from json_parse import json_parse


class JsonParseTest(unittest.TestCase):
    def test_sample(self):
        struct = "TestcaseStructure.json"
        val = "Values.json"
        json_parse(struct, val)
        with open("StructureWithValues.json", "r") as output_file:
            output = json.load(output_file)
        with open("StructureWithValuesSample.json", "r") as sample_file:
            sample = json.load(sample_file)
        self.assertDictEqual(output, sample, "Пример из задания")
    def test_error(self):
        struct = "TestcaseStructureWithErrors.json"
        val = "Values.json"
        json_parse(struct, val)
        with open("error.json", "r") as sample_file:
            error = json.load(sample_file)
        self.assertIsNotNone(error,"Должен формироваться файл с описанием ошибки")
    def test_empty_values(self):
        struct = "TestcaseStructure.json"
        val = "Empty.json"
        json_parse(struct, val)
        with open("StructureWithValues.json", "r") as output_file:
            output = json.load(output_file)
        with open(struct, "r") as sample_file:
            sample = json.load(sample_file)
        self.assertDictEqual(output, sample, "Пустые значения не меняют файл")
    def test_values_no_param(self):
        struct = "TestcaseStructure.json"
        val = "ValuesNoParam.json"
        json_parse(struct, val)
        with open("StructureWithValues.json", "r") as output_file:
            output = json.load(output_file)
        with open(struct, "r") as sample_file:
            sample = json.load(sample_file)
        self.assertDictEqual(output, sample, "Если мы не можем найти параметр с id из файла Values.json, то считаем, что такого параметра нет и значение подставлять некуда")
    def test_values_no_value(self):
        struct = "TestcaseStructureNoValue.json"
        val = "ValuesNoValue.json"
        json_parse(struct, val)
        with open("StructureWithValues.json", "r") as output_file:
            output = json.load(output_file)
        with open(struct, "r") as sample_file:
            sample = json.load(sample_file)
        self.assertDictEqual(output, sample, "Если у параметра с id из Values.json, в массиве values нет объекта с id равным value, то считаем, что такого значения нет и оставляем поле value пустым.")

if __name__ == '__main__':
    unittest.main()
