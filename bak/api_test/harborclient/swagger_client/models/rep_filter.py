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


class RepFilter(object):
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
        'kind': 'str',
        'value': 'str',
        'pattern': 'str',
        'metadata': 'object'
    }

    attribute_map = {
        'kind': 'kind',
        'value': 'value',
        'pattern': 'pattern',
        'metadata': 'metadata'
    }

    def __init__(self, kind=None, value=None, pattern=None, metadata=None):  # noqa: E501
        """RepFilter - a model defined in Swagger"""  # noqa: E501

        self._kind = None
        self._value = None
        self._pattern = None
        self._metadata = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if value is not None:
            self.value = value
        if pattern is not None:
            self.pattern = pattern
        if metadata is not None:
            self.metadata = metadata

    @property
    def kind(self):
        """Gets the kind of this RepFilter.  # noqa: E501

        The replication policy filter kind. The valid values are project, repository and tag.  # noqa: E501

        :return: The kind of this RepFilter.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this RepFilter.

        The replication policy filter kind. The valid values are project, repository and tag.  # noqa: E501

        :param kind: The kind of this RepFilter.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def value(self):
        """Gets the value of this RepFilter.  # noqa: E501

        The value of replication policy filter. When creating repository and tag filter, filling it with the pattern as string. When creating label filter, filling it with label ID as integer.  # noqa: E501

        :return: The value of this RepFilter.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RepFilter.

        The value of replication policy filter. When creating repository and tag filter, filling it with the pattern as string. When creating label filter, filling it with label ID as integer.  # noqa: E501

        :param value: The value of this RepFilter.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def pattern(self):
        """Gets the pattern of this RepFilter.  # noqa: E501

        Depraceted, use value instead. The replication policy filter pattern.  # noqa: E501

        :return: The pattern of this RepFilter.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this RepFilter.

        Depraceted, use value instead. The replication policy filter pattern.  # noqa: E501

        :param pattern: The pattern of this RepFilter.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

    @property
    def metadata(self):
        """Gets the metadata of this RepFilter.  # noqa: E501

        This map object is the replication policy filter metadata.  # noqa: E501

        :return: The metadata of this RepFilter.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this RepFilter.

        This map object is the replication policy filter metadata.  # noqa: E501

        :param metadata: The metadata of this RepFilter.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

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
        if not isinstance(other, RepFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
