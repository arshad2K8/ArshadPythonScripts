__author__ = 'arshad'
import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read('filterData.txt')
print Config.sections()

print Config.options("SectionOne")
print Config.get("SectionOne", "status")


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
