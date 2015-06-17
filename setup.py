from setuptools import setup, find_packages

setup(name='kanboard',
      version='0.1',
      description='kanboard API python client',
      author='Alexander Rudakov',
      author_email='freekoder@gmail.com',
      url='https://github.com/freekoder/kanboard-py',
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          ],
      keywords='kanboard API',
      install_requires=['requests'],
      packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'examples'])
      )
