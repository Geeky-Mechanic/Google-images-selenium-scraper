from os import listdir, system
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

# Prompt for handling duplicates
scan_for_duplicates = input("Would you like to scan for duplicates after scraping?([yY]/[nN]) : ")
max_distance = ""
detailed_output = ""
delete_duplicates = ""

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


def scan_images():
    dup_handling = "--on-equal quote"
    output_config = ""
    distance = 0
    if delete_duplicates == "y" or delete_duplicates == "Y":
        dup_handling = "--on-equal delete-second"
    if detailed_output == "y" or detailed_output == "Y":
        output_config = "--debug"
    try:
        if int(max_distance) >= 0:
            distance = int(max_distance)
    except ValueError:
        print("Max-distance number invalid, defaulting to 0")

    system(
        f"find-dups --progress --parallel {output_config} "
        f"--max-distance {distance} {dup_handling} root_directory {directory_to_save}")


if scan_for_duplicates == "y" or scan_for_duplicates == "Y":
    detailed_output = input("Would you like the detailed output?([yY]/[nN]) : ")
    delete_duplicates = input("Should duplicate images be deleted?([yY]/[nN]) : ")
    max_distance = input(
        "To what degree should the images be alike?(ENTER A WHOLE POSITIVE NUMBER, 0 being exact matches) : ")
    scan_images()
