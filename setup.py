from setuptools import setup

long_description = open("README.md").read()

setup(name='antspynet',
      version='0.2.0',
      description='A collection of deep learning architectures ported to the python language and tools for basic medical image processing.',
      long_description=long_description,
      long_description_content_type="text/markdown; charset=UTF-8; variant=GFM",
      url='https://github.com/ANTsX/ANTsPyNet',
      author='Nicholas J. Tustison and Brian B. Avants and Nick Cullen',
      author_email='ntustison@gmail.com',
      packages=['antspynet','antspynet/architectures','antspynet/utilities'],
      install_requires=[
            "antspyx",
            "keras",
            "scikit-learn",
            "tensorflow; platform_machine=='x86_64'",
            "tensorflow-aarch64; platform_machine=='x86_64'",
            "tensorflow-macos>=2.6; platform_machine == 'arm64' and sys_platform == 'darwin'",
            "tensorflow-metal>=2.6; platform_machine == 'arm64' and sys_platform == 'darwin'",
            "tensorflow-probability",
            "numpy",
            "requests",
            "statsmodels",
            "matplotlib"
            ],
      zip_safe=False)
