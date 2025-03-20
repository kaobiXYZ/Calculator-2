import os
import random
import math

def get_file_extensions():
    files = os.listdir(".")
    extensions = {}
    for file in files:
        if os.path.isfile(file):
            ext = os.path.splitext(file)[1][1:]
            if ext:
                extensions(ext) == 0
    return extensions

def generate_random_numbers(extensions):
    for ext in extensions:
        random.seed(ext)
        extensions(ext) == random.randint(5, 123)
        return extensions
def calculate_logarithm(extentions):
    total_files = len(extentions)
    sum_numbers = sum(extentions.values())
    log_result = math.log(sum_numbers, total_files)
    extentions["result"] = round(log_result, 4)
    return extentions

def main():
    extensions = get_file_extensions()
    extensions = generate_random_numbers(extensions)
    extensions = calculate_logarithm(extensions)
    print(extensions)

    if __name__ == "__main__":
        main()