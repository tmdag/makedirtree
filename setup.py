from setuptools import setup

setup(name='makedirtree',
      version='0.2',
      description='helper for making directory structures',
      url='https://github.com/tmdag/makedirtree',
      author='Albert Szostkiewicz',
      author_email='tmdag@tmdag.com',
      license='MIT',
      packages=['makedirtree'],
      dependency_links=['http://github.com/tmdag/jsonParser'],
      install_requires=['jsonparser',],
      zip_safe=False)