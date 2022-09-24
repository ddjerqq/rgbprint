import setuptools

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name="rgbprint",
    version="4.0.1",
    license="GNU",
    author="ddjerqq",
    author_email="ddjerqq@gmail.com",
    url="https://github.com/ddjerqq/rgbprint",
    keywords="rgb print gradient color colorama",
    description="Print colors and gradients in your terminal. Official github: https://github.com/ddjerqq/rgbprint",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=["rgbprint"],
)
