from setuptools import setup

setup(name='Anonymization_Toolbox',
      version="0.0.1",
      description='A Python Module to anonymize',
      long_description='A Python Module to anonymize',
      url='https://github.com/seralouk/Anonymization_Toolbox',
      author='Serafeim Loukas',
      author_email='seralouk@hotmail.com',
      license='MIT',
      packages=['Anonymous'],
      install_requires=[
          'pandas','numpy'  ],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
      ],
      zip_safe=False)
