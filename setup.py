# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by `poetry run pymedphys dev propagate`

from setuptools import setup

package_dir = {"": "lib"}

packages = [
    "pymedphys",
    "pymedphys._base",
    "pymedphys._data",
    "pymedphys._dev",
    "pymedphys._dicom",
    "pymedphys._dicom.anonymise",
    "pymedphys._dicom.connect",
    "pymedphys._dicom.constants",
    "pymedphys._dicom.ct",
    "pymedphys._dicom.delivery",
    "pymedphys._dicom.rtplan",
    "pymedphys._dicom.structure",
    "pymedphys._dicom.utilities",
    "pymedphys._electronfactors",
    "pymedphys._experimental",
    "pymedphys._experimental.autosegmentation",
    "pymedphys._experimental.chartchecks",
    "pymedphys._experimental.fileformats",
    "pymedphys._experimental.fileformats.mapcheck",
    "pymedphys._experimental.fileformats.mephysto",
    "pymedphys._experimental.fileformats.profiler",
    "pymedphys._experimental.film",
    "pymedphys._experimental.paulking",
    "pymedphys._experimental.pedromartinez",
    "pymedphys._experimental.pedromartinez.oncentra",
    "pymedphys._experimental.pedromartinez.utils",
    "pymedphys._experimental.pinnacle",
    "pymedphys._experimental.plancomplexity",
    "pymedphys._experimental.pseudonymisation",
    "pymedphys._experimental.quickcheck",
    "pymedphys._experimental.serviceplans",
    "pymedphys._experimental.streamlit",
    "pymedphys._experimental.streamlit.apps",
    "pymedphys._experimental.streamlit.apps.wlutz",
    "pymedphys._experimental.streamlit.utilities",
    "pymedphys._experimental.streamlit.utilities.dicom",
    "pymedphys._experimental.streamlit.utilities.iview",
    "pymedphys._experimental.vendor.pylinac_vendored",
    "pymedphys._experimental.vendor.pylinac_vendored.core",
    "pymedphys._experimental.wlutz",
    "pymedphys._gamma",
    "pymedphys._gamma.api",
    "pymedphys._gamma.implementation",
    "pymedphys._gamma.utilities",
    "pymedphys._icom",
    "pymedphys._imports",
    "pymedphys._imports.slow",
    "pymedphys._losslessjpeg",
    "pymedphys._metersetmap",
    "pymedphys._metersetmap.delivery",
    "pymedphys._metersetmap.plt",
    "pymedphys._mocks",
    "pymedphys._monaco",
    "pymedphys._mosaiq",
    "pymedphys._streamlit",
    "pymedphys._streamlit.apps",
    "pymedphys._streamlit.apps.metersetmap",
    "pymedphys._streamlit.server",
    "pymedphys._streamlit.utilities",
    "pymedphys._trf",
    "pymedphys._trf.decode",
    "pymedphys._trf.manage",
    "pymedphys._utilities",
    "pymedphys._utilities.algorithms",
    "pymedphys._utilities.constants",
    "pymedphys._utilities.filehash",
    "pymedphys._utilities.transforms",
    "pymedphys._vendor",
    "pymedphys._vendor.apipkg",
    "pymedphys.beta",
    "pymedphys.cli",
    "pymedphys.cli.experimental",
    "pymedphys.docs",
    "pymedphys.docs.theme",
    "pymedphys.experimental",
    "pymedphys.tests",
    "pymedphys.tests.coordinates",
    "pymedphys.tests.delivery",
    "pymedphys.tests.dicom",
    "pymedphys.tests.dicom.rtplan",
    "pymedphys.tests.dicom.structure",
    "pymedphys.tests.e2e",
    "pymedphys.tests.experimental",
    "pymedphys.tests.experimental.film",
    "pymedphys.tests.experimental.mapcheck",
    "pymedphys.tests.experimental.mephysto",
    "pymedphys.tests.experimental.paulking",
    "pymedphys.tests.experimental.paulking.test_coll",
    "pymedphys.tests.experimental.pinnacle",
    "pymedphys.tests.experimental.profiler",
    "pymedphys.tests.experimental.pseudonymisation",
    "pymedphys.tests.experimental.wlutz",
    "pymedphys.tests.gamma",
    "pymedphys.tests.logfiles",
    "pymedphys.tests.logging",
    "pymedphys.tests.losslessjpeg",
    "pymedphys.tests.metersetmap",
    "pymedphys.tests.mocks",
    "pymedphys.tests.monaco",
    "pymedphys.tests.mosaiq",
    "pymedphys.tests.trf",
    "pymedphys.tests.utilities",
]

