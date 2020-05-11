import logging

from testrail import Testrail


class TestSection:
    def test_get_sections(self, project, suite, section):
        sections = Testrail.sections()
        sections.get(project_id=project.id, suite_id=suite.id)

        assert sections[0].id

    def test_get_section(self, section):
        get_section = Testrail.section()
        get_section.get(section_id=section.id)
        assert get_section.id

    def test_add_section(self, section):
        assert section.id

    def test_update_section(self, section, test_section_data):
        updated_section_data = test_section_data['updated']

        section.name = updated_section_data['name']
        section.update()

        assert section.name == updated_section_data['name']

    def test_delete_section(self, section):
        deleted_section = section.delete()

        assert deleted_section.status_code == 200
