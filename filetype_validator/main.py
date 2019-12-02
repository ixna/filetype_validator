import filetype
import os

def determine_extension(file_object):
    file_name = ""
    try:
        file_name = file_object.name or file.object.filename
    except AttributeError:
        # we'll try parse from file name if file_object is string
        pass
    else:
        # return read pointer to initial so buffered reader object 
        # can be re-read on caller side
        file_object.seek(0)
    
    if not file_name and type(file_object) == str:
        file_name = os.path.basename(file_object)

    file_ext = os.path.splitext(file_name)[-1]
    return file_ext.replace(".", "")

def compare(extension, mime):
    # only check files that have extensions 
    if extension:


def validate(file_object):
    # get mime type from header signature information
    # extensions for corresponsing header signature reference
    # https://en.wikipedia.org/wiki/List_of_file_signatures
    extension = determine_extension(file_object)
    mime = filetype.guess_extension(file_object)

    return compare(extension, mime)