package_data = {
    "": ["*"],
    "pymedphys._experimental": ["serviceplans/templates/*", "streamlit/apps/data/*"],
    "pymedphys.docs": [
        "_static/*",
        "app/*",
        "app/ref/*",
        "cli/*",
        "cli/ref/*",
        "contrib/*",
        "contrib/other/*",
        "contrib/setups/*",
        "general/*",
        "img/*",
        "lib/*",
        "lib/background/*",
        "lib/howto/*",
        "lib/howto/gamma/*",
        "lib/howto/tunnels/*",
        "lib/howto/tunnels/img/*",
        "lib/ref/*",
        "lib/ref/experimental/*",
        "lib/tutes/*",
        "trees/*",
    ],
    "pymedphys.tests": [
        "dicom/data/rtplan/*",
        "dicom/scratch/*",
        "e2e/cypress/*",
        "e2e/cypress/fixtures/.gitignore",
        "e2e/cypress/integration/streamlit/*",
        "e2e/cypress/plugins/*",
        "e2e/cypress/support/*",
        "experimental/mephysto/data/baselines/*",
        "experimental/mephysto/data/measurements/*",
    ],
}

install_requires = ["typing-extensions"]

extras_require = {
    "comparables": ["flashgamma"],
    "dev": [
        "tqdm",
        "attrs",
        "watchdog",
        "keyring",
        "packaging",
        "PyYAML",
        "requests",
        "python-dateutil",
        "matplotlib",
        "scipy",
        "Pillow",
        "imageio",
        "xarray",
        "pymssql",
        "sqlalchemy",
        "natsort",
        "tomlkit",
        "pynetdicom",
        "pylibjpeg-libjpeg",
        "dbfread",
        "xmltodict",
        "timeago",
        "xlsxwriter",
        "plotly",
        "dicompyler-core",
        "numpy>=1.20.2",
        "pandas>=1.0.0",
        "pydicom>=2.0.0",
        "shapely>=1.7.0",
        "scikit-image>=0.18.1",
        "streamlit==0.78.0",
        "streamlit-ace==0.0.4",
        "streamlit-analytics==0.1.2",
        "pylinac==2.3.2",
        "scikit-learn",
        "fsspec",
        "sphinx-argparse",
        "sphinxcontrib-napoleon",
        "sphinx-book-theme",
        "networkx",
        "jupyter-book>=0.8.3",
        "pytest",
        "pytest-sugar",
        "hypothesis<6",
        "psutil",
        "pylint",
        "pytest-rerunfailures",
        "pre-commit",
        "black>=20.8b1,<21.0",
        "mypy",
        "rope",
        "doc8",
        "readme-renderer",
        "tabulate",
    ],
    "dicom": ["pynetdicom", "pylibjpeg-libjpeg", "pydicom>=2.0.0"],
    "docs": [
        "sphinx-argparse",
        "sphinxcontrib-napoleon",
        "sphinx-book-theme",
        "networkx",
        "jupyter-book>=0.8.3",
    ],
    "doctests": [
        "pylinac==2.3.2",
        "sphinx-book-theme",
        "black>=20.8b1,<21.0",
        "tabulate",
    ],
    "icom": ["numpy>=1.20.2"],
    "mosaiq": ["pymssql", "sqlalchemy", "pandas>=1.0.0", "scikit-learn"],
    "propagate": ["tomlkit", "black>=20.8b1,<21.0"],
    "tests": [
        "python-dateutil",
        "pytest",
        "pytest-sugar",
        "hypothesis<6",
        "psutil",
        "pylint",
        "pytest-rerunfailures",
    ],
    "user": [
        "tqdm",
        "attrs",
        "watchdog",
        "keyring",
        "packaging",
        "PyYAML",
        "requests",
        "python-dateutil",
        "matplotlib",
        "scipy",
        "Pillow",
        "imageio",
        "xarray",
        "pymssql",
        "sqlalchemy",
        "natsort",
        "tomlkit",
        "pynetdicom",
        "pylibjpeg-libjpeg",
        "dbfread",
        "xmltodict",
        "timeago",
        "xlsxwriter",
        "plotly",
        "dicompyler-core",
        "numpy>=1.20.2",
        "pandas>=1.0.0",
        "pydicom>=2.0.0",
        "shapely>=1.7.0",
        "scikit-image>=0.18.1",
        "streamlit==0.78.0",
        "streamlit-ace==0.0.4",
        "streamlit-analytics==0.1.2",
        "pylinac==2.3.2",
        "scikit-learn",
        "fsspec",
    ],
}

