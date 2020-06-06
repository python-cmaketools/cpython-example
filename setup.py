from cmaketools import setup

setup(
    name="cpython_example",
    version="0.0.1",
    author="Takeshi (Kesh) Ikuma",
    author_email="tikuam@gmail.com",
    description="A test package using CPython",
    url="https://github.com/python-cmaketools/cpython-example.git",
    license="MIT License",
    src_dir="src",
    ext_module_hint=r"Python3_add_library",
    has_package_data=False,
    install_requires=["cmaketools"]
)
