from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTAINS: _ClassVar[MatchType]
    EXACT: _ClassVar[MatchType]
    PRESENCE: _ClassVar[MatchType]

CONTAINS: MatchType
EXACT: MatchType
PRESENCE: MatchType
OPTIONS_FIELD_NUMBER: _ClassVar[int]
options: _descriptor.FieldDescriptor
MESSAGE_FIELD_NUMBER: _ClassVar[int]
message: _descriptor.FieldDescriptor
FIELD_FIELD_NUMBER: _ClassVar[int]
field: _descriptor.FieldDescriptor
ENUM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
enum_options: _descriptor.FieldDescriptor
ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
enum_value: _descriptor.FieldDescriptor
ONEOF_FIELD_NUMBER: _ClassVar[int]
oneof: _descriptor.FieldDescriptor

class ScalaPbOptions(_message.Message):
    __slots__ = (
        "package_name",
        "flat_package",
        "preamble",
        "single_file",
        "no_primitive_wrappers",
        "primitive_wrappers",
        "collection_type",
        "preserve_unknown_fields",
        "object_name",
        "scope",
        "lenses",
        "retain_source_code_info",
        "map_type",
        "no_default_values_in_constructor",
        "enum_value_naming",
        "enum_strip_prefix",
        "bytes_type",
        "java_conversions",
        "aux_message_options",
        "aux_field_options",
        "aux_enum_options",
        "aux_enum_value_options",
        "preprocessors",
        "field_transformations",
        "ignore_all_transformations",
        "getters",
        "scala3_sources",
        "test_only_no_java_conversions",
    )
    Extensions: _python_message._ExtensionDict

    class OptionsScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILE: _ClassVar[ScalaPbOptions.OptionsScope]
        PACKAGE: _ClassVar[ScalaPbOptions.OptionsScope]
    FILE: ScalaPbOptions.OptionsScope
    PACKAGE: ScalaPbOptions.OptionsScope

    class EnumValueNaming(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AS_IN_PROTO: _ClassVar[ScalaPbOptions.EnumValueNaming]
        CAMEL_CASE: _ClassVar[ScalaPbOptions.EnumValueNaming]
    AS_IN_PROTO: ScalaPbOptions.EnumValueNaming
    CAMEL_CASE: ScalaPbOptions.EnumValueNaming

    class AuxMessageOptions(_message.Message):
        __slots__ = ("target", "options")
        TARGET_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        target: str
        options: MessageOptions
        def __init__(
            self,
            target: _Optional[str] = ...,
            options: _Optional[_Union[MessageOptions, _Mapping]] = ...,
        ) -> None: ...

    class AuxFieldOptions(_message.Message):
        __slots__ = ("target", "options")
        TARGET_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        target: str
        options: FieldOptions
        def __init__(
            self,
            target: _Optional[str] = ...,
            options: _Optional[_Union[FieldOptions, _Mapping]] = ...,
        ) -> None: ...

    class AuxEnumOptions(_message.Message):
        __slots__ = ("target", "options")
        TARGET_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        target: str
        options: EnumOptions
        def __init__(
            self,
            target: _Optional[str] = ...,
            options: _Optional[_Union[EnumOptions, _Mapping]] = ...,
        ) -> None: ...

    class AuxEnumValueOptions(_message.Message):
        __slots__ = ("target", "options")
        TARGET_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        target: str
        options: EnumValueOptions
        def __init__(
            self,
            target: _Optional[str] = ...,
            options: _Optional[_Union[EnumValueOptions, _Mapping]] = ...,
        ) -> None: ...
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    FLAT_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    PREAMBLE_FIELD_NUMBER: _ClassVar[int]
    SINGLE_FILE_FIELD_NUMBER: _ClassVar[int]
    NO_PRIMITIVE_WRAPPERS_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_WRAPPERS_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_UNKNOWN_FIELDS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    LENSES_FIELD_NUMBER: _ClassVar[int]
    RETAIN_SOURCE_CODE_INFO_FIELD_NUMBER: _ClassVar[int]
    MAP_TYPE_FIELD_NUMBER: _ClassVar[int]
    NO_DEFAULT_VALUES_IN_CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_NAMING_FIELD_NUMBER: _ClassVar[int]
    ENUM_STRIP_PREFIX_FIELD_NUMBER: _ClassVar[int]
    BYTES_TYPE_FIELD_NUMBER: _ClassVar[int]
    JAVA_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    AUX_MESSAGE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AUX_FIELD_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AUX_ENUM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AUX_ENUM_VALUE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PREPROCESSORS_FIELD_NUMBER: _ClassVar[int]
    FIELD_TRANSFORMATIONS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ALL_TRANSFORMATIONS_FIELD_NUMBER: _ClassVar[int]
    GETTERS_FIELD_NUMBER: _ClassVar[int]
    SCALA3_SOURCES_FIELD_NUMBER: _ClassVar[int]
    TEST_ONLY_NO_JAVA_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    package_name: str
    flat_package: bool
    preamble: _containers.RepeatedScalarFieldContainer[str]
    single_file: bool
    no_primitive_wrappers: bool
    primitive_wrappers: bool
    collection_type: str
    preserve_unknown_fields: bool
    object_name: str
    scope: ScalaPbOptions.OptionsScope
    lenses: bool
    retain_source_code_info: bool
    map_type: str
    no_default_values_in_constructor: bool
    enum_value_naming: ScalaPbOptions.EnumValueNaming
    enum_strip_prefix: bool
    bytes_type: str
    java_conversions: bool
    aux_message_options: _containers.RepeatedCompositeFieldContainer[
        ScalaPbOptions.AuxMessageOptions
    ]
    aux_field_options: _containers.RepeatedCompositeFieldContainer[
        ScalaPbOptions.AuxFieldOptions
    ]
    aux_enum_options: _containers.RepeatedCompositeFieldContainer[
        ScalaPbOptions.AuxEnumOptions
    ]
    aux_enum_value_options: _containers.RepeatedCompositeFieldContainer[
        ScalaPbOptions.AuxEnumValueOptions
    ]
    preprocessors: _containers.RepeatedScalarFieldContainer[str]
    field_transformations: _containers.RepeatedCompositeFieldContainer[
        FieldTransformation
    ]
    ignore_all_transformations: bool
    getters: bool
    scala3_sources: bool
    test_only_no_java_conversions: bool
    def __init__(
        self,
        package_name: _Optional[str] = ...,
        flat_package: bool = ...,
        preamble: _Optional[_Iterable[str]] = ...,
        single_file: bool = ...,
        no_primitive_wrappers: bool = ...,
        primitive_wrappers: bool = ...,
        collection_type: _Optional[str] = ...,
        preserve_unknown_fields: bool = ...,
        object_name: _Optional[str] = ...,
        scope: _Optional[_Union[ScalaPbOptions.OptionsScope, str]] = ...,
        lenses: bool = ...,
        retain_source_code_info: bool = ...,
        map_type: _Optional[str] = ...,
        no_default_values_in_constructor: bool = ...,
        enum_value_naming: _Optional[_Union[ScalaPbOptions.EnumValueNaming, str]] = ...,
        enum_strip_prefix: bool = ...,
        bytes_type: _Optional[str] = ...,
        java_conversions: bool = ...,
        aux_message_options: _Optional[
            _Iterable[_Union[ScalaPbOptions.AuxMessageOptions, _Mapping]]
        ] = ...,
        aux_field_options: _Optional[
            _Iterable[_Union[ScalaPbOptions.AuxFieldOptions, _Mapping]]
        ] = ...,
        aux_enum_options: _Optional[
            _Iterable[_Union[ScalaPbOptions.AuxEnumOptions, _Mapping]]
        ] = ...,
        aux_enum_value_options: _Optional[
            _Iterable[_Union[ScalaPbOptions.AuxEnumValueOptions, _Mapping]]
        ] = ...,
        preprocessors: _Optional[_Iterable[str]] = ...,
        field_transformations: _Optional[
            _Iterable[_Union[FieldTransformation, _Mapping]]
        ] = ...,
        ignore_all_transformations: bool = ...,
        getters: bool = ...,
        scala3_sources: bool = ...,
        test_only_no_java_conversions: bool = ...,
        **kwargs
    ) -> None: ...

class MessageOptions(_message.Message):
    __slots__ = (
        "extends",
        "companion_extends",
        "annotations",
        "type",
        "companion_annotations",
        "sealed_oneof_extends",
        "no_box",
        "unknown_fields_annotations",
        "no_default_values_in_constructor",
        "sealed_oneof_companion_extends",
        "derives",
        "sealed_oneof_derives",
    )
    Extensions: _python_message._ExtensionDict
    EXTENDS_FIELD_NUMBER: _ClassVar[int]
    COMPANION_EXTENDS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPANION_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SEALED_ONEOF_EXTENDS_FIELD_NUMBER: _ClassVar[int]
    NO_BOX_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FIELDS_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    NO_DEFAULT_VALUES_IN_CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    SEALED_ONEOF_COMPANION_EXTENDS_FIELD_NUMBER: _ClassVar[int]
    DERIVES_FIELD_NUMBER: _ClassVar[int]
    SEALED_ONEOF_DERIVES_FIELD_NUMBER: _ClassVar[int]
    extends: _containers.RepeatedScalarFieldContainer[str]
    companion_extends: _containers.RepeatedScalarFieldContainer[str]
    annotations: _containers.RepeatedScalarFieldContainer[str]
    type: str
    companion_annotations: _containers.RepeatedScalarFieldContainer[str]
    sealed_oneof_extends: _containers.RepeatedScalarFieldContainer[str]
    no_box: bool
    unknown_fields_annotations: _containers.RepeatedScalarFieldContainer[str]
    no_default_values_in_constructor: bool
    sealed_oneof_companion_extends: _containers.RepeatedScalarFieldContainer[str]
    derives: _containers.RepeatedScalarFieldContainer[str]
    sealed_oneof_derives: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        extends: _Optional[_Iterable[str]] = ...,
        companion_extends: _Optional[_Iterable[str]] = ...,
        annotations: _Optional[_Iterable[str]] = ...,
        type: _Optional[str] = ...,
        companion_annotations: _Optional[_Iterable[str]] = ...,
        sealed_oneof_extends: _Optional[_Iterable[str]] = ...,
        no_box: bool = ...,
        unknown_fields_annotations: _Optional[_Iterable[str]] = ...,
        no_default_values_in_constructor: bool = ...,
        sealed_oneof_companion_extends: _Optional[_Iterable[str]] = ...,
        derives: _Optional[_Iterable[str]] = ...,
        sealed_oneof_derives: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class Collection(_message.Message):
    __slots__ = ("type", "non_empty", "adapter")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NON_EMPTY_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_FIELD_NUMBER: _ClassVar[int]
    type: str
    non_empty: bool
    adapter: str
    def __init__(
        self,
        type: _Optional[str] = ...,
        non_empty: bool = ...,
        adapter: _Optional[str] = ...,
    ) -> None: ...

class FieldOptions(_message.Message):
    __slots__ = (
        "type",
        "scala_name",
        "collection_type",
        "collection",
        "key_type",
        "value_type",
        "annotations",
        "map_type",
        "no_default_value_in_constructor",
        "no_box",
        "required",
    )
    Extensions: _python_message._ExtensionDict
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCALA_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    MAP_TYPE_FIELD_NUMBER: _ClassVar[int]
    NO_DEFAULT_VALUE_IN_CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    NO_BOX_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    type: str
    scala_name: str
    collection_type: str
    collection: Collection
    key_type: str
    value_type: str
    annotations: _containers.RepeatedScalarFieldContainer[str]
    map_type: str
    no_default_value_in_constructor: bool
    no_box: bool
    required: bool
    def __init__(
        self,
        type: _Optional[str] = ...,
        scala_name: _Optional[str] = ...,
        collection_type: _Optional[str] = ...,
        collection: _Optional[_Union[Collection, _Mapping]] = ...,
        key_type: _Optional[str] = ...,
        value_type: _Optional[str] = ...,
        annotations: _Optional[_Iterable[str]] = ...,
        map_type: _Optional[str] = ...,
        no_default_value_in_constructor: bool = ...,
        no_box: bool = ...,
        required: bool = ...,
    ) -> None: ...

class EnumOptions(_message.Message):
    __slots__ = (
        "extends",
        "companion_extends",
        "type",
        "base_annotations",
        "recognized_annotations",
        "unrecognized_annotations",
    )
    Extensions: _python_message._ExtensionDict
    EXTENDS_FIELD_NUMBER: _ClassVar[int]
    COMPANION_EXTENDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BASE_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    RECOGNIZED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UNRECOGNIZED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    extends: _containers.RepeatedScalarFieldContainer[str]
    companion_extends: _containers.RepeatedScalarFieldContainer[str]
    type: str
    base_annotations: _containers.RepeatedScalarFieldContainer[str]
    recognized_annotations: _containers.RepeatedScalarFieldContainer[str]
    unrecognized_annotations: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        extends: _Optional[_Iterable[str]] = ...,
        companion_extends: _Optional[_Iterable[str]] = ...,
        type: _Optional[str] = ...,
        base_annotations: _Optional[_Iterable[str]] = ...,
        recognized_annotations: _Optional[_Iterable[str]] = ...,
        unrecognized_annotations: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class EnumValueOptions(_message.Message):
    __slots__ = ("extends", "scala_name", "annotations")
    Extensions: _python_message._ExtensionDict
    EXTENDS_FIELD_NUMBER: _ClassVar[int]
    SCALA_NAME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    extends: _containers.RepeatedScalarFieldContainer[str]
    scala_name: str
    annotations: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        extends: _Optional[_Iterable[str]] = ...,
        scala_name: _Optional[str] = ...,
        annotations: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class OneofOptions(_message.Message):
    __slots__ = ("extends", "scala_name")
    Extensions: _python_message._ExtensionDict
    EXTENDS_FIELD_NUMBER: _ClassVar[int]
    SCALA_NAME_FIELD_NUMBER: _ClassVar[int]
    extends: _containers.RepeatedScalarFieldContainer[str]
    scala_name: str
    def __init__(
        self, extends: _Optional[_Iterable[str]] = ..., scala_name: _Optional[str] = ...
    ) -> None: ...

class FieldTransformation(_message.Message):
    __slots__ = ("when", "match_type", "set")
    WHEN_FIELD_NUMBER: _ClassVar[int]
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    SET_FIELD_NUMBER: _ClassVar[int]
    when: _descriptor_pb2.FieldDescriptorProto
    match_type: MatchType
    set: _descriptor_pb2.FieldOptions
    def __init__(
        self,
        when: _Optional[_Union[_descriptor_pb2.FieldDescriptorProto, _Mapping]] = ...,
        match_type: _Optional[_Union[MatchType, str]] = ...,
        set: _Optional[_Union[_descriptor_pb2.FieldOptions, _Mapping]] = ...,
    ) -> None: ...

class PreprocessorOutput(_message.Message):
    __slots__ = ("options_by_file",)

    class OptionsByFileEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ScalaPbOptions
        def __init__(
            self,
            key: _Optional[str] = ...,
            value: _Optional[_Union[ScalaPbOptions, _Mapping]] = ...,
        ) -> None: ...
    OPTIONS_BY_FILE_FIELD_NUMBER: _ClassVar[int]
    options_by_file: _containers.MessageMap[str, ScalaPbOptions]
    def __init__(
        self, options_by_file: _Optional[_Mapping[str, ScalaPbOptions]] = ...
    ) -> None: ...
