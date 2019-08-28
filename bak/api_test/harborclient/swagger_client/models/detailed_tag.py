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

from swagger_client.models.detailed_tag_scan_overview import DetailedTagScanOverview  # noqa: F401,E501
from swagger_client.models.label import Label  # noqa: F401,E501


class DetailedTag(object):
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
        'digest': 'str',
        'name': 'str',
        'size': 'int',
        'architecture': 'str',
        'os': 'str',
        'docker_version': 'str',
        'author': 'str',
        'created': 'str',
        'signature': 'object',
        'scan_overview': 'DetailedTagScanOverview',
        'labels': 'list[Label]'
    }

    attribute_map = {
        'digest': 'digest',
        'name': 'name',
        'size': 'size',
        'architecture': 'architecture',
        'os': 'os',
        'docker_version': 'docker_version',
        'author': 'author',
        'created': 'created',
        'signature': 'signature',
        'scan_overview': 'scan_overview',
        'labels': 'labels'
    }

    def __init__(self, digest=None, name=None, size=None, architecture=None, os=None, docker_version=None, author=None, created=None, signature=None, scan_overview=None, labels=None):  # noqa: E501
        """DetailedTag - a model defined in Swagger"""  # noqa: E501

        self._digest = None
        self._name = None
        self._size = None
        self._architecture = None
        self._os = None
        self._docker_version = None
        self._author = None
        self._created = None
        self._signature = None
        self._scan_overview = None
        self._labels = None
        self.discriminator = None

        if digest is not None:
            self.digest = digest
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if architecture is not None:
            self.architecture = architecture
        if os is not None:
            self.os = os
        if docker_version is not None:
            self.docker_version = docker_version
        if author is not None:
            self.author = author
        if created is not None:
            self.created = created
        if signature is not None:
            self.signature = signature
        if scan_overview is not None:
            self.scan_overview = scan_overview
        if labels is not None:
            self.labels = labels

    @property
    def digest(self):
        """Gets the digest of this DetailedTag.  # noqa: E501

        The digest of the tag.  # noqa: E501

        :return: The digest of this DetailedTag.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this DetailedTag.

        The digest of the tag.  # noqa: E501

        :param digest: The digest of this DetailedTag.  # noqa: E501
        :type: str
        """

        self._digest = digest

    @property
    def name(self):
        """Gets the name of this DetailedTag.  # noqa: E501

        The name of the tag.  # noqa: E501

        :return: The name of this DetailedTag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DetailedTag.

        The name of the tag.  # noqa: E501

        :param name: The name of this DetailedTag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """Gets the size of this DetailedTag.  # noqa: E501

        The size of the image.  # noqa: E501

        :return: The size of this DetailedTag.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DetailedTag.

        The size of the image.  # noqa: E501

        :param size: The size of this DetailedTag.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def architecture(self):
        """Gets the architecture of this DetailedTag.  # noqa: E501

        The architecture of the image.  # noqa: E501

        :return: The architecture of this DetailedTag.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this DetailedTag.

        The architecture of the image.  # noqa: E501

        :param architecture: The architecture of this DetailedTag.  # noqa: E501
        :type: str
        """

        self._architecture = architecture

    @property
    def os(self):
        """Gets the os of this DetailedTag.  # noqa: E501

        The os of the image.  # noqa: E501

        :return: The os of this DetailedTag.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this DetailedTag.

        The os of the image.  # noqa: E501

        :param os: The os of this DetailedTag.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def docker_version(self):
        """Gets the docker_version of this DetailedTag.  # noqa: E501

        The version of docker which builds the image.  # noqa: E501

        :return: The docker_version of this DetailedTag.  # noqa: E501
        :rtype: str
        """
        return self._docker_version

    @docker_version.setter
    def docker_version(self, docker_version):
        """Sets the docker_version of this DetailedTag.

        The version of docker which builds the image.  # noqa: E501

        :param docker_version: The docker_version of this DetailedTag.  # noqa: E501
        :type: str
        """

        self._docker_version = docker_version

    @property
    def author(self):
        """Gets the author of this DetailedTag.  # noqa: E501

        The author of the image.  # noqa: E501

        :return: The author of this DetailedTag.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this DetailedTag.

        The author of the image.  # noqa: E501

        :param author: The author of this DetailedTag.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def created(self):
        """Gets the created of this DetailedTag.  # noqa: E501

        The build time of the image.  # noqa: E501

        :return: The created of this DetailedTag.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DetailedTag.

        The build time of the image.  # noqa: E501

        :param created: The created of this DetailedTag.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def signature(self):
        """Gets the signature of this DetailedTag.  # noqa: E501

        The signature of image, defined by RepoSignature. If it is null, the image is unsigned.  # noqa: E501

        :return: The signature of this DetailedTag.  # noqa: E501
        :rtype: object
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this DetailedTag.

        The signature of image, defined by RepoSignature. If it is null, the image is unsigned.  # noqa: E501

        :param signature: The signature of this DetailedTag.  # noqa: E501
        :type: object
        """

        self._signature = signature

    @property
    def scan_overview(self):
        """Gets the scan_overview of this DetailedTag.  # noqa: E501


        :return: The scan_overview of this DetailedTag.  # noqa: E501
        :rtype: DetailedTagScanOverview
        """
        return self._scan_overview

    @scan_overview.setter
    def scan_overview(self, scan_overview):
        """Sets the scan_overview of this DetailedTag.


        :param scan_overview: The scan_overview of this DetailedTag.  # noqa: E501
        :type: DetailedTagScanOverview
        """

        self._scan_overview = scan_overview

    @property
    def labels(self):
        """Gets the labels of this DetailedTag.  # noqa: E501

        The label list.  # noqa: E501

        :return: The labels of this DetailedTag.  # noqa: E501
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this DetailedTag.

        The label list.  # noqa: E501

        :param labels: The labels of this DetailedTag.  # noqa: E501
        :type: list[Label]
        """

        self._labels = labels

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
        if not isinstance(other, DetailedTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
