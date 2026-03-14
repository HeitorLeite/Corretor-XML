from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_exe_options = {
    "packages": [],
    "excludes": [],
    "include_files": []
}

base = "gui"

executables = [
    Executable("Corretor_XML.py", base=base, icon=None)
]

setup(
    name="CorretorXML",
    version="1.0",
    description="Corretor de XML TISS",
    options={"build_exe": build_exe_options},
    executables=executables
)