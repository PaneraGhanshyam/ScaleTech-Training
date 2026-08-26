import json
import xml.etree.ElementTree as ET
import configparser
import yaml


with open(
    "data.json",
    "r",
    encoding="utf-8"
) as file:

    json_data = json.load(file)


print("=== JSON ===")

print(
    json_data["application"]["name"]
)

for user in json_data["users"]:
    print(
        f'{user["name"]} - '
        f'{user["role"]}'
    )




xml_tree = ET.parse("data.xml")

xml_root = xml_tree.getroot()


print("\n=== XML ===")

print(
    xml_root.find("name").text
)

for user in xml_root.find("users"):

    print(
        f'{user.find("name").text} - '
        f'{user.find("role").text}'
    )




ini_config = configparser.ConfigParser()

ini_config.read("config.ini")


print("\n=== INI ===")

print(
    ini_config["application"]["name"]
)

print(
    ini_config["database"].getint("port")
)




with open(
    "config.yaml",
    "r",
    encoding="utf-8"
) as file:

    yaml_config = yaml.safe_load(file)


print("\n=== YAML ===")

print(
    yaml_config["application"]["name"]
)

print(
    yaml_config["database"]["port"]
)

print(
    yaml_config["features"]
)