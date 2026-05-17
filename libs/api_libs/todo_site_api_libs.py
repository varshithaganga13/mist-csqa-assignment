import logging
from datetime import datetime
from libs.api_libs.constants import api_constants
from utils.api_utils.api_utils import CommonAPIUtils


class SiteAPILibs:
    """
    Class that holds the Site API CRUD operations.
    Follows the same pattern as OrgAPILibs.
    """

    def _build_url(self, env, path):
        """Build full API URL from environment and path."""
        return api_constants.CONST_EXT_API_URLs[env] + path

    def create_random_site_name(self):
        """Generate a unique site name using the current timestamp."""
        return "Automation Site " + str(datetime.now())[0:16]

    def _op_create_site(self, env, org_id):
        logging.info("{} :: Creating a new Site in Org {}".format(self.__class__.__name__, org_id))
        url = self._build_url(env, api_constants.CONST_API_ORG_SITES.format(org_id))
        site_data = {"name": self.create_random_site_name()}
        response = CommonAPIUtils().post_request_with_status_code_validation(url, site_data, 200)
        logging.info("{} :: Site created with ID {}".format(self.__class__.__name__, response.get('id')))
        return response

    def _op_get_site(self, env, site_id):
        logging.info("{} :: Getting details for Site {}".format(self.__class__.__name__, site_id))
        url = self._build_url(env, api_constants.CONST_API_SITE_DETAILS.format(site_id))
        return CommonAPIUtils().get_request_with_status_code_validation(url, 200)

    def _op_update_site(self, env, site_id, payload):
        logging.info("{} :: Updating Site {} with payload {}".format(self.__class__.__name__, site_id, payload))
        url = self._build_url(env, api_constants.CONST_API_SITE_DETAILS.format(site_id))
        return CommonAPIUtils().put_request_with_status_code_validation(url, payload, 200)

    def _op_delete_site(self, env, site_id):
        logging.info("{} :: Deleting Site {}".format(self.__class__.__name__, site_id))
        url = self._build_url(env, api_constants.CONST_API_SITE_DETAILS.format(site_id))
        CommonAPIUtils().delete_request_with_status_code_validation(url, 200)

    def _is_site_present(self, env, org_id, site_id):
        logging.info("{} :: Checking if Site {} exists in Org {}".format(self.__class__.__name__, site_id, org_id))
        url = self._build_url(env, api_constants.CONST_API_ORG_SITES.format(org_id))
        sites = CommonAPIUtils().get_request_with_status_code_validation(url, 200)
        return any(site['id'] == site_id for site in sites)