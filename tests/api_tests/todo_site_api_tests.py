import pytest
import logging
from libs.api_libs.todo_site_api_libs import SiteAPILibs
from libs.api_libs.org_api_libs import OrgAPILibs

site_obj = SiteAPILibs()
org_obj = OrgAPILibs()


class TestSiteAPI:
    """
    Test class for Site API CRUD operations.
    Follows the same pattern as TestOrgAPI.
    """

    org_id = ""  # Class variable for Org ID
    site_id = ""  # Class variable for Site ID

    def test_01_create_site(self, env):
        """
        Test to create a site via API and validate it exists.
        Creates a parent org first since sites belong to orgs.
        """
        logging.info("###################   IN TEST METHOD test_01_create_site ################")

        # Create a parent org (sites require an org)
        org = org_obj._op_create_org(env)
        TestSiteAPI.org_id = org['id']

        # Create a site inside that org
        site = site_obj._op_create_site(env, TestSiteAPI.org_id)
        TestSiteAPI.site_id = site['id']

        assert site_obj._is_site_present(env, TestSiteAPI.org_id, TestSiteAPI.site_id)

    def test_02_update_site(self, env):
        """
        Test to update a site name via API and validate the response.
        """
        logging.info("###################   IN TEST METHOD test_02_update_site ################")

        site_payload = {"name": site_obj.create_random_site_name()}
        updated = site_obj._op_update_site(env, TestSiteAPI.site_id, site_payload)

        assert updated['name'] == site_payload['name']

    def test_03_delete_site(self, env):
        """
        Test to delete a site via API and validate it no longer exists.
        Also cleans up the parent org.
        """
        logging.info("###################   IN TEST METHOD test_03_delete_site ################")

        site_obj._op_delete_site(env, TestSiteAPI.site_id)
        assert not site_obj._is_site_present(env, TestSiteAPI.org_id, TestSiteAPI.site_id)

        # Cleanup: delete the parent org
        org_obj._op_delete_org(env, TestSiteAPI.org_id)