from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Carbonis-client",
    version="0.1.12",
    author="Carbonis",
    author_email="hello@carbonis.ai",
    description="A package for interacting with the Carbonis Service-API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Smile-Ryin/Carbon-automation",
    license="MIT",
    packages=["Carbonis_client"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["requests"],
    keywords="carbonis nlp ai language-processing",
    include_package_data=True,
)
