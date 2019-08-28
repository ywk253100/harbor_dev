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


class UserGroup(object):
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
        'id': 'int',
        'group_name': 'str',
        'group_type': 'int',
        'ldap_group_dn': 'str'
    }

    attribute_map = {
        'id': 'id',
        'group_name': 'group_name',
        'group_type': 'group_type',
        'ldap_group_dn': 'ldap_group_dn'
    }

    def __init__(self, id=None, group_name=None, group_type=None, ldap_group_dn=None):  # noqa: E501
        """UserGroup - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._group_name = None
        self._group_type = None
        self._ldap_group_dn = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if group_name is not None:
            self.group_name = group_name
        if group_type is not None:
            self.group_type = group_type
        if ldap_group_dn is not None:
            self.ldap_group_dn = ldap_group_dn

    @property
    def id(self):
        """Gets the id of this UserGroup.  # noqa: E501

        The ID of the user group  # noqa: E501

        :return: The id of this UserGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserGroup.

        The ID of the user group  # noqa: E501

        :param id: The id of this UserGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def group_name(self):
        """Gets the group_name of this UserGroup.  # noqa: E501

        The name of the user group  # noqa: E501

        :return: The group_name of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this UserGroup.

        The name of the user group  # noqa: E501

        :param group_name: The group_name of this UserGroup.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def group_type(self):
        """Gets the group_type of this UserGroup.  # noqa: E501

        The group type, 1 for LDAP group.  # noqa: E501

        :return: The group_type of this UserGroup.  # noqa: E501
        :rtype: int
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this UserGroup.

        The group type, 1 for LDAP group.  # noqa: E501

        :param group_type: The group_type of this UserGroup.  # noqa: E501
        :type: int
        """

        self._group_type = group_type

    @property
    def ldap_group_dn(self):
        """Gets the ldap_group_dn of this UserGroup.  # noqa: E501

        The DN of the LDAP group if group type is 1 (LDAP group).  # noqa: E501

        :return: The ldap_group_dn of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._ldap_group_dn

    @ldap_group_dn.setter
    def ldap_group_dn(self, ldap_group_dn):
        """Sets the ldap_group_dn of this UserGroup.

        The DN of the LDAP group if group type is 1 (LDAP group).  # noqa: E501

        :param ldap_group_dn: The ldap_group_dn of this UserGroup.  # noqa: E501
        :type: str
        """

        self._ldap_group_dn = ldap_group_dn

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
        if not isinstance(other, UserGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
