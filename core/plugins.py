def load_modules():

    from module.print_url import print_url
    from module.print_timestamp import print_timestamp

    plugins = dict()

    urltp = print_url()
    timestamptp = print_timestamp()

    plugins['print_url'] = urltp
    plugins['print_timestamp'] = timestamptp

    return plugins

__modules__ = load_modules()
