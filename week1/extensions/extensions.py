# File Extension Categorizer for CS50p


# get file name from user and call function to check extension
def main():
    user_file = input("File Name: ").strip().lower()
    file_type = check_ext(user_file)
    print(file_type)


# check file extension and return category
def check_ext(file_name):
    ext = file_name.rsplit(".", 1)  # split the file into 'name' and 'ext'

    if len(ext) == 2:  # checks how many splits occured. One spilt has length 2
        # Cases for matching extension type from 'developer.mozilla.org' info
        match ext[1]:
            case "gif":
                return "image/gif"
            case "jpg":
                return "image/jpeg"
            case "jpeg":
                return "image/jpeg"
            case "png":
                return "image/png"
            case "pdf":
                return "application/pdf"
            case "txt":
                return "text/plain"
            case "zip":
                return "application/zip"
            case _:
                return "application/octet-stream"
    else:
        return "application/octet-stream"


main()
