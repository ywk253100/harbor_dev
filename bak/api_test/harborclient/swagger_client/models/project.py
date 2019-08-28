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

from swagger_client.models.project_metadata import ProjectMetadata  # noqa: F401,E501


class Project(object):
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
        'project_id': 'int',
        'owner_id': 'int',
        'name': 'str',
        'creation_time': 'str',
        'update_time': 'str',
        'deleted': 'bool',
        'owner_name': 'str',
        'togglable': 'bool',
        'current_user_role_id': 'int',
        'repo_count': 'int',
        'metadata': 'ProjectMetadata'
    }

    attribute_map = {
        'project_id': 'project_id',
        'owner_id': 'owner_id',
        'name': 'name',
        'creation_time': 'creation_time',
        'update_time': 'update_time',
        'deleted': 'deleted',
        'owner_name': 'owner_name',
        'togglable': 'togglable',
        'current_user_role_id': 'current_user_role_id',
        'repo_count': 'repo_count',
        'metadata': 'metadata'
    }

    def __init__(self, project_id=None, owner_id=None, name=None, creation_time=None, update_time=None, deleted=None, owner_name=None, togglable=None, current_user_role_id=None, repo_count=None, metadata=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501

        self._project_id = None
        self._owner_id = None
        self._name = None
        self._creation_time = None
        self._update_time = None
        self._deleted = None
        self._owner_name = None
        self._togglable = None
        self._current_user_role_id = None
        self._repo_count = None
        self._metadata = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if owner_id is not None:
            self.owner_id = owner_id
        if name is not None:
            self.name = name
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time
        if deleted is not None:
            self.deleted = deleted
        if owner_name is not None:
            self.owner_name = owner_name
        if togglable is not None:
            self.togglable = togglable
        if current_user_role_id is not None:
            self.current_user_role_id = current_user_role_id
        if repo_count is not None:
            self.repo_count = repo_count
        if metadata is not None:
            self.metadata = metadata

    @property
    def project_id(self):
        """Gets the project_id of this Project.  # noqa: E501

        Project ID  # noqa: E501

        :return: The project_id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Project.

        Project ID  # noqa: E501

        :param project_id: The project_id of this Project.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def owner_id(self):
        """Gets the owner_id of this Project.  # noqa: E501

        The owner ID of the project always means the creator of the project.  # noqa: E501

        :return: The owner_id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Project.

        The owner ID of the project always means the creator of the project.  # noqa: E501

        :param owner_id: The owner_id of this Project.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501

        The name of the project.  # noqa: E501

        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.

        The name of the project.  # noqa: E501

        :param name: The name of this Project.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def creation_time(self):
        """Gets the creation_time of this Project.  # noqa: E501

        The creation time of the project.  # noqa: E501

        :return: The creation_time of this Project.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Project.

        The creation time of the project.  # noqa: E501

        :param creation_time: The creation_time of this Project.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this Project.  # noqa: E501

        The update time of the project.  # noqa: E501

        :return: The update_time of this Project.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Project.

        The update time of the project.  # noqa: E501

        :param update_time: The update_time of this Project.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def deleted(self):
        """Gets the deleted of this Project.  # noqa: E501

        A deletion mark of the project.  # noqa: E501

        :return: The deleted of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Project.

        A deletion mark of the project.  # noqa: E501

        :param deleted: The deleted of this Project.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def owner_name(self):
        """Gets the owner_name of this Project.  # noqa: E501

        The owner name of the project.  # noqa: E501

        :return: The owner_name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this Project.

        The owner name of the project.  # noqa: E501

        :param owner_name: The owner_name of this Project.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def togglable(self):
        """Gets the togglable of this Project.  # noqa: E501

        Correspond to the UI about whether the project's publicity is  updatable (for UI)  # noqa: E501

        :return: The togglable of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._togglable

    @togglable.setter
    def togglable(self, togglable):
        """Sets the togglable of this Project.

        Correspond to the UI about whether the project's publicity is  updatable (for UI)  # noqa: E501

        :param togglable: The togglable of this Project.  # noqa: E501
        :type: bool
        """

        self._togglable = togglable

    @property
    def current_user_role_id(self):
        """Gets the current_user_role_id of this Project.  # noqa: E501

        The role ID of the current user who triggered the API (for UI)  # noqa: E501

        :return: The current_user_role_id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._current_user_role_id

    @current_user_role_id.setter
    def current_user_role_id(self, current_user_role_id):
        """Sets the current_user_role_id of this Project.

        The role ID of the current user who triggered the API (for UI)  # noqa: E501

        :param current_user_role_id: The current_user_role_id of this Project.  # noqa: E501
        :type: int
        """

        self._current_user_role_id = current_user_role_id

    @property
    def repo_count(self):
        """Gets the repo_count of this Project.  # noqa: E501

        The number of the repositories under this project.  # noqa: E501

        :return: The repo_count of this Project.  # noqa: E501
        :rtype: int
        """
        return self._repo_count

    @repo_count.setter
    def repo_count(self, repo_count):
        """Sets the repo_count of this Project.

        The number of the repositories under this project.  # noqa: E501

        :param repo_count: The repo_count of this Project.  # noqa: E501
        :type: int
        """

        self._repo_count = repo_count

    @property
    def metadata(self):
        """Gets the metadata of this Project.  # noqa: E501

        The metadata of the project.  # noqa: E501

        :return: The metadata of this Project.  # noqa: E501
        :rtype: ProjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Project.

        The metadata of the project.  # noqa: E501

        :param metadata: The metadata of this Project.  # noqa: E501
        :type: ProjectMetadata
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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other