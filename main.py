from os import listdir
from re import sub
from search_and_download import search_and_download

# ----> EDIT HERE <----
# Enter the path to the chromium driver here, either absolute or relative to this file
chrome_driver_path = "chromedriver"

# CLI prompts for querying
web_text_query = input("Write your search words : ")
number_of_images_in_query = input("How many images? : ")
directory_to_save = input("In which directory should the images be saved? : ")
print(f"Images will be saved to {directory_to_save}")


search_and_download(search_term=web_text_query, driver_path=chrome_driver_path,
                    target_path=directory_to_save, number_images=int(number_of_images_in_query))


def snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
                s.replace('-', ' '))).split()).lower()


files = listdir(directory_to_save + "/" + snake_case(web_text_query))
print("")
print("-----------------------------------------------------------------------------")
print("")
print(f"Successfully downloaded {len(files)} to {directory_to_save}")
print("")
