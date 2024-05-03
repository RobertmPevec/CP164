from functions import file_analyze
with open("t04.txt", "r", encoding="utf-8") as fh_1:
    # Call file_analyze function and pass the open file handle fh_1
    upp, low, dig, whi, rem = file_analyze(fh_1)
    # Now you can use the results as needed, maybe print them or process them further
    print(f"Uppercase: {upp}, Lowercase: {low}, Digits: {dig}, Whitespace: {whi}, Others: {rem}")
