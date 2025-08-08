from setuptools import find_packages, setup

setup(
    name="trainer",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "scikit-learn",
        "pandas",
        "joblib",
        "feast",
        "google-cloud-storage"
    ],
    entry_points={"console_scripts": ["trainer=trainer.task:main"]},
)
