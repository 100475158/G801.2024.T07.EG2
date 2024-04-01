#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "G801.2024.T07.EG2"
default_task = "publish"


@init
def initialize(project):
    project.build_depends_on("coverage")

    project.set_property("dir_source_unittest_python", "src/test/python")
    project.set_property("unittest_module_glob", "*_tests")
def set_properties(project):
    pass
