import json
import pytest

import requests

from testrail import Testrail

"""
PROJECT
"""
@pytest.fixture(scope='session')
def test_project_data():
    with open('tests/config/test_project_data.json') as stream:
        data = json.load(stream)

    return data


@pytest.fixture(scope='class')
def project(request, test_project_data):
    new_project_data = test_project_data['new']

    project = Testrail.project()
    project.name = new_project_data['name']
    project.announcement = new_project_data['announcement']
    project.show_announcement = new_project_data['show_announcement']
    project.suite_mode = new_project_data['suite_mode']
    project.add()

    def delete():
        try:
            alive = Testrail.project(project_id=project.id)
            alive.delete()
        except requests.HTTPError:
            pass

    request.addfinalizer(delete)
    return project


"""
SUITE
"""
@pytest.fixture(scope='session')
def test_suite_data():
    with open('tests/config/test_suite_data.json') as stream:
        data = json.load(stream)

    return data


@pytest.fixture(scope='class')
def suite(request, project, test_suite_data):
    new_suite_data = test_suite_data['new']

    suite = Testrail.suite()
    suite.name = new_suite_data['name']
    suite.description = new_suite_data['description']
    suite.add(project_id=project.id)

    def delete():
        try:
            alive = Testrail.suite(suite_id=suite.id)
            alive.delete()
        except requests.HTTPError:
            pass

    request.addfinalizer(delete)
    return suite


"""
SECTION
"""
@pytest.fixture(scope='session')
def test_section_data():
    with open('tests/config/test_section_data.json') as stream:
        data = json.load(stream)

    return data


@pytest.fixture(scope='class')
def section(request, suite, test_section_data):
    new_section_data = test_section_data['new']

    section = Testrail.section()
    section.name = new_section_data['name']
    section.suite_id = suite.id
    section.description = new_section_data['description']
    section.add(project_id=suite.project_id)

    def delete():
        try:
            alive = Testrail.section(section_id=section.id)
            alive.delete()
        except requests.HTTPError:
            pass

    request.addfinalizer(delete)
    return section


"""
CASE
"""
@pytest.fixture(scope='session')
def test_case_data():
    with open('tests/config/test_case_data.json') as stream:
        data = json.load(stream)

    return data


@pytest.fixture(scope='class')
def case(request, section, test_case_data):
    new_case_data = test_case_data['new']

    case = Testrail.case()
    case.title = new_case_data['title']
    case.add(section_id=section.id)

    def delete():
        try:
            alive = Testrail.case(case_id=case.id)
            alive.delete()
        except requests.HTTPError:
            pass

    request.addfinalizer(delete)
    return case


"""
MILESTONE
"""
@pytest.fixture(scope='session')
def test_milestone_data():
    with open('tests/config/test_milestone_data.json') as stream:
        data = json.load(stream)

    return data


@pytest.fixture(scope='class')
def milestone(request, project, test_milestone_data):
    new_milestone_data = test_milestone_data['new']

    milestone = Testrail.milestone()
    milestone.name = new_milestone_data['name']
    milestone.description = new_milestone_data['description']
    milestone.due_on = new_milestone_data['due_on']
    milestone.start_on = new_milestone_data['start_on']
    milestone.add(project_id=project.id)

    def delete():
        try:
            alive = Testrail.milestone(milestone_id=milestone.id)
            alive.delete()
        except requests.HTTPError:
            pass

    request.addfinalizer(delete)
    return milestone


"""
PLAN
"""
@pytest.fixture(scope='session')
def test_plan_data():
    with open('tests/config/test_plan_data.json') as stream:
        data = json.load(stream)

    return data


@pytest.fixture(scope='class')
def plan(request, project, test_plan_data):
    new_plan_data = test_plan_data['new']

    plan = Testrail.plan()
    plan.name = new_plan_data['name']
    plan.description = new_plan_data['description']
    plan.add(project_id=project.id)

    def delete():
        try:
            alive = Testrail.plan(plan_id=plan.id)
            alive.delete()
        except requests.HTTPError:
            pass

    request.addfinalizer(delete)
    return plan


"""
RUN
"""
@pytest.fixture(scope='session')
def test_run_data():
    with open('tests/config/test_run_data.json') as stream:
        data = json.load(stream)

    return data


@pytest.fixture(scope='class')
def run(request, project, suite, case, test_run_data):
    new_run_data = test_run_data['new']

    run = Testrail.run()
    run.suite_id = suite.id
    run.name = new_run_data['name']
    run.description = new_run_data['description']
    run.add(project_id=project.id)

    def delete():
        try:
            alive = Testrail.run(run_id=run.id)
            alive.delete()
        except requests.HTTPError:
            pass

    request.addfinalizer(delete)
    return run


"""
ENTRY
"""


@pytest.fixture(scope='session')
def test_entry_data():
    with open('tests/config/test_entry_data.json') as stream:
        data = json.load(stream)

    return data


@pytest.fixture(scope='class')
def entry(request, plan, run, test_entry_data):
    new_entry_data = test_entry_data['new']

    entry = Testrail.entry()
    entry.suite_id = new_entry_data['suite_id']
    entry.name = new_entry_data['name']
    entry.description = new_entry_data['description']
    entry.include_all = new_entry_data['include_all']
    entry.runs.append(run)

    def delete():
        try:
            alive = Testrail.entry(plan_id=plan.id, entry_id=entry.id)
            alive.delete()
        except requests.HTTPError:
            pass

    request.addfinalizer(delete)
    return entry

