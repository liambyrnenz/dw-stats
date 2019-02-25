# Liam Byrne (liambyrnenz)
# DWStats

# Season tuples begin from the 9th Doctor
SEASONS_AND_EPISODES = [(27, 13), (28, 13), (29, 13),
                        (30, 18), (31, 13), (32, 13), (33, 16), (34, 13), (35, 13),
                        (36, 13), (37, 11)]


def extension(season):
    """
    Return the correct page extension for the given season.
    :param season: season number
    :return: string for page extension (.htm or .html)
    """
    return ".htm" if season <= 34 else ".html"