entry_points = {
    "console_scripts": ["pymedphys = pymedphys.__main__:main"],
    "sphinx.html_themes": ["sphinx_pymedphys_theme = pymedphys.docs.theme"],
}

setup_kwargs = {
    "name": "pymedphys",
    "version": "0.36.1",
    "description": "Medical Physics library",
    "long_description": "|logo|\n\n.. |logo| image:: https://github.com/pymedphys/pymedphys/raw/ca501275227f190a77e641a75af925d9070952b6/lib/pymedphys/docs/_static/pymedphys_title.svg\n    :target: https://docs.pymedphys.com/\n\n.. START_OF_DOCS_IMPORT\n\n**A community effort to develop an open standard library for Medical Physics\nin Python. We build high quality, transparent software together via peer review\nand open source distribution. Open code is better science.**\n\n|online-app| |build| |pypi| |python| |license|\n\n.. |online-app| image:: https://img.shields.io/github/workflow/status/pymedphys/pymedphys/OnlineApp?event=schedule&label=online-app\n    :target: https://app.pymedphys.com\n\n.. |build| image:: https://img.shields.io/github/workflow/status/pymedphys/pymedphys/Library\n    :target: https://github.com/pymedphys/pymedphys/actions\n\n.. |pypi| image:: https://img.shields.io/pypi/v/pymedphys\n    :target: https://pypi.org/project/pymedphys/\n\n.. |python| image:: https://img.shields.io/pypi/pyversions/pymedphys\n    :target: https://pypi.org/project/pymedphys/\n\n.. |license| image:: https://img.shields.io/pypi/l/pymedphys\n    :target: https://choosealicense.com/licenses/apache-2.0/\n\n\nWhat is PyMedPhys?\n==================\n\nPyMedPhys is an open-source Medical Physics python library built by an open\ncommunity that values and prioritises code sharing, review, improvement, and\nlearning from each other. It is inspired by the collaborative work of our\nphysics peers in astronomy and the `Astropy Project`_. PyMedPhys is available\non `PyPI`_ and `GitHub`_.\n\n.. _`Astropy Project`: http://www.astropy.org/\n.. _`PyPI`: https://pypi.org/project/pymedphys/\n.. _`GitHub`: https://github.com/pymedphys/pymedphys\n\nBeta level of development\n*************************\n\nPyMedPhys is currently within the ``beta`` stage of its life-cycle. It will\nstay in this stage until the version number leaves ``0.x.x`` and enters\n``1.x.x``. While PyMedPhys is in ``beta`` stage, **no API is guaranteed to be\nstable from one release to the next.** In fact, it is very likely that the\nentire API will change multiple times before a ``1.0.0`` release. In practice,\nthis means that upgrading ``pymedphys`` to a new version will possibly break\nany code that was using the old version of pymedphys. We try to be abreast of\nthis by providing details of any breaking changes from one release to the next\nwithin the `Release Notes`_.\n\nCommunity\n**************\n\nPyMedPhys has a `Discourse community <https://pymedphys.discourse.group/>`_\nto both help you find your feet using PyMedPhys and to facilitate collaboration\nand general discussion. Please reach out over there and we'd love to get to\nknow you!\n\nDocumentation\n=============\n\nThe PyMedPhys documentation is split into five categories:\n\n1. `App Users Guide`_: for those who only wish to use ready-made PyMedPhys\n   tools.\n2. `Library Users Guide`_: for those building their own Python apps, scripts\n   and other tools who wish to incorporate elements of the PyMedPhys library.\n3. `CLI Users Guide`_: for those who wish to use PyMedPhys' ready-made command\n   line interface (e.g. to help automate existing workflows with minimal\n   programming).\n4. `Contributors Guide`_: for those who wish to make new contributions to\n   either the PyMedPhys library or the PyMedPhys app.\n5. `General`_: Material that may apply to any visitor to PyMedPhys.\n\n\nOur Team\n========\n\nPyMedPhys is what it is today due to its maintainers and contributors, both past\nand present. Here is our team.\n\nMaintainers\n***********\n\n* `Simon Biggs`_\n    * `Riverina Cancer Care Centre`_, Australia\n\n.. _`Simon Biggs`: https://github.com/SimonBiggs\n\n* `Stuart Swerdloff`_\n    * `ELEKTA Pty Ltd`_: New Zealand\n\n.. _`Stuart Swerdloff`: https://github.com/sjswerdloff\n\n* `Matthew Jennings`_\n    * `Royal Adelaide Hospital`_, Australia\n\n.. _`Matthew Jennings`: https://github.com/Matthew-Jennings\n\n\n|rccc| |sjs| |rah|\n\nActive contributors\n****************************\n\n* `Phillip Chlap`_\n    * `University of New South Wales`_, Australia\n    * `Ingham Institute`_, Australia\n\n.. _`Phillip Chlap`: https://github.com/pchlap\n\n* `Derek Lane`_\n    * `ELEKTA AB`_, Houston TX\n\n.. _`Derek Lane`: https://github.com/dg1an3\n\n* `Jake Rembish`_\n    * `UT Health San Antonio`_, USA\n\n.. _`Jake Rembish`: https://github.com/rembishj\n\n* `Matthew Cooper`_\n\n.. _`Matthew Cooper`: https://github.com/matthewdeancooper\n\n* `Pedro Martinez`_\n    * `University of Calgary`_, Canada\n    * `Tom Baker Cancer Centre`_, Canada\n\n.. _`Pedro Martinez`: https://github.com/peterg1t\n\n* `Rafael Ayala`_\n    * `Hospital General Universitario Gregorio Marañón`_, Spain\n\n.. _`Rafael Ayala`: https://github.com/ayalalazaro\n\n\n|uth| |uoc| |hgugm|\n\n\nPast contributors\n****************************\n\n* `Matthew Sobolewski <https://github.com/msobolewski>`_\n* `Paul King <https://github.com/kingrpaul>`_\n* `Jacob McAloney <https://github.com/JacobMcAloney>`_\n\n\n.. |rccc| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/rccc_200x200.png\n    :target: `Riverina Cancer Care Centre`_\n\n.. |rah| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/gosa_200x200.png\n    :target: `Royal Adelaide Hospital`_\n\n.. |uoc| image:: https://github.com/pymedphys/pymedphys/raw/363b544281aab282a56b297dc8fdd521233c6a63/logos/uoc_200x200.png\n    :target: `University of Calgary`_\n\n.. |uth| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/UTHSA_logo.png\n    :target: `UT Health San Antonio`_\n\n.. |hgugm| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/HGUGM_200x200.png\n    :target: `Hospital General Universitario Gregorio Marañón`_\n\n.. |sjs| image:: https://github.com/pymedphys/pymedphys/raw/7e9204656e0468b0843533472553a03a99387386/logos/swerdloff.png\n    :target: `Swerdloff Family`_\n\n.. _`Riverina Cancer Care Centre`: https://www.riverinacancercare.com.au/\n\n.. _`ELEKTA Pty Ltd`: https://www.elekta.com/\n\n.. _`ELEKTA AB`: https://www.elekta.com/\n\n.. _`Royal Adelaide Hospital`: https://www.rah.sa.gov.au/\n\n.. _`University of New South Wales`: https://www.unsw.edu.au/\n\n.. _`South Western Sydney Local Health District`: https://www.swslhd.health.nsw.gov.au/\n\n.. _`Anderson Regional Cancer Center`: https://www.andersonregional.org/services/cancer-care/\n\n.. _`Northern Beaches Cancer Care`: https://www.northernbeachescancercare.com.au/\n\n.. _`University of Calgary`: https://www.ucalgary.ca/\n\n.. _`Tom Baker Cancer Centre`: https://www.ahs.ca/tbcc\n\n.. _`UT Health San Antonio`: https://www.uthscsa.edu/academics/biomedical-sciences/programs/radiological-sciences-phd\n\n.. _`Hospital General Universitario Gregorio Marañón`: https://www.comunidad.madrid/hospital/gregoriomaranon/\n\n.. _`Swerdloff Family`: https://github.com/sjswerdloff\n\n.. _`Ingham Institute`: https://inghaminstitute.org.au/\n\n.. END_OF_DOCS_IMPORT\n\n.. _`Release Notes`: ./CHANGELOG.md\n\n.. _`Library Users Guide`: https://docs.pymedphys.com/lib/index.html\n.. _`CLI Users Guide`: https://docs.pymedphys.com/cli/index.html\n.. _`App Users Guide`: https://docs.pymedphys.com/app/index.html\n.. _`Contributors Guide`: https://docs.pymedphys.com/contrib/index.html\n.. _`General`: https://docs.pymedphys.com/general/index.html\n",
    "author": "PyMedPhys Contributors",
    "author_email": "developers@pymedphys.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://pymedphys.com",
    "package_dir": package_dir,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "extras_require": extras_require,
    "entry_points": entry_points,
    "python_requires": ">=3.7,<4.0",
}


setup(**setup_kwargs)
