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
            "gast<=0.4.0,>=0.2.1; platform_machine == 'arm64' and sys_platform == 'darwin'",
            # "keras; platform_machine=='x86_64' or platform_machine=='aarch64'",
            # "keras<2.10.0,>=2.9.0rc0; platform_machine == 'arm64' and sys_platform == 'darwin'",
            "matplotlib",
            "numpy",
            "requests",
            "scikit-learn",
            # "protobuf<3.20,>=3.9.2; platform_machine == 'arm64' and sys_platform == 'darwin'",
            "statsmodels",            
            "tensorflow; platform_machine=='x86_64' or platform_machine=='aarch64'",
            "tensorflow-macos==2.9.1; platform_machine == 'arm64' and sys_platform == 'darwin'",
            "tensorflow-metal==0.5.1; platform_machine == 'arm64' and sys_platform == 'darwin'",
            "tensorflow-probability; platform_machine=='x86_64' or platform_machine=='aarch64'",
            "tensorflow-probability==0.17.0; platform_machine == 'arm64' and sys_platform == 'darwin'"
            ],
      python_version='>=3.7,<=3.10',
      zip_safe=False)
