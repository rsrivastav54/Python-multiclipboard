import clipboard
import sys
import json

SAVED_DATA = "clipboard.json"


def write_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if(len(sys.argv) == 2):
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    if(command == 'save'):
        key = input("Enter key to save data :")
        data[key] = clipboard.paste()
        write_data(SAVED_DATA, data)
        print("Data saved!")
    elif(command == 'load'):
        key = input("Enter key to search for data :")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("No such key found")
    elif(command == 'list'):
        print(data)
    else:
        print("Unknown Command")
else:
    print("You entered more than 1 arguments")
