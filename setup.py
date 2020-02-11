import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sirg",
    version="0.0.1",
    author="Christopher Fichtlscherer",
    author_email="fichtlscherer@mailbox.org",
    description="Running SIR on random graphs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPL",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
