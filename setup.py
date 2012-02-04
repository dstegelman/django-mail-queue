from setuptools import setup, find_packages

version = '1.1.0'

setup(name='django-mail-queue',
      version=version,
      description="Simple Mail Queuing for Django",
      long_description="Mail Queueing for Django",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='django-mail-queue',
      author='Derek Stegelman',
      author_email='dstegelman@gmail.com',
      url='http://github.com/dstegelman/django-mail-queue',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
    )
