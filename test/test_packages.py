"""Test which packages give errors when trying to document."""
import importlib
import pip
import os


def builtin_packages():
    """Test builtin packages."""
    builtin_packages = ""
    with open('../builtin_list.txt') as f:
        builtin_packages = f.readlines()
    list_builtin_errors = list()
    for i in builtin_packages:
        itm = i.strip(" ").strip("\n")
        try:
            importlib.import_module(itm)
        except:
            list_builtin_errors.append(itm)
    return list_builtin_errors


def installed_packages():
    """Test installed packages."""
    installed_packages = pip.get_installed_distributions()
    list_installed_errors = list()
    for i in installed_packages:
        itm = str(i.key)
        try:
            importlib.import_module(itm)
        except:
            list_installed_errors.append(itm)
    return list_installed_errors


def test_packages():
    """Test all packages, verbose."""
    os.system('cls')
    print("Checking builtin packages... ")
    builtin_errors = builtin_packages()
    print("Done.")
    print("Builtin Packages w/ errors:\n-------------------------")
    for err in builtin_errors:
        print(err)
    print("Checking installed packages... ")
    installed_errors = installed_packages()
    print("Done.")
    print("Installed Packages w/ errors:\n----------------------------")
    for err in installed_errors:
        print(err)
    errors = builtin_errors + installed_errors
    return errors


if __name__ == '__main__':
    test_packages()
