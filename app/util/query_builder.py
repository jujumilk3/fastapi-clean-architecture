from sqlalchemy.sql.expression import and_

SQLALCHEMY_QUERY_MAPPER = {
    "eq": "__eq__",
    "ne": "__ne__",
    "lt": "__lt__",
    "lte": "__le__",
    "gt": "__gt__",
    "gte": "__ge__",
}


def dict_to_sqlalchemy_filter_options(model_class, search_option_dict):
    sql_alchemy_filter_options = []
    copied_dict = search_option_dict.copy()
    for key in search_option_dict:
        attr = getattr(model_class, key, None)
        if attr is None:
            continue
        option_from_dict = copied_dict.pop(key)
        if type(option_from_dict) in [int, float]:
            sql_alchemy_filter_options.append(attr == option_from_dict)
        elif type(option_from_dict) in [str]:
            sql_alchemy_filter_options.append(attr.like("%" + option_from_dict + "%"))
        elif type(option_from_dict) in [bool]:
            sql_alchemy_filter_options.append(attr.is_(option_from_dict))

    for custom_option in copied_dict:
        if "__" not in custom_option:
            continue
        key, command = custom_option.split("__")
        attr = getattr(model_class, key, None)
        if attr is None:
            continue
        option_from_dict = copied_dict[custom_option]
        if command == "in":
            sql_alchemy_filter_options.append(
                attr.in_([option.strip() for option in option_from_dict.split(",")])
            )
        elif command in SQLALCHEMY_QUERY_MAPPER.keys():
            sql_alchemy_filter_options.append(
                getattr(attr, SQLALCHEMY_QUERY_MAPPER[command])(option_from_dict)
            )
        elif command == "isnull":
            bool_command = "__eq__" if option_from_dict else "__ne__"
            sql_alchemy_filter_options.append(getattr(attr, bool_command)(None))

    return and_(True, *sql_alchemy_filter_options)
