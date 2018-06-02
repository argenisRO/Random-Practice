# Adventurer
# - Argenis Rodriguez

import src.const as c


def get_available_classes():
    '''
    Get Available Classes
    - Return a splitted list version of (_title_class_select)
      from the txt module, seperated by the { '|' }
      string and spaces.

    - Needs revision if (_title_class_select) is changed.
    '''
    _avail_classes = c._title_class_select[2:-2].lower().split(' | ')
    return _avail_classes
