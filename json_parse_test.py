import json
import unittest
from json_parse import json_parse


class JsonParseTest(unittest.TestCase):
    def test_sample(self):
        stuct = "TestcaseStructure.json"
        val = "Values.json"
        json_parse(stuct, val)
        with open("StructureWithValues.json", "r") as output_file:
            output = json.load(output_file)
        with open("StructureWithValuesSample.json", "r") as sample_file:
            sample = json.load(sample_file)
        self.assertDictEqual(output, sample, "Пример из задания")
    def test_error(self):
        stuct = "TestcaseStructureWithErrors.json"
        val = "Values.json"
        json_parse(stuct, val)
        with open("error.json", "r") as sample_file:
            error = json.load(sample_file)
        self.assertIsNotNone(error,"Должен формироваться файл с описанием ошибки")
if __name__ == '__main__':
    unittest.main()
