# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(
    name="TrebuchetTrigger",
    version="0.5.5",
    packages=find_packages(),
    install_requires=['GitPython>=0.3.2.RC1', 'PyYAML>=3.10', 'redis>=2.4.9', 'salt'],

    author="Ryan Lane",
    author_email="ryan@ryandlane.com",
    description="An extendable git interface to trebuchet.",
    license="apache2",
    url="https://github.com/trebuchet-deploy/trigger",

    entry_points={
        'console_scripts': [
            'git-trigger = trigger.shell:main',
            'git-deploy = trigger.shell:main',
            'trigger-submodule-update = trigger.utils.submodule_update:main',
        ],
    },
)
