# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 1.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ProjectMetadata(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'public': 'str',
        'enable_content_trust': 'str',
        'prevent_vulnerable_images_from_running': 'str',
        'prevent_vulnerable_images_from_running_severity': 'str',
        'automatically_scan_images_on_push': 'str'
    }

    attribute_map = {
        'public': 'public',
        'enable_content_trust': 'enable_content_trust',
        'prevent_vulnerable_images_from_running': 'prevent_vulnerable_images_from_running',
        'prevent_vulnerable_images_from_running_severity': 'prevent_vulnerable_images_from_running_severity',
        'automatically_scan_images_on_push': 'automatically_scan_images_on_push'
    }

    def __init__(self, public=None, enable_content_trust=None, prevent_vulnerable_images_from_running=None, prevent_vulnerable_images_from_running_severity=None, automatically_scan_images_on_push=None):  # noqa: E501
        """ProjectMetadata - a model defined in Swagger"""  # noqa: E501

        self._public = None
        self._enable_content_trust = None
        self._prevent_vulnerable_images_from_running = None
        self._prevent_vulnerable_images_from_running_severity = None
        self._automatically_scan_images_on_push = None
        self.discriminator = None

        if public is not None:
            self.public = public
        if enable_content_trust is not None:
            self.enable_content_trust = enable_content_trust
        if prevent_vulnerable_images_from_running is not None:
            self.prevent_vulnerable_images_from_running = prevent_vulnerable_images_from_running
        if prevent_vulnerable_images_from_running_severity is not None:
            self.prevent_vulnerable_images_from_running_severity = prevent_vulnerable_images_from_running_severity
        if automatically_scan_images_on_push is not None:
            self.automatically_scan_images_on_push = automatically_scan_images_on_push

    @property
    def public(self):
        """Gets the public of this ProjectMetadata.  # noqa: E501

        The public status of the project. The valid values are \"true\", \"false\".  # noqa: E501

        :return: The public of this ProjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ProjectMetadata.

        The public status of the project. The valid values are \"true\", \"false\".  # noqa: E501

        :param public: The public of this ProjectMetadata.  # noqa: E501
        :type: str
        """

        self._public = public

    @property
    def enable_content_trust(self):
        """Gets the enable_content_trust of this ProjectMetadata.  # noqa: E501

        Whether content trust is enabled or not. If it is enabled, user cann't pull unsigned images from this project. The valid values are \"true\", \"false\".  # noqa: E501

        :return: The enable_content_trust of this ProjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._enable_content_trust

    @enable_content_trust.setter
    def enable_content_trust(self, enable_content_trust):
        """Sets the enable_content_trust of this ProjectMetadata.

        Whether content trust is enabled or not. If it is enabled, user cann't pull unsigned images from this project. The valid values are \"true\", \"false\".  # noqa: E501

        :param enable_content_trust: The enable_content_trust of this ProjectMetadata.  # noqa: E501
        :type: str
        """

        self._enable_content_trust = enable_content_trust

    @property
    def prevent_vulnerable_images_from_running(self):
        """Gets the prevent_vulnerable_images_from_running of this ProjectMetadata.  # noqa: E501

        Whether prevent the vulnerable images from running. The valid values are \"true\", \"false\".  # noqa: E501

        :return: The prevent_vulnerable_images_from_running of this ProjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._prevent_vulnerable_images_from_running

    @prevent_vulnerable_images_from_running.setter
    def prevent_vulnerable_images_from_running(self, prevent_vulnerable_images_from_running):
        """Sets the prevent_vulnerable_images_from_running of this ProjectMetadata.

        Whether prevent the vulnerable images from running. The valid values are \"true\", \"false\".  # noqa: E501

        :param prevent_vulnerable_images_from_running: The prevent_vulnerable_images_from_running of this ProjectMetadata.  # noqa: E501
        :type: str
        """

        self._prevent_vulnerable_images_from_running = prevent_vulnerable_images_from_running

    @property
    def prevent_vulnerable_images_from_running_severity(self):
        """Gets the prevent_vulnerable_images_from_running_severity of this ProjectMetadata.  # noqa: E501

        If the vulnerability is high than severity defined here, the images cann't be pulled. The valid values are \"negligible\", \"low\", \"medium\", \"high\", \"critical\".  # noqa: E501

        :return: The prevent_vulnerable_images_from_running_severity of this ProjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._prevent_vulnerable_images_from_running_severity

    @prevent_vulnerable_images_from_running_severity.setter
    def prevent_vulnerable_images_from_running_severity(self, prevent_vulnerable_images_from_running_severity):
        """Sets the prevent_vulnerable_images_from_running_severity of this ProjectMetadata.

        If the vulnerability is high than severity defined here, the images cann't be pulled. The valid values are \"negligible\", \"low\", \"medium\", \"high\", \"critical\".  # noqa: E501

        :param prevent_vulnerable_images_from_running_severity: The prevent_vulnerable_images_from_running_severity of this ProjectMetadata.  # noqa: E501
        :type: str
        """

        self._prevent_vulnerable_images_from_running_severity = prevent_vulnerable_images_from_running_severity

    @property
    def automatically_scan_images_on_push(self):
        """Gets the automatically_scan_images_on_push of this ProjectMetadata.  # noqa: E501

        Whether scan images automatically when pushing. The valid values are \"true\", \"false\".  # noqa: E501

        :return: The automatically_scan_images_on_push of this ProjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._automatically_scan_images_on_push

    @automatically_scan_images_on_push.setter
    def automatically_scan_images_on_push(self, automatically_scan_images_on_push):
        """Sets the automatically_scan_images_on_push of this ProjectMetadata.

        Whether scan images automatically when pushing. The valid values are \"true\", \"false\".  # noqa: E501

        :param automatically_scan_images_on_push: The automatically_scan_images_on_push of this ProjectMetadata.  # noqa: E501
        :type: str
        """

        self._automatically_scan_images_on_push = automatically_scan_images_on_push

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other