import pathlib
from configparser import ConfigParser


def get_configData(section, key):
    config_file_path = pathlib.Path(__file__).parent.absolute().joinpath("config.ini")
    config = ConfigParser()
    config.read(config_file_path)

    try:
        data = config[section]
    except KeyError:
        raise KeyError("Invalid section specified")
    return data[key]


def get_githubURL():
    return get_configData("BROWSER", "URL")


def get_searchText():
    return get_configData("SEARCH", "SEARCHDATA")


def get_writtenInLanguage():
    return get_configData("FORM", "LANGUAGE")


def get_inTheState():
    return get_configData("FORM", "STATE")


def get_thisManyStars():
    return get_configData("FORM", "STARS")


def get_thisManyFollowers():
    return get_configData("FORM", "FOLLOWERS")


def get_thisLicense():
    return get_configData("FORM", "LICENSE")


def get_repoName():
    return get_configData("FORM", "REPO_NAME")
