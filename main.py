from os import listdir
import time
from re import sub
from search_and_download import search_and_download

query = input("Write your search words : ")
num_query = input("How many images? : ")
directory = input("In which directory (absolute path or relative to calling directory)? : ")
print(f"Images will be save to {directory}")

search_and_download(search_term=query, driver_path="chromedriver",
                    target_path=directory, number_images=int(num_query))

time.sleep(5)


def snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
                s.replace('-', ' '))).split()).lower()


files = listdir(directory + "/" + snake_case(query))
print("")
print("-----------------------------------------------------------------------------")
print("")
print(f"Successfully downloaded {len(files)} to {directory}")
print("")
