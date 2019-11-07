from setuptools import setup

#bring in __version__ from sourcecode
#per https://stackoverflow.com/a/17626524
#and https://stackoverflow.com/a/2073599

with open('cappy/version.py') as ver:
    exec(ver.read())

setup(name='cappy',
      version=__version__,
      description='The redcap api you build yourself',
      url='http://github.com/pfwhite/cappy',
      author='Patrick White',
      author_email='pfwhite9@gmail.com',
      license='Apache License 2.0',
      packages=['cappy'],
      include_package_data=True,
      install_requires=[
          'requests',
          'pyyaml'],
      zip_safe=False)
