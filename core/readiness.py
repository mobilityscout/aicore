def analyze(structure):

    return {
        "dirs_count": len(structure["dirs"]),
        "files_count": len(structure["files"]),
        "status": "SCANNED"
    }
