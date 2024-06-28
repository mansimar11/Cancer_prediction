import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_desciption=f.read()
    
    
__version__="0.0.0"

REPO_NAME="Cancer_prediction"
AUTHOR_NAME="mansimar11"
SRC_REPO="cancer_pred"
AUTHOR_EMAIL="mansimarsingh117@gmail.com"    


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package",
    Long_description=long_desciption,
    long_description_content="text/markdown",
    url=f"https://github.com/mansimar11/Cancer_prediction",
    project_urls={
        "Bug Tracker":f"https://github.com/mansimar11/Cancer_prediction/issues",
        
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    
    
)
    