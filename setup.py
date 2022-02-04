import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='commons',
    version='0.0.1',
    author='Manikandan Rajendran',
    author_email='manikandan.rajendran@betwaygroup.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ManikandanRajendran/commons',
    project_urls = {
        "Bug Tracker": "https://github.com/ManikandanRajendran/commons/issues"
    },
    packages=['commons'],
    install_requires=['requests'],
)
